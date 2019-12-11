import sys
from PyQt5 import QtWidgets
from Mainarayüz1 import QApplication,Ui_MainWindow,QtCore
import Mainarayüz1,Mainarayüz2

class myApp(MainWindow):
    def __init__(self):
        super(myApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_giris.clicked.connect(self,)
        self.ui.btn_kayit.clicked.connect(self,)

        self.ui.txt_kullanici.setText(self)
        self.ui.txt_sifre.setText(self)


    



app = QApplication()
window = myApp()
window.show()
app.exec_()