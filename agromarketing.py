from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MyWebBrowser(QMainWindow):

    def __init__(self,*args,**kwargs):
        super(MyWebBrowser,self).__init__(*args,**kwargs)

        self.window = QWidget()
        self.window.setWindowTitle("Agromarket")
        
        self.window.setGeometry(0,0,1980,1400)

        self.layout=QVBoxLayout()
        self.horizontal =QHBoxLayout()

        self.browser= QWebEngineView()

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://localhost/agromarketing/index.php"))


        self.window.setLayout(self.layout)
        self.window.show()

app= QApplication([])
window = MyWebBrowser()
app.exec_()