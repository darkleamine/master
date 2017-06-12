#!/bin/bash
sudo -S apt-get install -y ruby-full <<<$1
sudo  apt-get install -y rubygems <<<$1
sudo -S gem install engineyard <<<$1





