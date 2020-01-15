import sys
from PyQt5.QtWidgets import *#QDialog,QLabel,QVBoxLayout,QMainWindow,QApplication,QHBoxLayout, QPushButton,QWidget,QToolTip
from PyQt5.QtGui import QPixmap,QFont,QPalette
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        label1 =QLabel(self)
        label2 =QLabel(self)
        label3 =QLabel(self)
        label4 =QLabel(self)

        label1.setText("<font color=yellow>this is text label.</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href= '#'>welcome</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('this is label')
        label3.setPixmap(QPixmap("./top1.jpg"))

        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://item.jd.com/12417265.html'>thank you</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('this is url')

        vbow = QVBoxLayout()
        vbow.addWidget(label1)
        vbow.addWidget(label2)
        vbow.addWidget(label3)  
        vbow.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label2.linkActivated.connect(self.linkClicked)

        self.setLayout(vbow)
        self.setWindowTitle("QLabel")



    def linkHovered(self):
        print("鼠标滑过")

    def linkClicked(self):
        print("鼠标点击")

        
class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        nameLabel =QLabel("&Name",self)
        nameLineEdit = QLineEdit(self)
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel("&Password",self)
        passwordLineEdit = QLineEdit(self)
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK= QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel,0,0)
        mainLayout.addWidget(nameLineEdit,0,1,1,2)
        mainLayout.addWidget(passwordLineEdit,1,1,1,2)
        mainLayout.addWidget(passwordLabel,1,0)
        mainLayout.addWidget(btnOK,2,1)
        mainLayout.addWidget(btnCancel,2,2)
if __name__ == '__main__':
    app = QApplication(sys.argv)
  #  app.setWindowIcon()        
 #   main = QLabelDemo()
    main = QLabelBuddy()
    main.show()
    sys.exit(app.exec_())        