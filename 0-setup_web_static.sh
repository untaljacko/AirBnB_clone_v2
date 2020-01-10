#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static according to some directives.
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /dta/web_static/shared/
sudo echo -e "<html>
  <head>
    </head>
      <body>
          Holberton School
     </body>
     </html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
n_route="\\\n\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}"
sudo sed -i "51i $n_route" /etc/nginx/sites-available/default
sudo service nginx restart
