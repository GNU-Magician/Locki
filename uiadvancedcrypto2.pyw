# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advancedcryptocomplete.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

import binascii

import uiadvanceddecrypto2
import advanceddecrypt
import misc

import uibasicrypto2
import uibasicdecrypto2

import uiauth

import uifileencryption
import uifiledecryption

import main


class Ui_MainWindow(object):
    def openMain(self, MainWindow):
        self.window = QtWidgets.QMainWindow()
        obj = main.Ui_MainWindow()
        obj.setupUi(self.window)
        self.window.show()
        MainWindow.close()

    def openFileEncryption(self, MainWindow, number):
        self.window = QtWidgets.QMainWindow()
        obj = uifileencryption.Ui_MainWindow()

        if number == 0:
            obj.setupUi(self.window, 0)
            self.window.show()
            MainWindow.close()

        if number == 1:
            obj.setupUi(self.window, 1)
            self.window.show()
            MainWindow.close()

        if number == 2:
            obj.setupUi(self.window, 2)
            self.window.show()
            MainWindow.close()      

        if number == 3:
            obj = uifiledecryption.Ui_MainWindow()
            obj.setupUi(self.window, 0)
            self.window.show()
            MainWindow.close()

        if number == 4:
            obj = uifiledecryption.Ui_MainWindow()
            obj.setupUi(self.window, 1)
            self.window.show()
            MainWindow.close() 



    def openBasicCrypto(self, MainWindow, number):
        self.window = QtWidgets.QMainWindow()
        obj = uibasicrypto2.Ui_MainWindow()

        if number == 1:
            obj.setupUi(self.window, 1)
            self.window.show()
            MainWindow.close()
        if number == 0:
            obj.setupUi(self.window, 0)
            self.window.show()
            MainWindow.close()
        if number == 2:
            obj = uibasicdecrypto2.Ui_MainWindow()
            obj.setupUi(self.window, 1)
            self.window.show()
            MainWindow.close()          
        if number == 3:
            obj = uibasicdecrypto2.Ui_MainWindow()
            obj.setupUi(self.window, 0)
            self.window.show()
            MainWindow.close()          


    def openAuth(self, MainWindow, number):
        self.window = QtWidgets.QMainWindow()
        obj = uiauth.Ui_MainWindow()

        if number == 0:
            obj.setupUi(self.window, 0)
            self.window.show()
            MainWindow.close()
        if number == 1:
            obj.setupUi(self.window, 1)
            self.window.show()
            MainWindow.close()
        if number == 2:
            obj.setupUi(self.window, 2)
            self.window.show()
            MainWindow.close()

    def openAdvancedCrypto(self, MainWindow, number):
        self.window = QtWidgets.QMainWindow()
        if number == 0:
            self.setupUi(self.window, 0)
            self.window.show()
            MainWindow.close()

        if number == 1:
            self.setupUi(self.window, 1)
            self.window.show()
            MainWindow.close()     

        if number == 2:
            obj = uiadvanceddecrypto2.Ui_MainWindow()
            obj.setupUi(self.window, 0)
            self.window.show()
            MainWindow.close()    
        if number == 3:
            obj = uiadvanceddecrypto2.Ui_MainWindow()
            obj.setupUi(self.window, 1)
            self.window.show()
            MainWindow.close()

    def aesEncrypt(self):
        text = self.plainCeasar.toPlainText()
        obj = advanceddecrypt.enc()
        cipherAndNonce = obj.aes_encrypt(text)
        ciphertext = cipherAndNonce[0]
        nonce = cipherAndNonce[1]
        self.cipherCeasar.setPlainText(binascii.hexlify(ciphertext).decode("utf-8"))
        self.cipherCeasar_2.setPlainText(binascii.hexlify(nonce).decode("utf-8"))


    def salsaEncrypt(self):
        text = self.plainSalsa.toPlainText()
        obj = advanceddecrypt.enc()
        self.cipherSalsa.setPlainText(obj.salsa20_encrypt(text))


    def salsaTab(self):
        self.stackedWidget.setCurrentIndex(0)

    def aesTab(self):
        self.stackedWidget.setCurrentIndex(1)

    def keyPairTab(self):
        self.stackedWidget.setCurrentIndex(3)

    def rsaTab(self):
        self.stackedWidget.setCurrentIndex(2)

    def openDecrypt(self, MainWindow):
        obj = uiadvanceddecrypto2.Ui_MainWindow()
        self.window = QtWidgets.QMainWindow()
        obj.setupUi(self.window, 0)
        MainWindow.close()
        self.window.show()

    def createKeys(self):
        privkey = QFileDialog.getSaveFileName(caption='Salve a chave privada', 
   directory='c:\\',filter="Chave privada (.pem)")
        privkey = "".join(privkey)
        privkey = privkey.replace("Chave privada (.pem)", ".pem")
        misc.keyPair(privkey)

        pubkey = QFileDialog.getSaveFileName(caption='Salve a chave publica', 
   directory='c:\\',filter="Chave publica (.pem)")
        pubkey = "".join(pubkey)
        pubkey = pubkey.replace("Chave publica (.pem)", ".pem")
        misc.readKeyPair(privkey, pubkey)

    def rsaEncrypt(self):
        text = self.plainRSA.toPlainText()
        misc.read
        




    def setupUi(self, MainWindow, number):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(557, 512)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background:rgb(59, 63, 140);")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 211, 541))
        self.widget.setStyleSheet("background-color: rgb(8, 16, 81);")
        self.widget.setObjectName("widget")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(200, -180, 20, 721))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.decPushBtn = QtWidgets.QPushButton(self.widget)
        self.decPushBtn.setGeometry(QtCore.QRect(30, 40, 151, 41))
        self.decPushBtn.setStyleSheet("background:rgb(59, 63, 140);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"\n"
"")
        self.decPushBtn.setObjectName("decPushBtn")
        self.decPushBtn.clicked.connect(lambda: self.openDecrypt(MainWindow))

        self.aesPushBtn = QtWidgets.QPushButton(self.widget)
        self.aesPushBtn.setGeometry(QtCore.QRect(40, 320, 131, 41))
        self.aesPushBtn.setStyleSheet("background:rgb(59, 63, 140);\n"
"color: white;\n"
"\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.aesPushBtn.setObjectName("aesPushBtn")
        self.aesPushBtn.clicked.connect(self.aesTab)

        self.salsaPushBtn = QtWidgets.QPushButton(self.widget)
        self.salsaPushBtn.setGeometry(QtCore.QRect(40, 220, 131, 41))
        self.salsaPushBtn.setStyleSheet("background:rgb(59, 63, 140);\n"
"color: white;\n"
"\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.salsaPushBtn.setObjectName("salsaPushBtn")
        self.salsaPushBtn.clicked.connect(self.salsaTab)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(220, -10, 331, 521))
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageSalsa = QtWidgets.QWidget()
        self.pageSalsa.setObjectName("pageSalsa")
        self.label_2 = QtWidgets.QLabel(self.pageSalsa)
        self.label_2.setGeometry(QtCore.QRect(40, 280, 161, 20))
        self.label_2.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_2.setObjectName("label_2")
        self.salsaBtn = QtWidgets.QPushButton(self.pageSalsa)
        self.salsaBtn.setGeometry(QtCore.QRect(40, 230, 101, 23))
        self.salsaBtn.setStyleSheet("background-color: rgb(8, 16, 81);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.salsaBtn.setObjectName("salsaBtn")
        self.salsaBtn.clicked.connect(self.salsaEncrypt)


        self.label = QtWidgets.QLabel(self.pageSalsa)
        self.label.setGeometry(QtCore.QRect(20, 60, 311, 21))
        self.label.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label.setObjectName("label")
        self.plainSalsa = QtWidgets.QTextEdit(self.pageSalsa)
        self.plainSalsa.setGeometry(QtCore.QRect(40, 90, 251, 131))
        self.plainSalsa.setStyleSheet("background: white;")
        self.plainSalsa.setObjectName("plainSalsa")
        self.cipherSalsa = QtWidgets.QTextEdit(self.pageSalsa)
        self.cipherSalsa.setGeometry(QtCore.QRect(40, 310, 251, 141))
        self.cipherSalsa.setStyleSheet("background: white;")
        self.cipherSalsa.setObjectName("cipherSalsa")
        self.label_6 = QtWidgets.QLabel(self.pageSalsa)
        self.label_6.setGeometry(QtCore.QRect(140, 20, 91, 21))
        self.label_6.setStyleSheet("color:white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.pageSalsa)
        self.pageAES = QtWidgets.QWidget()
        self.pageAES.setObjectName("pageAES")
        self.label_4 = QtWidgets.QLabel(self.pageAES)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 311, 21))
        self.label_4.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_4.setObjectName("label_4")
        self.plainCeasar = QtWidgets.QTextEdit(self.pageAES)
        self.plainCeasar.setGeometry(QtCore.QRect(40, 90, 251, 111))
        self.plainCeasar.setStyleSheet("background: white;")
        self.plainCeasar.setObjectName("plainCeasar")
        self.ceasarBtn = QtWidgets.QPushButton(self.pageAES)
        self.ceasarBtn.setGeometry(QtCore.QRect(40, 210, 101, 23))
        self.ceasarBtn.setStyleSheet("background-color: rgb(8, 16, 81);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.ceasarBtn.setObjectName("ceasarBtn")
        self.ceasarBtn.clicked.connect(self.aesEncrypt)

        self.label_3 = QtWidgets.QLabel(self.pageAES)
        self.label_3.setGeometry(QtCore.QRect(40, 260, 161, 20))
        self.label_3.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_3.setObjectName("label_3")
        self.cipherCeasar = QtWidgets.QTextEdit(self.pageAES)
        self.cipherCeasar.setGeometry(QtCore.QRect(40, 280, 251, 61))
        self.cipherCeasar.setStyleSheet("background: white;")
        self.cipherCeasar.setObjectName("cipherCeasar")
        self.label_5 = QtWidgets.QLabel(self.pageAES)
        self.label_5.setGeometry(QtCore.QRect(140, 20, 41, 21))
        self.label_5.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_5.setObjectName("label_5")
        self.cipherCeasar_2 = QtWidgets.QTextEdit(self.pageAES)
        self.cipherCeasar_2.setGeometry(QtCore.QRect(40, 390, 251, 61))
        self.cipherCeasar_2.setStyleSheet("background: white;")
        self.cipherCeasar_2.setObjectName("cipherCeasar_2")
        self.label_14 = QtWidgets.QLabel(self.pageAES)
        self.label_14.setGeometry(QtCore.QRect(40, 370, 161, 20))
        self.label_14.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_14.setObjectName("label_14")
        self.stackedWidget.addWidget(self.pageAES)
        self.pageRSA = QtWidgets.QWidget()
        self.pageRSA.setObjectName("pageRSA")
        self.label_7 = QtWidgets.QLabel(self.pageRSA)
        self.label_7.setGeometry(QtCore.QRect(140, 20, 41, 21))
        self.label_7.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.pageRSA)
        self.label_8.setGeometry(QtCore.QRect(30, 330, 161, 20))
        self.label_8.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.pageRSA)
        self.label_9.setGeometry(QtCore.QRect(20, 60, 311, 21))
        self.label_9.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_9.setObjectName("label_9")
        self.RSAbtn = QtWidgets.QPushButton(self.pageRSA)
        self.RSAbtn.setGeometry(QtCore.QRect(40, 280, 251, 23))
        self.RSAbtn.setStyleSheet("background-color: rgb(8, 16, 81);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.RSAbtn.setObjectName("RSAbtn")
        self.cipherRSA = QtWidgets.QTextEdit(self.pageRSA)
        self.cipherRSA.setGeometry(QtCore.QRect(30, 360, 261, 121))
        self.cipherRSA.setStyleSheet("background: white;")
        self.cipherRSA.setObjectName("cipherRSA")
        self.plainRSA = QtWidgets.QTextEdit(self.pageRSA)
        self.plainRSA.setGeometry(QtCore.QRect(40, 90, 251, 111))
        self.plainRSA.setStyleSheet("background: white;")
        self.plainRSA.setObjectName("plainRSA")
        self.label_10 = QtWidgets.QLabel(self.pageRSA)
        self.label_10.setGeometry(QtCore.QRect(40, 210, 241, 31))
        self.label_10.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_10.setObjectName("label_10")
        self.searchBtnRSA = QtWidgets.QPushButton(self.pageRSA)
        self.searchBtnRSA.setGeometry(QtCore.QRect(40, 250, 101, 21))
        self.searchBtnRSA.setStyleSheet("background-color: rgb(8, 16, 81);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.searchBtnRSA.setObjectName("searchBtnRSA")
        self.label_11 = QtWidgets.QLabel(self.pageRSA)
        self.label_11.setGeometry(QtCore.QRect(150, 250, 51, 20))
        self.label_11.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_11.setObjectName("label_11")
        self.keyLabelRSA = QtWidgets.QLabel(self.pageRSA)
        self.keyLabelRSA.setGeometry(QtCore.QRect(210, 250, 101, 20))
        self.keyLabelRSA.setStyleSheet("color: rgb(0, 0, 255);\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.keyLabelRSA.setText("")
        self.keyLabelRSA.setObjectName("keyLabelRSA")
        self.errorLabelRSA = QtWidgets.QLabel(self.pageRSA)
        self.errorLabelRSA.setGeometry(QtCore.QRect(-10, 310, 341, 21))
        self.errorLabelRSA.setStyleSheet("color: red;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.errorLabelRSA.setText("")
        self.errorLabelRSA.setObjectName("errorLabelRSA")
        self.stackedWidget.addWidget(self.pageRSA)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.errorLabelKeyPair = QtWidgets.QLabel(self.page)
        self.errorLabelKeyPair.setGeometry(QtCore.QRect(-10, 250, 341, 101))
        self.errorLabelKeyPair.setStyleSheet("color: red;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.errorLabelKeyPair.setText("")
        self.errorLabelKeyPair.setObjectName("errorLabelKeyPair")
        self.label_12 = QtWidgets.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(30, 200, 151, 21))
        self.label_12.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page)
        self.label_13.setGeometry(QtCore.QRect(90, 50, 151, 21))
        self.label_13.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_13.setObjectName("label_13")
        self.label_15 = QtWidgets.QLabel(self.page)
        self.label_15.setGeometry(QtCore.QRect(30, 110, 271, 61))
        self.label_15.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_15.setObjectName("label_15")
        self.createKeyPair = QtWidgets.QPushButton(self.page)
        self.createKeyPair.setGeometry(QtCore.QRect(190, 200, 101, 21))
        self.createKeyPair.setStyleSheet("background-color: rgb(8, 16, 81);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.createKeyPair.setObjectName("createKeyPair")
        self.stackedWidget.addWidget(self.page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 21))
        self.menubar.setObjectName("menubar")
        self.menuVoltar = QtWidgets.QMenu(self.menubar)
        self.menuVoltar.setObjectName("menuVoltar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuCriptografia = QtWidgets.QMenu(self.menubar)
        self.menuCriptografia.setObjectName("menuCriptografia")
        self.menuCriptografia_B_sica = QtWidgets.QMenu(self.menuCriptografia)
        self.menuCriptografia_B_sica.setObjectName("menuCriptografia_B_sica")
        self.menuCriptografia_Avan_ada = QtWidgets.QMenu(self.menuCriptografia)
        self.menuCriptografia_Avan_ada.setObjectName("menuCriptografia_Avan_ada")
        self.menuCriptografia_de_Arquivos = QtWidgets.QMenu(self.menuCriptografia)
        self.menuCriptografia_de_Arquivos.setObjectName("menuCriptografia_de_Arquivos")
        self.menuAutentica_o = QtWidgets.QMenu(self.menubar)
        self.menuAutentica_o.setObjectName("menuAutentica_o")
        self.menuDecripta_o = QtWidgets.QMenu(self.menubar)
        self.menuDecripta_o.setObjectName("menuDecripta_o")
        self.menuCriptografia_B_sica_2 = QtWidgets.QMenu(self.menuDecripta_o)
        self.menuCriptografia_B_sica_2.setObjectName("menuCriptografia_B_sica_2")
        self.menuCriptografia_Avan_ada_2 = QtWidgets.QMenu(self.menuDecripta_o)
        self.menuCriptografia_Avan_ada_2.setObjectName("menuCriptografia_Avan_ada_2")
        self.menuCriptografia_de_Arquivos_2 = QtWidgets.QMenu(self.menuDecripta_o)
        self.menuCriptografia_de_Arquivos_2.setObjectName("menuCriptografia_de_Arquivos_2")
        MainWindow.setMenuBar(self.menubar)
        self.actionTela_Principal = QtWidgets.QAction(MainWindow)
        self.actionTela_Principal.setObjectName("actionTela_Principal")
        self.actionTela_Princpal = QtWidgets.QAction(MainWindow)
        self.actionTela_Princpal.setObjectName("actionTela_Princpal")
        self.actionTela_Princpal.triggered.connect(lambda: self.openMain(MainWindow))

        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionSair.triggered.connect(MainWindow.close)

        self.actionHash_SHA_256 = QtWidgets.QAction(MainWindow)
        self.actionHash_SHA_256.setObjectName("actionHash_SHA_256")
        self.actionHash_SHA_256.triggered.connect(lambda: self.openAuth(MainWindow, 1))

        self.actionAssinatura_SHA_256 = QtWidgets.QAction(MainWindow)
        self.actionAssinatura_SHA_256.setObjectName("actionAssinatura_SHA_256")
        self.actionAssinatura_SHA_256.triggered.connect(lambda: self.openAuth(MainWindow, 0))

        self.actionChecar_Assinatura = QtWidgets.QAction(MainWindow)
        self.actionChecar_Assinatura.setObjectName("actionChecar_Assinatura")
        self.actionChecar_Assinatura.triggered.connect(lambda: self.openAuth(MainWindow, 2))

        self.actionCifra_de_Cesar = QtWidgets.QAction(MainWindow)
        self.actionCifra_de_Cesar.setObjectName("actionCifra_de_Cesar")
        self.actionCifra_de_Cesar.triggered.connect(lambda: self.openBasicCrypto(MainWindow, 0))

        self.actionPontua_o = QtWidgets.QAction(MainWindow)
        self.actionPontua_o.setObjectName("actionPontua_o")
        self.actionPontua_o.triggered.connect(lambda: self.openBasicCrypto(MainWindow, 1))

        self.actionAES = QtWidgets.QAction(MainWindow)
        self.actionAES.setObjectName("actionAES")
        self.actionAES.triggered.connect(lambda: self.openAdvancedCrypto(MainWindow, 0))

        self.actionAES_2 = QtWidgets.QAction(MainWindow)
        self.actionAES_2.setObjectName("actionAES_2")
        self.actionAES_2.triggered.connect(lambda: self.openAdvancedCrypto(MainWindow, 1))

        self.actionAES_3 = QtWidgets.QAction(MainWindow)
        self.actionAES_3.setObjectName("actionAES_3")
        self.actionAES_3.triggered.connect(lambda: self.openFileEncryption(MainWindow, 0)) #fileencryption

        self.actionCriar_Par_de_Chaves_RSA = QtWidgets.QAction(MainWindow)
        self.actionCriar_Par_de_Chaves_RSA.setObjectName("actionCriar_Par_de_Chaves_RSA")
        self.actionCriar_Par_de_Chaves_RSA.triggered.connect(lambda: self.openFileEncryption(MainWindow, 1)) #fileencryption


        self.actionRSA = QtWidgets.QAction(MainWindow)
        self.actionRSA.setObjectName("actionRSA")
        self.actionRSA.triggered.connect(lambda: self.openFileEncryption(MainWindow, 2)) #fileencryption

        self.actionCifra_de_C_sar = QtWidgets.QAction(MainWindow)
        self.actionCifra_de_C_sar.setObjectName("actionCifra_de_C_sar")
        self.actionCifra_de_C_sar.triggered.connect(lambda: self.openBasicCrypto(MainWindow, 2))

        self.actionPontua_o_2 = QtWidgets.QAction(MainWindow)
        self.actionPontua_o_2.setObjectName("actionPontua_o_2")
        self.actionPontua_o_2.triggered.connect(lambda: self.openBasicCrypto(MainWindow, 3))

        self.actionAES_4 = QtWidgets.QAction(MainWindow)
        self.actionAES_4.setObjectName("actionAES_4")
        self.actionAES_4.triggered.connect(lambda: self.openAdvancedCrypto(MainWindow, 2))


        self.actionAES_5 = QtWidgets.QAction(MainWindow)
        self.actionAES_5.setObjectName("actionAES_5")
        self.actionAES_5.triggered.connect(lambda: self.openAdvancedCrypto(MainWindow, 3))

        self.actionAES_6 = QtWidgets.QAction(MainWindow)
        self.actionAES_6.setObjectName("actionAES_6")
        self.actionAES_6.triggered.connect(lambda: self.openFileEncryption(MainWindow, 3))

        self.actionRSA_2 = QtWidgets.QAction(MainWindow)
        self.actionRSA_2.setObjectName("actionRSA_2")
        self.actionRSA_2.triggered.connect(lambda: self.openFileEncryption(MainWindow, 4))

        self.menuMenu.addAction(self.actionTela_Princpal)
        self.menuMenu.addAction(self.actionSair)
        self.menuCriptografia_B_sica.addAction(self.actionCifra_de_Cesar)
        self.menuCriptografia_B_sica.addAction(self.actionPontua_o)
        self.menuCriptografia_Avan_ada.addAction(self.actionAES)
        self.menuCriptografia_Avan_ada.addAction(self.actionAES_2)
        self.menuCriptografia_de_Arquivos.addAction(self.actionAES_3)
        self.menuCriptografia_de_Arquivos.addAction(self.actionCriar_Par_de_Chaves_RSA)
        self.menuCriptografia_de_Arquivos.addAction(self.actionRSA)
        self.menuCriptografia.addAction(self.menuCriptografia_B_sica.menuAction())
        self.menuCriptografia.addAction(self.menuCriptografia_Avan_ada.menuAction())
        self.menuCriptografia.addAction(self.menuCriptografia_de_Arquivos.menuAction())
        self.menuAutentica_o.addAction(self.actionHash_SHA_256)
        self.menuAutentica_o.addAction(self.actionAssinatura_SHA_256)
        self.menuAutentica_o.addAction(self.actionChecar_Assinatura)
        self.menuCriptografia_B_sica_2.addAction(self.actionCifra_de_C_sar)
        self.menuCriptografia_B_sica_2.addAction(self.actionPontua_o_2)
        self.menuCriptografia_Avan_ada_2.addAction(self.actionAES_4)
        self.menuCriptografia_Avan_ada_2.addAction(self.actionAES_5)
        self.menuCriptografia_de_Arquivos_2.addAction(self.actionAES_6)
        self.menuCriptografia_de_Arquivos_2.addAction(self.actionRSA_2)
        self.menuDecripta_o.addAction(self.menuCriptografia_B_sica_2.menuAction())
        self.menuDecripta_o.addAction(self.menuCriptografia_Avan_ada_2.menuAction())
        self.menuDecripta_o.addAction(self.menuCriptografia_de_Arquivos_2.menuAction())
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuCriptografia.menuAction())
        self.menubar.addAction(self.menuDecripta_o.menuAction())
        self.menubar.addAction(self.menuAutentica_o.menuAction())
        MainWindow.setWindowIcon(QtGui.QIcon("./assets/minilogo.png"))


        self.retranslateUi(MainWindow)
        if number == 0:
            self.stackedWidget.setCurrentIndex(0)
        if number == 1: 
            self.stackedWidget.setCurrentIndex(1)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Locki"))
        self.decPushBtn.setText(_translate("MainWindow", "Descriptografar"))
        self.aesPushBtn.setText(_translate("MainWindow", "AES"))
        self.salsaPushBtn.setText(_translate("MainWindow", "Salsa20"))
        self.label_2.setText(_translate("MainWindow", "O resultado é:"))
        self.salsaBtn.setText(_translate("MainWindow", "Enviar"))
        self.label.setText(_translate("MainWindow", "Digite embaixo o conteúdo a ser cifrado"))
        self.label_6.setText(_translate("MainWindow", "Salsa20"))
        self.label_4.setText(_translate("MainWindow", "Digite embaixo o conteúdo a ser cifrado"))
        self.ceasarBtn.setText(_translate("MainWindow", "Enviar"))
        self.label_3.setText(_translate("MainWindow", "O texto cifrado é:"))
        self.label_5.setText(_translate("MainWindow", "AES"))
        self.label_14.setText(_translate("MainWindow", "O \"nó\" é:"))
        self.label_7.setText(_translate("MainWindow", "RSA"))
        self.label_8.setText(_translate("MainWindow", "O resultado é:"))
        self.label_9.setText(_translate("MainWindow", "Digite embaixo o conteúdo a ser cifrado"))
        self.RSAbtn.setText(_translate("MainWindow", "Enviar"))
        self.label_10.setText(_translate("MainWindow", "Escolha abaixo a chave pública\n"
"e envie tudo"))
        self.searchBtnRSA.setText(_translate("MainWindow", "Procurar..."))
        self.label_11.setText(_translate("MainWindow", "Chave:"))
        self.label_12.setText(_translate("MainWindow", "Criar par de chaves:"))
        self.label_13.setText(_translate("MainWindow", "Criar Par de Chaves"))
        self.label_15.setText(_translate("MainWindow", "Para criar um par de chaves (RSA), \n"
"simplesmente escolha o lugar onde \n"
"salvar as duas"))
        self.createKeyPair.setText(_translate("MainWindow", "Criar.."))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuCriptografia.setTitle(_translate("MainWindow", "Encriptação"))
        self.menuCriptografia_B_sica.setTitle(_translate("MainWindow", "Criptografia Básica"))
        self.menuCriptografia_Avan_ada.setTitle(_translate("MainWindow", "Criptografia Avançada"))
        self.menuCriptografia_de_Arquivos.setTitle(_translate("MainWindow", "Criptografia de Arquivos"))
        self.menuAutentica_o.setTitle(_translate("MainWindow", "Autenticação"))
        self.menuDecripta_o.setTitle(_translate("MainWindow", "Decriptação"))
        self.menuCriptografia_B_sica_2.setTitle(_translate("MainWindow", "Criptografia Básica"))
        self.menuCriptografia_Avan_ada_2.setTitle(_translate("MainWindow", "Criptografia Avançada"))
        self.menuCriptografia_de_Arquivos_2.setTitle(_translate("MainWindow", "Criptografia de Arquivos"))
        self.actionTela_Princpal.setText(_translate("MainWindow", "Tela Princpal"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.actionHash_SHA_256.setText(_translate("MainWindow", "Hash (SHA-256)"))
        self.actionAssinatura_SHA_256.setText(_translate("MainWindow", "Assinatura (SHA-256)"))
        self.actionChecar_Assinatura.setText(_translate("MainWindow", "Checar Assinatura"))
        self.actionCifra_de_Cesar.setText(_translate("MainWindow", "Cifra de Cesar"))
        self.actionPontua_o.setText(_translate("MainWindow", "Pontuação"))
        self.actionAES.setText(_translate("MainWindow", "Salsa20"))
        self.actionAES_2.setText(_translate("MainWindow", "AES"))
        self.actionAES_3.setText(_translate("MainWindow", "AES"))
        self.actionCriar_Par_de_Chaves_RSA.setText(_translate("MainWindow", "Criar Par de Chaves (RSA)"))
        self.actionRSA.setText(_translate("MainWindow", "RSA"))
        self.actionCifra_de_C_sar.setText(_translate("MainWindow", "Cifra de César"))
        self.actionPontua_o_2.setText(_translate("MainWindow", "Pontuação"))
        self.actionAES_4.setText(_translate("MainWindow", "Salsa20"))
        self.actionAES_5.setText(_translate("MainWindow", "AES"))
        self.actionAES_6.setText(_translate("MainWindow", "AES"))
        self.actionRSA_2.setText(_translate("MainWindow", "RSA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

