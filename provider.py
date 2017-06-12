from ibm import *
from  pivotel import *
from  heroku import *
from developpeur import *
class provider:
    global pack_aws, pack_ibm, pack_pivotel, pack_heroku, pack_engine_yard, ver_package_install, console, console_app
    ver_package_install = 'verifier_la_instalation_des_logiciel.sh'
    pack_aws = "awscli"
    pack_ibm = 'cf-cli'
    pack_pivotel = pack_ibm
    pack_heroku = 'heroku'

    def __init__(self,nom_provider):
        self.nom_provider=nom_provider

########################################################################################################################
    def build(self,ver,pack,pwd_os,titre):
        if (pack == pack_ibm and titre == 'IBM'):
            ibm_instance = ibm()
            ibm_instance.build(self,ver_package_install, pack, pwd_os)
        elif(pack == pack_heroku):
            heroku_instance = heroku()
            heroku_instance.build(self,ver_package_install, pack, pwd_os)
        else:
            pivotel_instance = pivotel()
            pivotel_instance.build(self,ver_package_install, pack, pwd_os)
########################################################################################################################
    def config(self,dirctory,nom_app,pack,titre):
        if (pack == pack_ibm and titre == 'IBM'):
            ibm_instance = ibm()
            ibm_instance.config(self,dirctory,nom_app)
        elif (pack == pack_heroku):
            heroku_instance = heroku()
            heroku_instance.config(self,dirctory)
        else:
            pivotel_instance = pivotel()
            pivotel_instance.config(self,dirctory,nom_app)
########################################################################################################################
    def authentification (self,pack,dev,titre):
        if (pack == pack_ibm and titre == 'IBM'):
            ibm_instance = ibm()
            ibm_instance.authentification(self,dev.email,dev.password)
        elif (pack == pack_heroku):
            heroku_instance = heroku()
            heroku_instance.authentification(self,dev.email,dev.password)
        else:
            pivotel_instance = pivotel()
            pivotel_instance.authentification(self,dev.email,dev.password)
########################################################################################################################
    def run (self,pack,nom_app,titre):
        if (pack == pack_ibm and titre == 'IBM'):
            ibm_instance = ibm()
            ibm_instance.execute (self,nom_app)
        elif (pack == pack_heroku):
            heroku_instance = heroku()
            heroku_instance.execute(self, nom_app)
        else:
            pivotel_instance = pivotel()
            pivotel_instance.execute (self,nom_app)
########################################################################################################################
    def apps(self,pack,titre):
        if (pack == pack_ibm and titre == 'IBM'):
            ibm_instance = ibm()
            ibm_instance.apps()
        elif (pack == pack_heroku):
            heroku_instance = heroku()
            heroku_instance.apps()
        else:
            pivotel_instance = pivotel()
            pivotel_instance.apps()


