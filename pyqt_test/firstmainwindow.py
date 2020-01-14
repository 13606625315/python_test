import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QHBoxLayout, QPushButton,QWidget

class FirstMainWin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("first!")

        self.resize(500,300)

        self.status =self.statusBar()

        self.status.showMessage("5s",5000)

        self.button = QPushButton('quit')
        self.button.clicked.connect(self.onClickButton)
        layout = QHBoxLayout()
        layout.addWidget(self.button)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    def onClickButton(self):
        app = QApplication.instance()
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
  #  app.setWindowIcon()        
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())