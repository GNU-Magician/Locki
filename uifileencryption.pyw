# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileencryption.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import *
import uifiledecryption
import uibasicrypto2
import uibasicdecrypto2
import uiauth
import uifileencryption
import uiadvancedcrypto2
import uiadvanceddecrypto2
import pyAesCrypt
import misc
import os
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

        if number == 0:
            self.setupUi(self.window, 0)
            self.window.show()
            MainWindow.close()

        if number == 1:
            self.setupUi(self.window, 1)
            self.window.show()
            MainWindow.close()

        if number == 2:
            self.setupUi(self.window, 2)
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
        obj = uiadvancedcrypto.Ui_MainWindow()
        if number == 0:
            obj.setupUi(self.window, 0)
            self.window.show()
            MainWindow.close()

        if number == 1:
            obj.setupUi(self.window, 1)
            self.window.show()
            MainWindow.close()     

        if number == 2:
            obj = uiadvanceddecrypto.Ui_MainWindow()
            obj.setupUi(self.window, 0)
            self.window.show()
            MainWindow.close()    
        if number == 3:
            obj = uiadvanceddecrypto.Ui_MainWindow()
            obj.setupUi(self.window, 1)
            self.window.show()
            MainWindow.close()
    def openDecrypt(self, MainWindow):
        self.window = QtWidgets.QMainWindow()
        obj = uifiledecryption.Ui_MainWindow()
        obj.setupUi(self.window, 0)
        MainWindow.close()
        self.window.show()

    def AEStab(self):
        self.stackedWidget.setCurrentIndex(0)
        self.rsaBtn_2.setStyleSheet("background: #0cf6ff; color: rgb(8, 16, 81); font-family: verdana; font-weight: 500;")
        self.keyPairBtn.setStyleSheet("background:rgb(59, 63, 140); color: white; font-family: verdana; font-weight: 500;")
        self.rsaBtn.setStyleSheet("background:rgb(59, 63, 140); color: white; font-family: verdana; font-weight: 500;")
    
    def RSAtab(self):
        self.stackedWidget.setCurrentIndex(2)
        self.rsaBtn.setStyleSheet("background: #0cf6ff; color: rgb(8, 16, 81); font-family: verdana; font-weight: 500;")
        self.keyPairBtn.setStyleSheet("background:rgb(59, 63, 140); color: white; font-family: verdana; font-weight: 500;")
        self.rsaBtn_2.setStyleSheet("background:rgb(59, 63, 140); color: white; font-family: verdana; font-weight: 500;")
    
    def keytab(self):
        self.stackedWidget.setCurrentIndex(1)
        self.keyPairBtn.setStyleSheet("background: #0cf6ff; color: rgb(8, 16, 81); font-family: verdana; font-weight: 500;")
        self.rsaBtn.setStyleSheet("background:rgb(59, 63, 140); color: white; font-family: verdana; font-weight: 500;")
        self.rsaBtn_2.setStyleSheet("background:rgb(59, 63, 140); color: white; font-family: verdana; font-weight: 500;")

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

    def rsaFindFile(self):
        self.filenames = QFileDialog.getOpenFileName(caption='Escolha o arquivo a ser encriptado', 
   directory='c:\\',filter="Qualquer arquivo (*)")
        self.filenames = self.filenames[0].replace("/", "\\")
        self.fileLabelRSA.setText(os.path.basename(self.filenames))



    def rsaFindKey(self):
        self.filename = QFileDialog.getOpenFileName(caption='Escolha a chave pública', 
   directory='c:\\',filter="Chave pública (*.pem)")
        self.filename = self.filename[0].replace("/", "\\")
        self.keyLabelRSA.setText(os.path.basename(self.filename))

    def rsaEncrypt(self):
        try:
            result = misc.encryptRSA(self.filenames, self.filename)
        except AttributeError:
            result = 2


        dialog = QtWidgets.QDialog()
        layout2 = QtWidgets.QHBoxLayout(dialog)
        layout = QtWidgets.QVBoxLayout()
        layout2.addLayout(layout)

        if result:
            label = QtWidgets.QLabel("Arquivo criptografado com sucesso.")
        if result == 2:
            label = QtWidgets.QLabel("Escolha um arquivo pra ser criptografado.")
        self.btndialog = QtWidgets.QPushButton("Ok")
        layout.addWidget(label)
        layout.addWidget(self.btndialog)
        dialog.setGeometry(550, 300, 170, 100)
        self.btndialog.clicked.connect(dialog.close) 
        dialog.setWindowTitle("Locki")
        dialog.exec_()         

    def fileSearch(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode(QtWidgets.QFileDialog.AnyFile)
        filenames = []

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            self.filename = ""
            self.filename = self.filename.join(filenames)
            print(self.filename)
            self.fileNameLabel.setText(os.path.basename(self.filename))

    def fileEncrypt(self):
        text = self.passwordText.toPlainText()
        try:
            result = misc.file_enc(self.filename, text)
        except AttributeError:
            result = 2
        
        dialog = QtWidgets.QDialog()
        layout2 = QtWidgets.QHBoxLayout(dialog)
        layout = QtWidgets.QVBoxLayout()
        layout2.addLayout(layout)

        if result:
            label = QtWidgets.QLabel("Arquivo criptografado com sucesso.")
        if result == 2:
            label = QtWidgets.QLabel("Escolha um arquivo para ser criptografado.")
        self.btndialog = QtWidgets.QPushButton("Ok")
        layout.addWidget(label)
        layout.addWidget(self.btndialog)
        dialog.setGeometry(550, 300, 170, 100)
        self.btndialog.clicked.connect(dialog.close) 
        dialog.setWindowTitle("Locki")
        dialog.exec_()

    def setupUi(self, MainWindow, number):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 512)
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
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(30, 50, 141, 51))
        self.pushButton.setStyleSheet("background:rgb(59, 63, 140);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.openDecrypt(MainWindow))

        self.keyPairBtn = QtWidgets.QPushButton(self.widget)
        self.keyPairBtn.setGeometry(QtCore.QRect(40, 300, 131, 41))
        self.keyPairBtn.setStyleSheet("background:rgb(59, 63, 140);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.keyPairBtn.setObjectName("keyPairBtn")
        self.keyPairBtn.clicked.connect(self.keytab)

        self.rsaBtn = QtWidgets.QPushButton(self.widget)
        self.rsaBtn.setGeometry(QtCore.QRect(40, 360, 131, 41))
        self.rsaBtn.setStyleSheet("background:rgb(59, 63, 140);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.rsaBtn.setObjectName("rsaBtn")
        self.rsaBtn.clicked.connect(self.RSAtab)


        self.rsaBtn_2 = QtWidgets.QPushButton(self.widget)
        self.rsaBtn_2.setGeometry(QtCore.QRect(40, 230, 131, 41))
        self.rsaBtn_2.setStyleSheet("background:rgb(59, 63, 140);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.rsaBtn_2.setObjectName("rsaBtn_2")
        self.rsaBtn_2.clicked.connect(self.AEStab)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(220, -10, 331, 521))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.pagePunc = QtWidgets.QWidget()
        self.pagePunc.setObjectName("pagePunc")
        self.label_2 = QtWidgets.QLabel(self.pagePunc)
        self.label_2.setGeometry(QtCore.QRect(20, 260, 211, 20))
        self.label_2.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_2.setObjectName("label_2")
        self.decFileSearchBtn = QtWidgets.QPushButton(self.pagePunc)
        self.decFileSearchBtn.setGeometry(QtCore.QRect(20, 220, 91, 23))
        self.decFileSearchBtn.setStyleSheet("background-color: rgb(8, 16, 81);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.decFileSearchBtn.setObjectName("decFileSearchBtn")
        self.decFileSearchBtn.clicked.connect(self.fileSearch)

        self.label = QtWidgets.QLabel(self.pagePunc)
        self.label.setGeometry(QtCore.QRect(20, 130, 291, 71))
        self.label.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label.setObjectName("label")
        self.passwordText = QtWidgets.QTextEdit(self.pagePunc)
        self.passwordText.setGeometry(QtCore.QRect(20, 290, 251, 21))
        self.passwordText.setStyleSheet("background: white;")
        self.passwordText.setObjectName("passwordText")
        self.label_6 = QtWidgets.QLabel(self.pagePunc)
        self.label_6.setGeometry(QtCore.QRect(140, 90, 31, 21))
        self.label_6.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.pagePunc)
        self.label_7.setGeometry(QtCore.QRect(120, 220, 61, 20))
        self.label_7.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_7.setObjectName("label_7")
        self.fileNameLabel = QtWidgets.QLabel(self.pagePunc)
        self.fileNameLabel.setGeometry(QtCore.QRect(190, 220, 131, 21))
        self.fileNameLabel.setStyleSheet("color:rgb(0, 0, 127);\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.fileNameLabel.setText("")
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.decSendBtn = QtWidgets.QPushButton(self.pagePunc)
        self.decSendBtn.setGeometry(QtCore.QRect(50, 330, 181, 23))
        self.decSendBtn.setStyleSheet("background-color: rgb(8, 16, 81);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.decSendBtn.setObjectName("decSendBtn")
        self.decSendBtn.clicked.connect(self.fileEncrypt)

        self.stackedWidget.addWidget(self.pagePunc)
        self.pageCeasar = QtWidgets.QWidget()
        self.pageCeasar.setObjectName("pageCeasar")
        self.label_13 = QtWidgets.QLabel(self.pageCeasar)
        self.label_13.setGeometry(QtCore.QRect(80, 140, 151, 21))
        self.label_13.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_13.setObjectName("label_13")
        self.label_12 = QtWidgets.QLabel(self.pageCeasar)
        self.label_12.setGeometry(QtCore.QRect(30, 290, 151, 21))
        self.label_12.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_12.setObjectName("label_12")
        self.createKeyPairBtn = QtWidgets.QPushButton(self.pageCeasar)
        self.createKeyPairBtn.setGeometry(QtCore.QRect(190, 290, 101, 21))
        self.createKeyPairBtn.setStyleSheet("background-color: rgb(8, 16, 81);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.createKeyPairBtn.setObjectName("createKeyPairBtn")
        self.createKeyPairBtn.clicked.connect(self.createKeys)

        self.label_15 = QtWidgets.QLabel(self.pageCeasar)
        self.label_15.setGeometry(QtCore.QRect(30, 200, 271, 61))
        self.label_15.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_15.setObjectName("label_15")
        self.stackedWidget.addWidget(self.pageCeasar)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.keyLabelRSA = QtWidgets.QLabel(self.page)
        self.keyLabelRSA.setGeometry(QtCore.QRect(200, 280, 121, 20))
        self.keyLabelRSA.setStyleSheet("color: rgb(0, 0, 255);\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.keyLabelRSA.setText("")
        self.keyLabelRSA.setObjectName("keyLabelRSA")
        self.RSAsendbtn = QtWidgets.QPushButton(self.page)
        self.RSAsendbtn.setGeometry(QtCore.QRect(30, 310, 251, 23))
        self.RSAsendbtn.setStyleSheet("background-color: rgb(8, 16, 81);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.RSAsendbtn.setObjectName("RSAsendbtn")
        self.RSAsendbtn.clicked.connect(self.rsaEncrypt)
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(30, 140, 251, 21))
        self.label_9.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_9.setObjectName("label_9")
        self.searchKeyBtnRSA = QtWidgets.QPushButton(self.page)
        self.searchKeyBtnRSA.setGeometry(QtCore.QRect(30, 280, 101, 21))
        self.searchKeyBtnRSA.setStyleSheet("background-color: rgb(8, 16, 81);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.searchKeyBtnRSA.setObjectName("searchKeyBtnRSA")
        self.searchKeyBtnRSA.clicked.connect(self.rsaFindKey)


        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(140, 280, 51, 20))
        self.label_11.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(130, 80, 41, 21))
        self.label_10.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_10.setObjectName("label_10")
        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setGeometry(QtCore.QRect(30, 240, 241, 31))
        self.label_14.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_14.setObjectName("label_14")
        self.searchFileBtnRSA = QtWidgets.QPushButton(self.page)
        self.searchFileBtnRSA.setGeometry(QtCore.QRect(30, 170, 251, 21))
        self.searchFileBtnRSA.setStyleSheet("background-color: rgb(8, 16, 81);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.searchFileBtnRSA.setObjectName("searchFileBtnRSA")
        self.searchFileBtnRSA.clicked.connect(self.rsaFindFile)

        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setGeometry(QtCore.QRect(30, 200, 71, 20))
        self.label_16.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_16.setObjectName("label_16")
        self.fileLabelRSA = QtWidgets.QLabel(self.page)
        self.fileLabelRSA.setGeometry(QtCore.QRect(110, 200, 201, 20))
        self.fileLabelRSA.setStyleSheet("color: rgb(0, 0, 255);\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.fileLabelRSA.setText("")
        self.fileLabelRSA.setObjectName("fileLabelRSA")
        self.stackedWidget.addWidget(self.page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 683, 21))
        self.menubar.setObjectName("menubar")
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

        if number == 0:
            self.stackedWidget.setCurrentIndex(0)
        if number == 1: 
            self.stackedWidget.setCurrentIndex(1)
        if number == 2:
            self.stackedWidget.setCurrentIndex(2)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Locki"))
        self.pushButton.setText(_translate("MainWindow", "Descriptografar"))
        self.keyPairBtn.setText(_translate("MainWindow", "Criar Par de\n"
"Chaves"))
        self.rsaBtn.setText(_translate("MainWindow", "RSA"))
        self.rsaBtn_2.setText(_translate("MainWindow", "AES"))
        self.label_2.setText(_translate("MainWindow", "Digite sua senha (se tiver)"))
        self.decFileSearchBtn.setText(_translate("MainWindow", "Procurar..."))
        self.label.setText(_translate("MainWindow", "Escolha o arquivo que será cifrado,\n"
"e digite a senha para poder acessá-lo\n"
"(não precisa preencher se não quizer\n"
"senha)"))
        self.label_6.setText(_translate("MainWindow", "AES"))
        self.label_7.setText(_translate("MainWindow", "Arquivo:"))
        self.decSendBtn.setText(_translate("MainWindow", "Decriptar"))
        self.label_13.setText(_translate("MainWindow", "Criar Par de Chaves"))
        self.label_12.setText(_translate("MainWindow", "Criar par de chaves:"))
        self.createKeyPairBtn.setText(_translate("MainWindow", "Criar.."))
        self.label_15.setText(_translate("MainWindow", "Para criar um par de chaves (RSA), \n"
"simplesmente escolha o lugar onde \n"
"salvar as duas"))
        self.RSAsendbtn.setText(_translate("MainWindow", "Enviar"))
        self.label_9.setText(_translate("MainWindow", "Escolha o arquivo pra ser cifrado"))
        self.searchKeyBtnRSA.setText(_translate("MainWindow", "Procurar..."))
        self.label_11.setText(_translate("MainWindow", "Chave:"))
        self.label_10.setText(_translate("MainWindow", "RSA"))
        self.label_14.setText(_translate("MainWindow", "Escolha abaixo a chave pública\n"
"e envie tudo"))
        self.searchFileBtnRSA.setText(_translate("MainWindow", "Procurar..."))
        self.label_16.setText(_translate("MainWindow", "Arquivo:"))
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

