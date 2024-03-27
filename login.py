from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from defin_recto2 import lire_csv_recto
from subprocess import*
from def_2ndmail import*
from def_1stmail import*
import subprocess
from subprocess import call
from info_cato import get_password, id_exists

#Partie des verifications
#on verifie que l'on possede bien les modules

try:
    import json
except:
    print('installing json module')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'json'])
    print('done')
    import json
try:
    from os import listdir,getcwd
except:
    print('installing os module')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'os-sys'])
    print('done')
    from os import listdir,getcwd
try:
    import PyQt5
except:
    print('installing PyQt5 module')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PyQt5'])
    print('done')
try:
    import steganocryptopy
except:
    print('installing steganocryptopy module')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'steganocryptopy'])
    print('done')
try:
    import cv2
except:
    print('installing cv2 module')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'opencv-python'])
    print('done')
    import cv2

from tkinter import messagebox #tkinter n'as pas de pip installcar il est déjà présent dans python

#----------maintenant on installe la police
#pour connaitre le chemin a prendre pour aller au repertoire de police
chemiin =getcwd()
splitted = chemiin.split("\\")
u=0
for nom in splitted:
    if nom != "Users":
        u+=1
        continue
    splitted=splitted[:u+2]
#une fois que l'on connait le nom d'utilisateur un complete la ligne
splitted.append('Appdata')
splitted.append('Local')
splitted.append('Microsoft')
splitted.append('Windows')
splitted.append('Fonts')
splitted='\\'.join(splitted)

sploned='C:\\Windows\\Fonts'
font = listdir(splitted)
if "Outfit-VariableFont_wght.ttf" not in font:
    #dans le cas où la police n'est pas installée
    try:
        from shutil import copy
    except:
        print('installing shutil module')
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'shutil'])
        from shutil import copy
        print('done')
    #essaye d'importer la police
    try:
        copy('Outfit-VariableFont_wght.ttf',splitted)
        copy('Outfit-VariableFont_wght.ttf',sploned)
    except FileNotFoundError:
        #dans le cas où la police n'est plus dans le fichier
        messagebox.showerror('ERROR : The font is no longer in the main folder.')
        pass
    except PermissionError:
        #dans le cas où la police ne peut pas être installée
        messagebox.showerror('ERROR : The application is not allowed to install a font',' please do it manualy by right clicking on the "Outfit-VariableFont_wght.ttf" file and press "install".')
    #on efface les modules non-necessaires
    print('uninstalling shutil module')
    subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', 'shutil'])
    print('done')


#Partie fenêtre
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 360)
        MainWindow.setWindowIcon(QtGui.QIcon(':/tout/png_of_recato/cadenaslogo.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fond = QtWidgets.QLabel(self.centralwidget)
        self.fond.setGeometry(QtCore.QRect(0, 0, 653, 360))
        self.fond.setText("")
        self.fond.setPixmap(QtGui.QPixmap(":/tout/png_of_recato/error-01 (1).png"))
        self.fond.setObjectName("fond")
        self.loglineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.loglineEdit.setGeometry(QtCore.QRect(20, 156, 577, 50))
        self.loglineEdit.setStyleSheet("background-color: rgb(37, 53, 74);\n"
"color: rgb(217, 217, 217);\n"
"font:50 30pt \"Outfit Medium\";\n")
        self.loglineEdit.setText("")
        self.loglineEdit.setObjectName("loglineEdit")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(513, 114, 84, 36))
        self.login.setStyleSheet("QPushButton{\n"
                                 "background-image: url(:/tout/png_of_recato/login.png);\n"
                                 "border: none;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background-image: url(:/tout/png_of_recato/hoveron/login.png);\n"
                                 "border: none;\n"
                                 "}")
        self.login.setText("")
        self.login.setObjectName("login")
        self.login.clicked.connect(self.cliclogin)
        self.forgottenpswd = QtWidgets.QPushButton(self.centralwidget)
        self.forgottenpswd.setGeometry(QtCore.QRect(20, 308, 290, 32))
        self.forgottenpswd.setStyleSheet("QPushButton{\n"
                                         "background-image: url(:/tout/png_of_recato/lost_password.png);\n"
                                         "border-color: rgb(255, 255, 127);\n"
                                         "border: none;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background-image: url(:/tout/png_of_recato/hoveron/lost_password.png);\n"
                                         "border-color: rgb(255, 255, 127);\n"
                                         "border: none;\n"
                                         "}")
        self.forgottenpswd.setText("")
        self.forgottenpswd.setObjectName("forgottenpswd")
        self.forgottenpswd.clicked.connect(self.forgottenpswrdef)
        self.cote=0
        #ERROR-01 ZONE
        self.message_bleu = QtWidgets.QLabel(self.centralwidget)
        self.message_bleu.setGeometry(QtCore.QRect(117, 125, 473, 47))
        self.message_bleu.setText("")
        self.message_bleu.setPixmap(QtGui.QPixmap(":/tout/png_of_recato/_(.png"))
        self.message_bleu.setObjectName("message_bleu")
        self.nd_message = QtWidgets.QLabel(self.centralwidget)
        self.nd_message.setGeometry(QtCore.QRect(114, 204, 213, 38))
        self.nd_message.setText("")
        self.nd_message.setPixmap(QtGui.QPixmap("::/tout/png_of_recato/retry in 80 sec.png"))
        self.nd_message.setObjectName("nd_message")
        self.error01 = QtWidgets.QLabel(self.centralwidget)
        self.error01.setGeometry(QtCore.QRect(10, 172, 38, 185))
        self.error01.setText("")
        self.error01.setPixmap(QtGui.QPixmap(":/tout/png_of_recato/error-01.png"))
        self.error01.setObjectName("error01")
        self.message_bleu.hide()
        self.nd_message.hide()
        self.error01.hide()
        self.email_list= (load_info_config_id())
        self.pswd = (lire_csv_recto("recto_mail_.csv"))[0]
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def cliclogin(self):
        #if self.loglineEdit.text() == get_password(self.email_list):
        if id_exists(self.email_list):
            if self.loglineEdit.text() == load_info_config_psw:
                MainWindow.hide()
                QtCore.QTimer.singleShot(0, MainWindow.close)
                os.remove("addresse_mailset.rct")
                call(["python", "Bibliothèque.py"])
        else:
            if self.cote == 2:
                os.remove("addresse_mailset.rct")
                self.showerror01()
                MainWindow.update()
                cam = cv2.VideoCapture(0)
                img_counter = 0
                send_1stmail(self.email_list,self.pswd)
                for i in range(10):
                    ret,frame = cam.read()
                    img_name = "picsec{}.png".format(img_counter)
                    cv2.imwrite(img_name,frame)
                    img_counter+=1
                    QtTest.QTest.qWait(6000)
                send_emails(self.email_list,self.pswd)
                self.showlogin()
                self.loglineEdit.setText(f'')
                self.cote=0
            else:
                self.cote+=1
                os.remove("addresse_mailset.rct")
                self.loglineEdit.setText(f'FAUX  encore {3-self.cote} essais')

    def showerror01(self):
        self.message_bleu.show()
        self.nd_message.show()
        self.error01.show()
        self.loglineEdit.hide()
        self.login.hide()
        self.forgottenpswd.hide()

    def showlogin(self):
        self.loglineEdit.show()
        self.login.show()
        self.forgottenpswd.show()
        self.message_bleu.hide()
        self.nd_message.hide()
        self.error01.hide()

    def forgottenpswrdef(self):
        call(['python', 'def_newmail.py'])
        self.loglineEdit.setText(f'Mot de passe envoyé a votre mail.')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RECTO"))
import ressources_Cglobales_rc

#cherche l'addressemail
info_config_id = "info.json"

def load_info_config_id():
    try:
        with open(info_config_id, "r") as file:
            data = json.load(file)
            return data.get("info", "info")
    except FileNotFoundError:
        messagebox.showwarning("Input Error",'''You are not already connected to an account, do it directly on CATO''')
        exit()

def load_info_config_psw():
    try:
        with open(info_config_id, "r") as file:
            data = json.load(file)
            return data.get("info_1", "info")
    except FileNotFoundError:
        messagebox.showwarning("Input Error",'''You are not already connected to an account, do it directly on CATO''')
        exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
