#!/usr/bin/python3.5
from tkinter import *
from tkinter.messagebox import *
import tkinter.filedialog
from developpeur import *
from application import *
from deploy import *





def repertoire( path_entry):
    global dirc
    path_entry.delete(0, END)
    console.delete(1.0, END);
    dirc = tkinter.filedialog.askdirectory(initialdir='/home/ghost', title='Select your app folder')
    path_entry.insert(0, dirc)
    path_entry = dirc
    return dirc
def choix(fournisseur,title):
    global pack,titre,tech
    pack=fournisseur
    titre=title
    print("pack =",pack,"fournissuer",titre)
    showinfo(pack, "Déploiement sur "+titre)
    context=askquestion("Contexte d'execution", "Docker [YES/NO]", icon='warning')
    if context =="yes":
        tech="docker"
    else:
        tech="runtime"
def show_entry_fields():
   #list=[]
   print("First Name: %s\npassword: %s\npassword_system :  %s\nchemins :  %s\nrun command :   %s\napplication : %s" % (email.get(), pwd.get(),pwd_sys.get(),path.get(),run_command.get(),app_name.get()))
   dev = developpeur(email.get(),pwd.get(),pwd_sys.get(),pack)
   print(" a ",dev.email," p",dev.password)
   app =application(app_name.get(),path.get())
   print("app ",app.nom_app,"app path ",app.path)
   print("pack =",pack,"fournissuer", titre)
   console.delete(1.0, END)
   console_app.delete(1.0, END);
   deploy_ins = deploy(dev.email, dev.password, dev.pwd_os, pack, app.nom_app,app.path)  # ,app.command
   login, deployer, apps = deploy_ins.deploy_fun(ver_package_install, pack, dev.pwd_os, titre, app.path, app.nom_app,dev.email,dev.password, tech,run_command.get())
   console.insert(END, "***********************login********************************* *\n" + login + "\n")
   console.insert(END, "***********************deploy**********************************\n" + deployer + "\n")
   console_app.insert(END, "***********************apps*********************************\n" + apps + "\n")

master = Tk()
master.wm_minsize(800,600)
master.wm_maxsize(800,600)
master.title("DAC:Déploiement des applications sur le Cloud")
global pack_aws, pack_ibm, pack_pivotel, pack_heroku, pack_engine_yard, ver_package_install,console,console_app
ver_package_install = 'verifier_la_instalation_des_logiciel.sh'
pack_aws = "awscli"
pack_ibm = 'cf-cli'
pack_pivotel = pack_ibm
pack_heroku = 'heroku'
aws_photo=PhotoImage(file="/home/ghost/PycharmProjects/pfe/icone/aws.png")
ibm_photo=PhotoImage(file="/home/ghost/PycharmProjects/pfe/icone/ibm.png")
heroku_photo=PhotoImage(file="/home/ghost/PycharmProjects/pfe/icone/heroku.png")
pivotel_photo=PhotoImage(file="/home/ghost/PycharmProjects/pfe/icone/pivotel.png")
aws_button = Button(master, text="aws", image=aws_photo, width=100, height=50,command=lambda :choix(pack_aws,"amazon"))#,command=lambda: self.fun(pack_aws, 'Amazon AWS'))
ibm_button = Button(master, text="ibm", image=ibm_photo, width=100, height=50,command=lambda :choix(pack_ibm,"IBM"))#, command=lambda: self.fun(pack_ibm, 'IBM'))
heroku_button = Button(master, text="heroku", image=heroku_photo, width=100, height=50,command=lambda :choix(pack_heroku,"Heroku"))#,command=lambda: self.fun(pack_heroku, 'Heroku'))
pivotel_button = Button(master, text="pivotel", image=pivotel_photo, width=100, height=50,command=lambda :choix(pack_pivotel,"Pivotal"))#,command=lambda: self.fun(pack_pivotel, 'Pivotel'))
aws_button.place(x=10, y=25)
ibm_button.place(x=10, y=120)
heroku_button.place(x=10,y=200)
pivotel_button.place(x=10, y=290)
#####################################
information = Frame(master)
information.place(x=160,y=350,width=600,height=500)
Label(information , text="Email:",anchor=W,width=25).grid(row=0)
Label(information , text="Mote de passe:",anchor=W,width=25).grid(row=5)
Label(information , text="Mote de passe system:",anchor=W,width=25).grid(row=10)
Label(information , text="Pour install outils d'interaction:",anchor=W,width=25).grid(row=20,column=1)
Label(information , text="Chemins vers application:",anchor=W,width=25).grid(row=28)
Label(information , text="run command:",anchor=W,width=25).grid(row=50)
Label(information , text="Nom application:",anchor=W,width=25).grid(row=70)
Label(master,text="Console:",anchor=W,font="bold").place(x=120,y=10)
var_email =StringVar()
email = Entry(information,width=25,bg="white",textvariable=var_email)
var_email.set("amine@live.fr")
pwd = Entry(information ,width=25,bg="white",show="*")
pwd_sys=Entry(information,width=25 ,bg="white",show="*")
path=Entry(information ,width=25,bg="white")
run_command=Entry(information,width=25,bg="white")
app_name=Entry(information ,width=25,bg="white")

email.grid(row=0, column=1)
pwd.grid(row=5, column=1)
pwd_sys.grid(row=10,column=1)
path.grid(row=28,column=1)
run_command.grid(row=50,column=1)
app_name.grid(row=70,column=1)

#### determine le chemin de l'application
browse = Button(information, text="directory",width=10,bg="gray75" ,command=lambda: repertoire(path)).grid(row=28,column=2)
####affiche les application
applications=Label(master,text='application',font="bold").place(x=120,y=230)
console_app = Text(master, bg="black", fg="white")
console_app.place(x=120,y=250,height=100,width=650)
###sticky pour l'alignement des borders selon
Button(information, text='deployer', width=10,bg="gray75",command=show_entry_fields).grid(row=70, column=2, sticky=W, pady=4)
### console pour affiche log applications
console = Text(master,bg="black",fg="white")
console.place(x=120,y=30,height=200,width=650)
#### bare de diffelement assoccier aux console
button_scrollbar = Scrollbar(console,bg="#696969",activebackground="#696969")
button_scrollbar.pack(side=RIGHT, fill=Y)
console.config(  yscrollcommand = button_scrollbar.set)
mainloop( )


















































"""
import tkinter.filedialog
ibm_config = Tk()
ibm_config.title("cloud provider ")
ibm_config.config()
ibm_config.wm_minsize(250, 200)
def collect(nom,pwd,pwd_sys):
    list=[]
    list.append(nom);list.append(pwd);list.append(pwd_sys)
    print(list)
    return list

def repertoire(path_entry):
    global dirc
    path_entry.delete(0, END)
    #console.delete(1.0, END)
    dirc = tkinter.filedialog.askdirectory(initialdir='/home/ghost', title='Select your app folder')
    path_entry.insert(0, dirc)
    path_entry = dirc
    return dirc
var_nom = StringVar()
nom = Entry(ibm_config,bg="white",textvariable=var_nom)
a=var_nom.get()
print (a)
var_pwd = StringVar()
pwd = Entry(ibm_config, show="*",bg="white",textvariable=var_pwd)
var_pwd_sys=StringVar()
pwd_sys=Entry(ibm_config,show='*',bg="white",textvariable=var_pwd_sys)

############################################## nom egale email  utilisateur object
                ############################################## label dev
nom_label = Label(ibm_config, text="email", font='bold')
pwd_label = Label(ibm_config, text="pwd", font='bold')
pwd_sys_label = Label(ibm_config, text='pwd_sys', font='bold')
note = Label(ibm_config,text='root pwd pour install package ',fg='red')
path_label = Label(ibm_config,text="path",font='bold')
                ############################################## app
path_entry = Entry(ibm_config,bg="white",text='')
nom_app_label= Label(ibm_config,text="app name",font='bold')
nom_app_entry = Entry(ibm_config, bg="white" )
browse =Button(ibm_config,text="directory",command=lambda :repertoire(path_entry))
get_inf=Button (ibm_config,text="done",command=lambda :collect(a,var_pwd,var_pwd_sys))

nom.grid(row=0,column=1)
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
get_inf.grid(row=5,column=2)
nom_app_label.grid(row=5,column=0)
nom_app_entry.grid(row=5,column=1)
ibm_config.mainloop()
print (var_nom,var_pwd_sys,var_pwd)
"""