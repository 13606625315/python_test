import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    #创建application应用实例
    app = QApplication(sys.argv)
    #创建窗口
    w = QWidget()
    #设置宽高
    w.resize(300,150)
    #移动窗口
    w.move(300,300)
    #设置标题
    w.setWindowTitle("陈韬好")
    w.show()
    
    #进入程序主循环,并通过exit（）确保主循环安全结束
    sys.exit(app.exec_())

