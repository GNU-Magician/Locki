# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basicdecrypto.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import uibasicrypto2
import basiccrypto
import string

import uiauth

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
            self.setupUi(self.window, 1)
            self.window.show()
            MainWindow.close()          
        if number == 3:
            self.setupUi(self.window, 0)
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
    def ceasarTab(self):
        self.stackedWidget.setCurrentIndex(1)
        self.pushButton_2.setStyleSheet("background-color: rgb(8, 16, 81); color: white; font-family: verdana; font-weight: 500;")
        self.pushButton_3.setStyleSheet("background:#29B6F6; color: white; font-family: verdana; font-weight: 500;")

    def puncTab(self):
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_3.setStyleSheet("background-color: rgb(8, 16, 81); color: white; font-family: verdana; font-weight: 500;")
        self.pushButton_2.setStyleSheet("background:#29B6F6; color: white; font-family: verdana; font-weight: 500;")

    def openEncrypt(self, MainWindow):
        obj = uibasicrypto2.Ui_MainWindow()
        self.window = QtWidgets.QMainWindow()
        obj.setupUi(self.window, 0)
        MainWindow.close()
        self.window.show()

    def ceasarDecrypt(self):
        text = self.plainCeasar.toPlainText()
        self.cipherCeasar.setPlainText(basiccrypto.ceasar_cipher_dec(text.lower()))

    def puncDecrypt(self):
        text = self.plainPunc.toPlainText()
        self.cipherPunc.setPlainText(basiccrypto.punc_cipher_dec(text))



    def setupUi(self, MainWindow, number):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 512)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background:#29B6F6;")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 211, 541))
        self.widget.setStyleSheet("background-color:#0091EA;")
        self.widget.setObjectName("widget")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(200, -180, 20, 721))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(30, 40, 151, 41))
        self.pushButton.setStyleSheet("background:#29B6F6;\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.openEncrypt(MainWindow))

        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 230, 131, 51))
        self.pushButton_2.setStyleSheet("background:#29B6F6;\n"
"\n"
"color: white;\n"
"\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.ceasarTab)

        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 340, 131, 51))
        self.pushButton_3.setStyleSheet("background:#29B6F6;\n"
"\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.puncTab)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(220, -10, 301, 521))
        self.stackedWidget.setObjectName("stackedWidget")
        self.pagePunc = QtWidgets.QWidget()
        self.pagePunc.setObjectName("pagePunc")
        self.label_2 = QtWidgets.QLabel(self.pagePunc)
        self.label_2.setGeometry(QtCore.QRect(20, 280, 161, 20))
        self.label_2.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_2.setObjectName("label_2")
        self.puncBtn = QtWidgets.QPushButton(self.pagePunc)
        self.puncBtn.setGeometry(QtCore.QRect(20, 230, 101, 23))
        self.puncBtn.setStyleSheet("background-color:#0091EA;\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.puncBtn.setObjectName("puncBtn")
        self.puncBtn.clicked.connect(self.puncDecrypt)

        self.label = QtWidgets.QLabel(self.pagePunc)
        self.label.setGeometry(QtCore.QRect(10, 60, 301, 21))
        self.label.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label.setObjectName("label")
        self.plainPunc = QtWidgets.QTextEdit(self.pagePunc)
        self.plainPunc.setGeometry(QtCore.QRect(20, 90, 271, 131))
        self.plainPunc.setStyleSheet("background: white;")
        self.plainPunc.setObjectName("plainPunc")
        self.cipherPunc = QtWidgets.QTextEdit(self.pagePunc)
        self.cipherPunc.setGeometry(QtCore.QRect(20, 310, 271, 141))
        self.cipherPunc.setStyleSheet("background: white;")
        self.cipherPunc.setObjectName("cipherPunc")
        self.label_6 = QtWidgets.QLabel(self.pagePunc)
        self.label_6.setGeometry(QtCore.QRect(110, 20, 91, 21))
        self.label_6.setStyleSheet("color:white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.pagePunc)
        self.pageCeasar = QtWidgets.QWidget()
        self.pageCeasar.setObjectName("pageCeasar")
        self.label_4 = QtWidgets.QLabel(self.pageCeasar)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 301, 21))
        self.label_4.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_4.setObjectName("label_4")
        self.plainCeasar = QtWidgets.QTextEdit(self.pageCeasar)
        self.plainCeasar.setGeometry(QtCore.QRect(20, 90, 271, 131))
        self.plainCeasar.setStyleSheet("background: white;")
        self.plainCeasar.setObjectName("plainCeasar")
        self.ceasarBtn = QtWidgets.QPushButton(self.pageCeasar)
        self.ceasarBtn.setGeometry(QtCore.QRect(20, 230, 101, 23))
        self.ceasarBtn.setStyleSheet("background-color:#0091EA;\n"
"\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.ceasarBtn.setObjectName("ceasarBtn")
        self.ceasarBtn.clicked.connect(self.ceasarDecrypt)

        self.label_3 = QtWidgets.QLabel(self.pageCeasar)
        self.label_3.setGeometry(QtCore.QRect(20, 280, 161, 20))
        self.label_3.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_3.setObjectName("label_3")
        self.cipherCeasar = QtWidgets.QTextEdit(self.pageCeasar)
        self.cipherCeasar.setGeometry(QtCore.QRect(20, 310, 271, 141))
        self.cipherCeasar.setStyleSheet("background: white;")
        self.cipherCeasar.setObjectName("cipherCeasar")
        self.label_5 = QtWidgets.QLabel(self.pageCeasar)
        self.label_5.setGeometry(QtCore.QRect(100, 20, 111, 21))
        self.label_5.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.pageCeasar)
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

        self.retranslateUi(MainWindow)
        if number == 0:
            self.stackedWidget.setCurrentIndex(0)
        if number == 1: 
            self.stackedWidget.setCurrentIndex(1)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Locki"))
        self.pushButton.setText(_translate("MainWindow", "Criptografar"))
        self.pushButton_2.setText(_translate("MainWindow", "Cifra de César"))
        self.pushButton_3.setText(_translate("MainWindow", "Pontuação"))
        self.label_2.setText(_translate("MainWindow", "O resultado é:"))
        self.puncBtn.setText(_translate("MainWindow", "Enviar"))
        self.label.setText(_translate("MainWindow", "Digite embaixo o conteúdo a ser cifrado"))
        self.label_6.setText(_translate("MainWindow", "Pontuação"))
        self.label_4.setText(_translate("MainWindow", "Digite embaixo o conteúdo a ser cifrado"))
        self.ceasarBtn.setText(_translate("MainWindow", "Enviar"))
        self.label_3.setText(_translate("MainWindow", "O resultado é:"))
        self.label_5.setText(_translate("MainWindow", "Cifra de Cesar"))
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

