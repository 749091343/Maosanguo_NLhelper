# -*- coding: utf-8 -*-

import sys
from HelperMainMenu import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


if __name__ == '__main__':
    # 创建Qt应用程序实例
    app = QApplication(sys.argv)

    # 创建一个QWidget对象，作为主窗口
    w = HelperMainMenu()
    w.show()

    # 运行Qt应用程序
    sys.exit(app.exec_())
