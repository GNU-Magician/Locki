# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filedecryption.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import fileencryption
import os
import misc

class Ui_MainWindow(object):

    def openEncrypt(self, MainWindow):
        self.window = QtWidgets.QMainWindow()
        obj = fileencryption.Ui_MainWindow()
        obj.setupUi(self.window)
        MainWindow.close()
        self.window.show()

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

    def fileDecrypt(self):
        text = self.passwordText.toPlainText()
        try:
            result = misc.file_dec(self.filename, text)
        except AttributeError:
            result = 3
        dialog = QDialog()
        layout2 = QtWidgets.QHBoxLayout(dialog)
        layout = QtWidgets.QVBoxLayout()
        layout2.addLayout(layout)
           
        if result:
            label = QtWidgets.QLabel("Arquivo restaurado com sucesso.")
        if result == 2:
            label = QtWidgets.QLabel("Senha errada.")
        if result == 3:
            label = QtWidgets.QLabel("Arquivo não encontrado.")

        self.btndialog = QtWidgets.QPushButton("Ok")
        layout.addWidget(label)
        layout.addWidget(self.btndialog)
        dialog.setGeometry(550, 300, 170, 100)
        self.btndialog.clicked.connect(dialog.close) 
        dialog.exec_()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 512)
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
        self.pushButton.setGeometry(QtCore.QRect(30, 210, 141, 51))
        self.pushButton.setStyleSheet("background:#29B6F6;\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.openEncrypt(MainWindow))

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(220, -10, 301, 521))
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
        self.decFileSearchBtn.setStyleSheet("background-color:#0091EA;\n"
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
        self.label_6.setGeometry(QtCore.QRect(60, 90, 201, 21))
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
        self.decSendBtn.setStyleSheet("background-color:#0091EA;\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.decSendBtn.setObjectName("decSendBtn")
        self.decSendBtn.clicked.connect(self.fileDecrypt)


        self.stackedWidget.addWidget(self.pagePunc)
        self.pageCeasar = QtWidgets.QWidget()
        self.pageCeasar.setObjectName("pageCeasar")
        self.label_4 = QtWidgets.QLabel(self.pageCeasar)
        self.label_4.setGeometry(QtCore.QRect(0, 60, 301, 21))
        self.label_4.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_4.setObjectName("label_4")
        self.plainCeasar = QtWidgets.QTextEdit(self.pageCeasar)
        self.plainCeasar.setGeometry(QtCore.QRect(10, 90, 251, 131))
        self.plainCeasar.setStyleSheet("background: white;")
        self.plainCeasar.setObjectName("plainCeasar")
        self.ceasarBtn = QtWidgets.QPushButton(self.pageCeasar)
        self.ceasarBtn.setGeometry(QtCore.QRect(10, 230, 101, 23))
        self.ceasarBtn.setStyleSheet("background-color:rgb(44, 51, 91);\n"
"\n"
"color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;")
        self.ceasarBtn.setObjectName("ceasarBtn")
        self.label_3 = QtWidgets.QLabel(self.pageCeasar)
        self.label_3.setGeometry(QtCore.QRect(0, 280, 161, 20))
        self.label_3.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_3.setObjectName("label_3")
        self.cipherCeasar = QtWidgets.QTextEdit(self.pageCeasar)
        self.cipherCeasar.setGeometry(QtCore.QRect(10, 310, 251, 141))
        self.cipherCeasar.setStyleSheet("background: white;")
        self.cipherCeasar.setObjectName("cipherCeasar")
        self.label_5 = QtWidgets.QLabel(self.pageCeasar)
        self.label_5.setGeometry(QtCore.QRect(80, 20, 221, 21))
        self.label_5.setStyleSheet("color: white;\n"
"font-family: verdana;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.pageCeasar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 21))
        self.menubar.setObjectName("menubar")
        self.menuVoltar = QtWidgets.QMenu(self.menubar)
        self.menuVoltar.setObjectName("menuVoltar")
        MainWindow.setMenuBar(self.menubar)
        self.actionTela_Principal = QtWidgets.QAction(MainWindow)
        self.actionTela_Principal.setObjectName("actionTela_Principal")
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.menuVoltar.addAction(self.actionTela_Principal)
        self.menuVoltar.addAction(self.actionSair)
        self.menubar.addAction(self.menuVoltar.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Criptografar"))
        self.label_2.setText(_translate("MainWindow", "Digite sua senha (se tiver)"))
        self.decFileSearchBtn.setText(_translate("MainWindow", "Procurar..."))
        self.label.setText(_translate("MainWindow", "Escolha o arquivo que será restaurado,\n"
"e digite a senha para poder acessá-lo\n"
"(não precisa preencher se não houver\n"
"senha)"))
        self.label_6.setText(_translate("MainWindow", "Decriptação de Arquivos"))
        self.label_7.setText(_translate("MainWindow", "Arquivo:"))
        self.decSendBtn.setText(_translate("MainWindow", "Decriptar"))
        self.label_4.setText(_translate("MainWindow", "Digite embaixo o conteúdo a ser cifrado"))
        self.ceasarBtn.setText(_translate("MainWindow", "Enviar"))
        self.label_3.setText(_translate("MainWindow", "O resultado é:"))
        self.label_5.setText(_translate("MainWindow", "Cifra de Cesar"))
        self.menuVoltar.setTitle(_translate("MainWindow", "Menu"))
        self.actionTela_Principal.setText(_translate("MainWindow", "Tela Principal"))
        self.actionTela_Principal.setShortcut(_translate("MainWindow", "Ctrl+Shift+Q"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.actionSair.setShortcut(_translate("MainWindow", "Ctrl+Shift+E"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

