from tkinter import *
from  developpeur import *
from application import  *

pack="heroku"
ibm_config = Tk()
ibm_config.title("cloud provider amine ")
ibm_config.config()
ibm_config.wm_minsize(250, 200)
global nom,pwd,pwd_sys
                ########################################### dev info
nom = Entry(ibm_config,bg="white")
                #nom.insert(0,"koudjil10@gmail.com")
nom.insert(0,nom.get())
pwd = Entry(ibm_config, show="*",bg="white")
                #pwd.insert(0,"Darkle09&")
pwd_sys=Entry(ibm_config,show='*',bg="white")
                #pwd_sys.insert(0, "darkle09")
                ############################################## nom egale email  utilisateur object
                #nom_utilisateur , rest = nom.get().split("@")
nom_utilisateur  = developpeur(nom.get(), pwd.get(),pwd_sys.get(),pack)
                ############################################## label dev
nom_label = Label(ibm_config, text="email", font='bold')
pwd_label = Label(ibm_config, text="pwd", font='bold')
pwd_sys_label = Label(ibm_config, text='pwd_sys', font='bold')
note = Label(ibm_config,text='root pwd pour install package '+pack,fg='red')
path_label = Label(ibm_config,text="path",font='bold')
                ############################################## app
path_entry = Entry(ibm_config,bg="white",text='')
browse =Button(ibm_config,text="directory",command=lambda :self.repertoire(path_entry))
nom_app_label = Label(ibm_config, text="app name", font='bold')
nom_app_entry = Entry(ibm_config, bg="white" )
                #nom_app_entry.insert(0, "amine3150910")
                #command_app_label=Label(ibm_config,text="command run app", font='bold')
                #command_app_entry= Entry(ibm_config,bg="white")
                #################################################### app object

app = application(nom_app_entry.get(),path_entry)#,command_app_entry.get()
                ####################################################
#get_inf=Button (ibm_config,text="done",command=lambda :self.aff(pack,titre,nom_app_entry.get(),nom_utilisateur,app,tech="runtime"))
                #get_inf = Button(ibm_config, text="done",command=lambda: self.aff(pack, titre, nom_app_entry.get(),command_app_entry,path_entry,nom.get,tech="runtime"))
#button_docker=Button (ibm_config,text="docker",command=lambda :self.aff(pack,titre,nom_app_entry.get(),nom_utilisateur,app,tech="docker"))
                #############################################################################

def aff(self, pack, titre, nom_app, nom_utilisateur, app, tech):
                                print ("app  object name=", app.nom_app, "path= ", app.path)
                                print("utilisateur object=", nom_utilisateur.email, " password=", nom_utilisateur.password, " password os=",
                                nom_utilisateur.pwd_os, "pack ", nom_utilisateur.pack)

                                console.delete(1.0, END)
                                console_app.delete(1.0,END)
                                print("utilisateur object",nom_utilisateur.email," password",nom_utilisateur.password," password os",nom_utilisateur.pwd_os,"pack ",nom_utilisateur.pack)
                                app.path=dirc
                                print ("app  object name=",app.nom_app,"path ",app.path)#,"command",app.command
    #####
                                ver = 'verifier_la_instalation_des_logiciel.sh'
                                deploy_ins =deploy(nom_utilisateur.email,nom_utilisateur.password,nom_utilisateur.pwd_os,pack,app.nom_app,app.path)#,app.command
                                login, deployer ,apps=deploy_ins.deploy_fun(ver,pack,nom_utilisateur.pwd_os,titre,app.path,app.nom_app,nom_utilisateur.email,nom_utilisateur.password,tech)
                                console.insert(END, "***********************login********************************* *\n" + login + "\n")
                                console.insert(END, "***********************deploy**********************************\n" + deployer + "\n")
                                console_app.insert(END,"***********************apps*********************************\n"+ apps + "\n")


                #################################################### placement dans frame
nom.grid(row=0,column=1)
nom.delete(0, END)
nom_label.grid(row=0, column=0)
pwd.grid(row=1,column=1)
pwd_label.grid(row=1, column=0)
pwd_sys.grid(row=2,column=1)
pwd_sys_label.grid(row=2,column=0)
#get_inf.grid(row=5,column=2)
#button_docker.grid(row=6,column=2)
#command_app_label.grid(row=6,column=0)
#command_app_entry.grid(row=6,column=1)
note.grid(row=3,column=1)
path_label.grid(row=4,column=0)
path_entry.grid(row=4,column=1)
browse.grid(row=4,column=2)
nom_app_label.grid(row=5,column=0)
nom_app_entry.grid(row=5,column=1)
print ("amine",)
ibm_config.mainloop()




