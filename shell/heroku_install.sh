#!/bin/bash
chmod +x heroku_install.sh
sudo -S add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./"<<<$1

 #curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -

 #sudo apt-get update

 sudo -S apt-get -y install heroku<<<$1
 #sudo apt install heimdal-clients
 heroku plugins:install  heroku-container-tools