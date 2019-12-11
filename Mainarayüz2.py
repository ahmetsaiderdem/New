# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.arayuz2 = QtWidgets.QWidget(MainWindow)
        self.arayuz2.setObjectName("arayuz2")
        self.groupBox = QtWidgets.QGroupBox(self.arayuz2)
        self.groupBox.setGeometry(QtCore.QRect(59, 39, 421, 221))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(30, 20, 361, 141))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_kullanici1 = QtWidgets.QLabel(self.widget)
        self.lbl_kullanici1.setObjectName("lbl_kullanici1")
        self.gridLayout.addWidget(self.lbl_kullanici1, 0, 0, 1, 1)
        self.txt_kullanici1 = QtWidgets.QLineEdit(self.widget)
        self.txt_kullanici1.setObjectName("txt_kullanici1")
        self.gridLayout.addWidget(self.txt_kullanici1, 0, 1, 1, 1)
        self.lbl_sifre1 = QtWidgets.QLabel(self.widget)
        self.lbl_sifre1.setObjectName("lbl_sifre1")
        self.gridLayout.addWidget(self.lbl_sifre1, 1, 0, 1, 1)
        self.txt_sifre1 = QtWidgets.QLineEdit(self.widget)
        self.txt_sifre1.setObjectName("txt_sifre1")
        self.gridLayout.addWidget(self.txt_sifre1, 1, 1, 1, 1)
        self.btn_kayit1 = QtWidgets.QPushButton(self.widget)
        self.btn_kayit1.setObjectName("btn_kayit1")
        self.gridLayout.addWidget(self.btn_kayit1, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.arayuz2)
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
        self.groupBox.setTitle(_translate("MainWindow", "Kayıt Ekranı"))
        self.lbl_kullanici1.setText(_translate("MainWindow", "Kullanıcı Adı:"))
        self.lbl_sifre1.setText(_translate("MainWindow", "Şifre:"))
        self.btn_kayit1.setText(_translate("MainWindow", "Kayıt Ol"))
