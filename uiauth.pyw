# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basicauthcomplete2.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import misc
import os
import binascii
import uibasicrypto2
import uibasicdecrypto2


import uifileencryption
import uifiledecryption

import uiadvancedcrypto2
import uiadvanceddecrypto2
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

    def openAdvancedCrypto(self, MainWindow, number):
        self.window = QtWidgets.QMainWindow()
        obj = uiadvancedcrypto2.Ui_MainWindow()
        if number == 0:
            obj.setupUi(self.window, 0)
            self.window.show()
            MainWindow.close()

        if number == 1:
            obj.setupUi(self.window, 1)
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

    def sendPublicKey(self):
        text = self.plainCheckSig.toPlainText()
        sig = self.plainCheckSig2.toPlainText()
        try:
            result = misc.versig(message=bytes(text, encoding="utf-8"), signature=sig, file=self.filename)
        except AttributeError:
            result = 3
        except (ValueError, TypeError):
            result = 4
            #label = pick a damn file
        dialog = QtWidgets.QDialog()
        layout2 = QtWidgets.QHBoxLayout(dialog)
        layout = QtWidgets.QVBoxLayout()
        layout2.addLayout(layout)

        if result:
            label = QtWidgets.QLabel("A assinatura é válida.")
        if result == 3:
            label = QtWidgets.QLabel("Preencha todos os campos.")
        if result == 4:
            label = QtWidgets.QLabel("Selecione uma chave pública RSA.")                   
        if not result:
            label = QtWidgets.QLabel("A assinatura não é válida.")

        self.btndialog = QtWidgets.QPushButton("Ok")
        layout.addWidget(label)
        layout.addWidget(self.btndialog)
        dialog.setGeometry(550, 300, 170, 100)
        self.btndialog.clicked.connect(dialog.close) 
        dialog.setWindowTitle("Locki")
        dialog.exec_()


    def findPublicKey(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        filenames = []

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            self.filename = ""
            self.filename = self.filename.join(filenames)
            print(self.filename)
            self.publicKeyFileLabel.setText(os.path.basename(self.filename))
        
    def searchKeySig(self): 
        #make the object self.filenames pass to the sender function
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        filename = []
        self.filenames = ""
        if dlg.exec_():
            filename = dlg.selectedFiles()
            self.filenames = self.filenames.join(filename)
            self.keyFileLabel.setText(os.path.basename(self.filenames))
        #remake a window where you insert the signature, this one is lost


    def sigText(self):
        try:
            text = self.plainSig.toPlainText()
        #send object from browse button here
        #maybe change function name
            result = self.cipherSig.setPlainText(misc.makesig(bytes(text, "utf-8"), self.filenames))
        except AttributeError:
            result = 3
        except (TypeError, ValueError): 
            result = 4


        dialog = QtWidgets.QDialog()
        layout2 = QtWidgets.QHBoxLayout(dialog)
        layout = QtWidgets.QVBoxLayout()
        layout2.addLayout(layout)


        if result == 3:
            label = QtWidgets.QLabel("Preencha todos os campos.")
        if result == 4:
            label = QtWidgets.QLabel("Selecione uma chave publica RSA.")

        self.btndialog = QtWidgets.QPushButton("Ok")
        layout.addWidget(label)
        layout.addWidget(self.btndialog)
        dialog.setGeometry(550, 300, 170, 100)
        self.btndialog.clicked.connect(dialog.close) 
        dialog.setWindowTitle("Locki")
        dialog.exec_()


    def hashText(self):
        text = self.plainHash.toPlainText()
        self.cipherHash.setPlainText(misc.makehash(bytes(text, "utf-8")))

    def authTab(self):
        self.stackedWidget.setCurrentIndex(1)
        self.authPushBtn.setStyleSheet("background: #0cf6ff; color: rgb(8, 16, 81); font-family: verdana; font-weight: 500;")
        self.sigPushBtn.setStyleSheet("background:rgb(59, 63, 140); color: white; font-family: verdana; font-weight: 500;")
        self.checkPushBtn.setStyleSheet("background:rgb(59, 63, 140); color: white; font-family: verdana; font-weight: 500;")

    def sigTab(self):
        self.stackedWidget.setCurrentIndex(0)
        self.sigPushBtn.setStyleSheet("background: #0cf6ff; color: rgb(8, 16, 81); font-family: verdana; font-weight: 500;")
        self.authPushBtn.setStyleSheet("background:rgb(59, 63, 140); color: white; font-family: verdana; font-weight: 500;")
        self.checkPushBtn.setStyleSheet("background:rgb(59, 63, 140); color: white; font-family: verdana; font-weight: 500;")

    def checkSigTab(self):
        self.stackedWidget.setCurrentIndex(2)
        self.checkPushBtn.setStyleSheet("background: #0cf6ff; color: rgb(8, 16, 81); font-family: verdana; font-weight: 500;")
        self.authPushBtn.setStyleSheet("background:rgb(59, 63, 140); color: white; font-family: verdana; font-weight: 500;")
        self.sigPushBtn.setStyleSheet("background:rgb(59, 63, 140); color: white; font-family: verdana; font-weight: 500;")

    def setupUi(self, MainWindow, number):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(558, 539)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background:rgb(59, 63, 140)")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 211, 541))
        self.widget.setStyleSheet("background-color: rgb(8, 16, 81)")
        self.widget.setObjectName("widget")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(200, -180, 20, 721))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.authPushBtn = QtWidgets.QPushButton(self.widget)
        self.authPushBtn.setGeometry(QtCore.QRect(40, 110, 131, 41))
        self.authPushBtn.setStyleSheet("background:rgb(59, 63, 140);\n"
"\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.authPushBtn.setObjectName("authPushBtn")
        self.authPushBtn.clicked.connect(self.authTab)
        self.sigPushBtn = QtWidgets.QPushButton(self.widget)
        self.sigPushBtn.setGeometry(QtCore.QRect(40, 340, 131, 41))
        self.sigPushBtn.setStyleSheet("background:rgb(59, 63, 140);\n"
"\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.sigPushBtn.setObjectName("sigPushBtn")
        self.sigPushBtn.clicked.connect(self.sigTab)

        self.checkPushBtn = QtWidgets.QPushButton(self.widget)
        self.checkPushBtn.setGeometry(QtCore.QRect(40, 400, 131, 41))
        self.checkPushBtn.setStyleSheet("background:rgb(59, 63, 140);\n"
"\n"
"color: white;\n"
"font-family: Verdana;\n"
"font-weight: 500;")
        self.checkPushBtn.setObjectName("checkPushBtn")
        self.checkPushBtn.clicked.connect(self.checkSigTab)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(240, 10, 311, 521))
        self.stackedWidget.setObjectName("stackedWidget")
        self.pagePunc = QtWidgets.QWidget()
        self.pagePunc.setObjectName("pagePunc")
        self.label_2 = QtWidgets.QLabel(self.pagePunc)
        self.label_2.setGeometry(QtCore.QRect(0, 310, 161, 20))
        self.label_2.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_2.setObjectName("label_2")
        self.sigBtn = QtWidgets.QPushButton(self.pagePunc)
        self.sigBtn.setGeometry(QtCore.QRect(0, 250, 281, 23))
        self.sigBtn.setStyleSheet("background-color: rgb(8, 16, 81);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.sigBtn.setObjectName("sigBtn")
        self.sigBtn.clicked.connect(self.sigText)

        self.label = QtWidgets.QLabel(self.pagePunc)
        self.label.setGeometry(QtCore.QRect(0, 60, 301, 21))
        self.label.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label.setObjectName("label")
        self.plainSig = QtWidgets.QTextEdit(self.pagePunc)
        self.plainSig.setGeometry(QtCore.QRect(10, 90, 271, 61))
        self.plainSig.setStyleSheet("background: white;")
        self.plainSig.setObjectName("plainSig")
        self.cipherSig = QtWidgets.QTextEdit(self.pagePunc)
        self.cipherSig.setGeometry(QtCore.QRect(0, 340, 281, 141))
        self.cipherSig.setStyleSheet("background: white;")
        self.cipherSig.setObjectName("cipherSig")
        self.label_6 = QtWidgets.QLabel(self.pagePunc)
        self.label_6.setGeometry(QtCore.QRect(70, 20, 171, 21))
        self.label_6.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.pagePunc)
        self.label_7.setGeometry(QtCore.QRect(0, 170, 301, 31))
        self.label_7.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_7.setObjectName("label_7")

        self.fileSearchBtn = QtWidgets.QPushButton(self.pagePunc)
        self.fileSearchBtn.setGeometry(QtCore.QRect(0, 210, 101, 23))
        self.fileSearchBtn.setStyleSheet("background-color: rgb(8, 16, 81);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.fileSearchBtn.setObjectName("fileSearchBtn")
        self.fileSearchBtn.clicked.connect(self.searchKeySig)


        self.label_8 = QtWidgets.QLabel(self.pagePunc)
        self.label_8.setGeometry(QtCore.QRect(110, 210, 51, 21))
        self.label_8.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_8.setObjectName("label_8")
        self.keyFileLabel = QtWidgets.QLabel(self.pagePunc)
        self.keyFileLabel.setGeometry(QtCore.QRect(170, 210, 101, 21))
        self.keyFileLabel.setStyleSheet("color: rgb(0, 170, 255);\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.keyFileLabel.setText("")
        self.keyFileLabel.setObjectName("keyFileLabel")
        self.errorLabel = QtWidgets.QLabel(self.pagePunc)
        self.errorLabel.setGeometry(QtCore.QRect(0, 280, 311, 31))
        self.errorLabel.setStyleSheet("color: red;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.stackedWidget.addWidget(self.pagePunc)
        self.pageCeasar = QtWidgets.QWidget()
        self.pageCeasar.setObjectName("pageCeasar")
        self.label_4 = QtWidgets.QLabel(self.pageCeasar)
        self.label_4.setGeometry(QtCore.QRect(0, 60, 311, 21))
        self.label_4.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_4.setObjectName("label_4")
        self.plainHash = QtWidgets.QTextEdit(self.pageCeasar)
        self.plainHash.setGeometry(QtCore.QRect(10, 90, 251, 131))
        self.plainHash.setStyleSheet("background: white;")
        self.plainHash.setObjectName("plainHash")



        self.hashBtn = QtWidgets.QPushButton(self.pageCeasar)
        self.hashBtn.setGeometry(QtCore.QRect(10, 230, 101, 23))
        self.hashBtn.setStyleSheet("background-color: rgb(8, 16, 81);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.hashBtn.setObjectName("hashBtn")
        self.hashBtn.clicked.connect(self.hashText)


        self.label_3 = QtWidgets.QLabel(self.pageCeasar)
        self.label_3.setGeometry(QtCore.QRect(0, 280, 161, 20))
        self.label_3.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_3.setObjectName("label_3")
        self.cipherHash = QtWidgets.QTextEdit(self.pageCeasar)
        self.cipherHash.setGeometry(QtCore.QRect(10, 310, 251, 141))
        self.cipherHash.setStyleSheet("background: white;")
        self.cipherHash.setObjectName("cipherHash")
        self.cipherHash.setReadOnly(1)

        self.label_5 = QtWidgets.QLabel(self.pageCeasar)
        self.label_5.setGeometry(QtCore.QRect(60, 20, 171, 21))
        self.label_5.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.pageCeasar)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setGeometry(QtCore.QRect(0, 60, 311, 21))
        self.label_17.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_17.setObjectName("label_17")
        self.plainCheckSig = QtWidgets.QTextEdit(self.page)
        self.plainCheckSig.setGeometry(QtCore.QRect(0, 90, 291, 81))
        self.plainCheckSig.setStyleSheet("background: white;")
        self.plainCheckSig.setObjectName("plainCheckSig")



        self.errorLabel_3 = QtWidgets.QLabel(self.page)
        self.errorLabel_3.setGeometry(QtCore.QRect(0, 400, 311, 31))
        self.errorLabel_3.setStyleSheet("color: red;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.errorLabel_3.setText("")
        self.errorLabel_3.setObjectName("errorLabel_3")
        self.label_18 = QtWidgets.QLabel(self.page)
        self.label_18.setGeometry(QtCore.QRect(50, 20, 221, 21))
        self.label_18.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.page)
        self.label_19.setGeometry(QtCore.QRect(110, 210, 51, 21))
        self.label_19.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_19.setObjectName("label_19")
        self.publicKeyFileLabel = QtWidgets.QLabel(self.page)
        self.publicKeyFileLabel.setGeometry(QtCore.QRect(170, 210, 141, 21))
        self.publicKeyFileLabel.setStyleSheet("color: rgb(0, 170, 255);\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.publicKeyFileLabel.setText("")
        self.publicKeyFileLabel.setObjectName("publicKeyFileLabel")


        self.label_20 = QtWidgets.QLabel(self.page)
        self.label_20.setGeometry(QtCore.QRect(0, 440, 111, 20))
        self.label_20.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_20.setObjectName("label_20")
        self.sigSendBtn = QtWidgets.QPushButton(self.page)
        self.sigSendBtn.setGeometry(QtCore.QRect(0, 370, 291, 23))
        self.sigSendBtn.setStyleSheet("background-color: rgb(8, 16, 81);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.sigSendBtn.setObjectName("sigSendBtn")
        self.sigSendBtn.clicked.connect(self.sendPublicKey)


        self.publicKeySearch = QtWidgets.QPushButton(self.page)
        self.publicKeySearch.setGeometry(QtCore.QRect(0, 210, 101, 23))
        self.publicKeySearch.setStyleSheet("background-color: rgb(8, 16, 81);\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.publicKeySearch.setObjectName("publicKeySearch")
        self.publicKeySearch.clicked.connect(self.findPublicKey)


        self.label_21 = QtWidgets.QLabel(self.page)
        self.label_21.setGeometry(QtCore.QRect(0, 180, 301, 31))
        self.label_21.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_21.setObjectName("label_21")
        self.publicKeyLabel = QtWidgets.QLabel(self.page)
        self.publicKeyLabel.setGeometry(QtCore.QRect(120, 440, 161, 20))
        self.publicKeyLabel.setStyleSheet("color: rgb(0, 255, 0);\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.publicKeyLabel.setText("")
        self.publicKeyLabel.setObjectName("publicKeyLabel")
        self.label_22 = QtWidgets.QLabel(self.page)
        self.label_22.setGeometry(QtCore.QRect(0, 240, 301, 31))
        self.label_22.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_22.setObjectName("label_22")
        self.plainCheckSig2 = QtWidgets.QTextEdit(self.page)
        self.plainCheckSig2.setGeometry(QtCore.QRect(0, 280, 291, 81))
        self.plainCheckSig2.setStyleSheet("background: white;")
        self.plainCheckSig2.setObjectName("plainCheckSig2")
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
        self.stackedWidget.setCurrentIndex(0)

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
        self.authPushBtn.setText(_translate("MainWindow", "Autenticação"))
        self.sigPushBtn.setText(_translate("MainWindow", "Assinatura"))
        self.checkPushBtn.setText(_translate("MainWindow", "Checar \n"
"Assinatura"))
        self.label_2.setText(_translate("MainWindow", "O resultado é:"))
        self.sigBtn.setText(_translate("MainWindow", "Enviar"))
        self.label.setText(_translate("MainWindow", "Digite o conteúdo a para ser assinado"))
        self.label_6.setText(_translate("MainWindow", "Assinatura (SHA256)"))
        self.label_7.setText(_translate("MainWindow", "Escolha a chave privada à assinar,\n"
"e envie tudo"))
        self.fileSearchBtn.setText(_translate("MainWindow", "Procurar.."))
        self.label_8.setText(_translate("MainWindow", "Chave: "))
        self.label_4.setText(_translate("MainWindow", "Digite embaixo o texto a ser autenticado"))
        self.hashBtn.setText(_translate("MainWindow", "Enviar"))
        self.label_3.setText(_translate("MainWindow", "O hash desse texto é: "))
        self.label_5.setText(_translate("MainWindow", "Autenticação (SHA256)"))
        self.label_17.setText(_translate("MainWindow", "Verifique a assinatura do texto abaixo:"))
        self.label_18.setText(_translate("MainWindow", "Checar Assinatura (SHA256)"))
        self.label_19.setText(_translate("MainWindow", "Chave: "))
        self.sigSendBtn.setText(_translate("MainWindow", "Enviar"))
        self.publicKeySearch.setText(_translate("MainWindow", "Procurar.."))
        self.label_21.setText(_translate("MainWindow", "Escolha a chave publica do assinante"))
        self.label_22.setText(_translate("MainWindow", "Digite a assinatura à ser verificada"))
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

