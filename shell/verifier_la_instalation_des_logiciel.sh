#!/bin/bash
chmod 777 verifier_la_instalation_des_logiciel.sh
    echo $1 $2 $3
  apt-cache pkgnames  > log_install.txt
   var=$(grep -c $1 log_install.txt)
#  -gt == supereur
# -eq == equivalant
 if [ $var -eq "0" ];
  then
    echo "package non installer";echo ./$2 $3;
    ./$2 $3;
  else   echo "package  installer";./$2 $3;fi
