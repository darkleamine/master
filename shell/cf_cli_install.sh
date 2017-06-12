#!/bin/bash
wget -q -O - https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | sudo apt-key add 

echo "deb http://packages.cloudfoundry.org/debian stable main" | sudo tee /etc/apt/sources.list.d/cloudfoundry-cli.list

#sudo apt-get update

sudo -S apt-get -y install cf-cli <<<$1
cf install-plugin -f https://static-ice.ng.bluemix.net/ibm-containers-linux_x64