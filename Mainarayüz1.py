# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mani1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.arayuz1 = QtWidgets.QWidget(MainWindow)
        self.arayuz1.setObjectName("arayuz1")
        self.groupBox = QtWidgets.QGroupBox(self.arayuz1)
        self.groupBox.setGeometry(QtCore.QRect(120, 40, 341, 201))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(40, 40, 241, 111))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_kullanici = QtWidgets.QLabel(self.widget)
        self.lbl_kullanici.setObjectName("lbl_kullanici")
        self.gridLayout.addWidget(self.lbl_kullanici, 0, 0, 1, 1)
        self.txt_kullanici = QtWidgets.QLineEdit(self.widget)
        self.txt_kullanici.setObjectName("txt_kullanici")
        self.gridLayout.addWidget(self.txt_kullanici, 0, 1, 1, 2)
        self.lbl_sifre = QtWidgets.QLabel(self.widget)
        self.lbl_sifre.setObjectName("lbl_sifre")
        self.gridLayout.addWidget(self.lbl_sifre, 1, 0, 1, 1)
        self.txt_sifre = QtWidgets.QLineEdit(self.widget)
        self.txt_sifre.setObjectName("txt_sifre")
        self.gridLayout.addWidget(self.txt_sifre, 1, 1, 1, 2)
        self.btn_giris = QtWidgets.QPushButton(self.widget)
        self.btn_giris.setObjectName("btn_giris")
        self.gridLayout.addWidget(self.btn_giris, 2, 0, 1, 2)
        self.btn_kayit = QtWidgets.QPushButton(self.widget)
        self.btn_kayit.setObjectName("btn_kayit")
        self.gridLayout.addWidget(self.btn_kayit, 2, 2, 1, 1)
        self.lbl_bilgi = QtWidgets.QLabel(self.groupBox)
        self.lbl_bilgi.setGeometry(QtCore.QRect(20, 170, 261, 16))
        self.lbl_bilgi.setText("")
        self.lbl_bilgi.setObjectName("lbl_bilgi")
        MainWindow.setCentralWidget(self.arayuz1)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Giriş Ekranı"))
        self.lbl_kullanici.setText(_translate("MainWindow", "Kullanıcı Adı: "))
        self.lbl_sifre.setText(_translate("MainWindow", "Şifre: "))
        self.btn_giris.setText(_translate("MainWindow", "Giriş Yap"))
        self.btn_kayit.setText(_translate("MainWindow", "Kayıt Ol"))
