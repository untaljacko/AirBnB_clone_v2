#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack. """
from datetime import datetime
from fabric.api import local


def do_pack():
    """ doc do_pack """
    local("mkdir -p versions")
    new_pack = "versions/web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S"))
    def_pack = local("tar -cvzf {} web_static".format(new_pack))
    return def_pack
