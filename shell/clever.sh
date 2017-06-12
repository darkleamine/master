#!/bin/bash

npm list -g > log_install_npm.txt
var=$(grep -c $1 log_install_npm.txt)
#  -gt == supereur
# -eq == equivalant
sudo -S apt-get -y install openssl <<<$2
 if [ $var -eq "0" ];
  then
    echo "package non installer";
    #sudo -S npm install -g clever-tools <<<$2;
  else   echo "package  installer"; #sudo -S npm install -g clever-tools <<<$2;
  fi;