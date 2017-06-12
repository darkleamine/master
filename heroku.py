import os
import subprocess
import json
from subprocess import CalledProcessError


class heroku:
    def __init__(self):
        pass
        #ci on cas de confidencialite fait elemenier root_pwd


        ################################################################################################################
    def build(self,ver,pack,pwd):
        os.chdir("/home/ghost/PycharmProjects/pfe/shell/")
        ver="./"+ver
        print(ver)
        list = []
        list.append(ver);list.append(" ");list.append(pack);list.append(" ");list.append("heroku_install.sh");list.append(" ");list.append(pwd)
        print("list =")
        print(list)
        cmd="".join(list)
        print ("cmd = "+cmd)
        a=os.system('echo $PWD')
        print(a)
        os.system(cmd)
        ################################################################################################################
    def authentification(self,email,pwd):
        auth = open("data.txt", "w")
        auth.write(email + '\n');
        auth.write(pwd);
        auth.close()
        print ("fin fichier")
        try:
            os.system("cat data.txt")
            login = subprocess.getoutput("heroku <data.txt")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                "command login '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        os.system('rm data.txt')

        return  login

        ################################################################################################################
    def execute(self, nom_app):
        try:
            create=subprocess.getoutput("heroku create "+nom_app)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                "command create '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        os.system('heroku create '+nom_app)
        #os.system('git remote -v')
        #os.system('git remote set-url heroku https://git.heroku.com/'+nom_app+'.git')
        try:

            deploy = subprocess.getoutput("git push heroku HEAD:master")
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command deploy '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        try:
               subprocess.getoutput("heroku open")
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command deploy '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        return create+deploy
        ################################################################################################################
    def apps(self):
        try:
           apps=subprocess.getoutput("heroku apps")
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command apps '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        return  apps
        ################################################################################################################
    def run(self,email,pwd,nom_app):
        auth = open("data.txt", "w")
        auth.write(email+'\n');auth.write(pwd);auth.close()
        #os.system('heroku  < data.txt ')
        try:
           login=subprocess.getoutput("heroku <data.txt")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                "command login '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        os.system('rm data.txt')
        #os.system('heroku create ')
        try:
            create=subprocess.getoutput("heroku create "+nom_app)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                "command create '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        os.system('git remote -v')
        os.system('git remote set-url heroku https://git.heroku.com/'+nom_app+'.git')
        try:
            deploy = subprocess.getoutput("git push heroku master")
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command deploy '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

        #os.system('heroku apps')
        try:
           apps=subprocess.getoutput("heroku apps")
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command apps '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        os.system("heroku open")
        return login,create,deploy,apps

        ################################################################################################################
    def config(self,dirctory,command_execute):
          print ("derictory ", dirctory)
          list = [];
          list.append(dirctory)
          os.chdir(dirctory)
          os.system("pwd")
        ################################################################################################################

          fichiers = os.listdir(dirctory)
          Fichier = open('procfile', 'w')
          Fichier.write(
              "  web: " + command_execute + " \n")

          Fichier.close()

#heroku_instance =heroku('verifier_la_instalation_des_logiciel.sh','heroku','darkle09')
#heroku_instance.build('verifier_la_instalation_des_logiciel.sh','heroku','darkle09')
    def container(self,nom_app):

        try:
            login = subprocess.getoutput("heroku container:login")
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command login to container contexte '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        try:
            create = subprocess.getoutput("heroku create "+nom_app)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                "command create app to container service '{}' return with error (code {}): {}".format(e.cmd, e.returncode,
                                                                                                  e.output))
        try:
            print("la")
            deploy = subprocess.getoutput("heroku container:push web --app "+nom_app)
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command deploy to container contexte '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        try:
            print ("lala")
            run_browser = subprocess.getoutput("heroku open --app"+nom_app)
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command deploy to container contexte '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

        return deploy


































"""
    if "package.json" in fichiers:
        json_data = open("package.json").read()
        data = json.loads(json_data)
        m = data["scripts"]["start"]
        print(m)
        Fichier.write(
            "  web: " + m + " \n")  # donner le buildpack pour nodejs
    elif "requirements.txt" in fichiers:
        Fichier.write(
            " web: gunicorn gettingstarted.wsgi --log-file - \n")  # donner le buildpack pour python
    elif "composer.json" in fichiers:
        Fichier.write(
            "  web: vendor/bin/heroku-php-apache2 web/  \n")  # donner le buildpack pour php
        # Fichier.write("  instances : 2 \n")
"""