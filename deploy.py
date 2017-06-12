import developpeur
import application
import provider
from ibm import *
from  pivotel import *
from  heroku import *
from clever import *
from developpeur import *
from application import *
class deploy:
    global pack_aws, pack_ibm, pack_pivotel, pack_heroku, pack_engine_yard, ver_package_install, console, console_app
    ver_package_install = 'verifier_la_instalation_des_logiciel.sh'
    pack_aws = "awscli"
    pack_ibm = 'cf-cli'
    pack_pivotel = pack_ibm
    pack_heroku = 'heroku'

    def __init__(self,nom_dev,password,pwd_os,pack,nom_app,path):#command
           self.dev= developpeur(nom_dev,password,pwd_os,pack)
           self.app= application(nom_app,path)#,command
           #self.provider = provider()


    def deploy_fun (self,ver,pack,pwd_os,titre,path,nom_app,nom_dev,password,tech,command_execute):
        #self.build(ver,pack,pwd_os,titre)
        self.config(path,nom_app,pack,titre,command_execute)
        login =self.authentification(pack,nom_dev,password,titre)
        if(tech=="runtime"):
            deployer = self.run(pack,nom_app,titre)
        else:
            deployer=self.container(pack,titre,nom_app)
        apps=self.apps(pack,titre)
        return  login,deployer,apps
        ########################################################################################################################
    def build( self,ver, pack, pwd_os, titre):
            if (pack == pack_ibm and titre == 'IBM'):
                ibm_instance = ibm()
                ibm_instance.build( ver_package_install, pack, pwd_os)
            elif (pack == pack_heroku):
                heroku_instance = heroku()
                heroku_instance.build( ver_package_install, pack, pwd_os)
            else:
                pivotel_instance = pivotel()
                pivotel_instance.build( ver_package_install, pack, pwd_os)
                ########################################################################################################################

    def config(self, dirctory, nom_app, pack, titre,command_execute):
            if (pack == pack_ibm and titre == 'IBM'):
                ibm_instance = ibm()
                ibm_instance.config( dirctory, nom_app,command_execute)
            elif (pack == pack_heroku):
                heroku_instance = heroku()
                heroku_instance.config( dirctory,command_execute)
            else:
                pivotel_instance = pivotel()
                pivotel_instance.config( dirctory, nom_app,command_execute)
                ########################################################################################################################

    def authentification(self, pack, email,password, titre):
            if (pack == pack_ibm and titre == 'IBM'):
                ibm_instance = ibm()
                login=ibm_instance.authentification( email, password)
            elif (pack == pack_heroku):
                heroku_instance = heroku()
                login =heroku_instance.authentification( email, password)
            else:
                pivotel_instance = pivotel()
                login=pivotel_instance.authentification( email, password)
            return login
                ########################################################################################################################

    def run(self, pack, nom_app, titre):
            if (pack == pack_ibm and titre == 'IBM'):
                ibm_instance = ibm()
                deployer=ibm_instance.execute( nom_app)
            elif (pack == pack_heroku):
                heroku_instance = heroku()
                deployer=heroku_instance.execute( nom_app)
            else:
                pivotel_instance = pivotel()
                deployer=pivotel_instance.execute( nom_app)
            return deployer
                ########################################################################################################################

    def apps(self, pack, titre):
            if (pack == pack_ibm and titre == 'IBM'):
                ibm_instance = ibm()
                apps=ibm_instance.apps()
            elif (pack == pack_heroku):
                heroku_instance = heroku()
                apps=heroku_instance.apps()
            else:
                pivotel_instance = pivotel()
                apps=pivotel_instance.apps()

            return  apps
    def container(self,pack,titre,nom_app):
        if (pack == pack_ibm and titre == 'IBM'):
            ibm_instance = ibm()
            #deployer = ibm_instance.apps()
        elif (pack == pack_heroku):
            heroku_instance = heroku()
            deployer = heroku_instance.container(nom_app)
        else:
            pivotel_instance = pivotel()
            #deployer = pivotel_instance.apps()
        return deployer