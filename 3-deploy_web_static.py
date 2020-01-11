#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy """
from datetime import datetime
from fabric.api import local, run, put, env
from os.path import exists


env.hosts = ['35.243.184.141', '35.243.142.241']


def do_pack():
    """ doc do_pack """
    local("mkdir -p versions")
    new_pack = "versions/web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S"))
    def_pack = local("tar -cvzf {} web_static".format(new_pack))
    return def_pack


def do_deploy(archive_path):
    """ doc do_deploy """
    if exists(archive_path):
        put(archive_path, "/tmp/")
        pack_file = archive_path.split("/")[1].split(".")[0]
        remote_path = "/data/web_static/releases/{}".format(pack_file)
        run("mkdir {}".format(remote_path))
        run("tar -zxvf /tmp/{}.tgz --directory {}/".format(
            pack_file, remote_path))
        run("rm /tmp/{}".format(archive_path.split("/")[1]))
        run("rm /data/web_static/current")
        run("ln -sf /data/web_static/releases/{}\
            /data/web_static/current".format(pack_file))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/current/".format(pack_file))
        run("rm -rf /data/web_static/releases/{}/web_static/".format(
            pack_file))
        return True
    else:
        return False


def deploy():
    """ doc deploy """
    try:
        archive_path = do_pack()
    except:
        return False
    return do_deploy(archive_path)

    return do_deploy(archive_path)
