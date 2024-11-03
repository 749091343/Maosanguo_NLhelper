# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HelperMainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 567)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/nighter_icon2_256x256.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_simu = QtWidgets.QLabel(self.centralwidget)
        self.label_simu.setObjectName("label_simu")
        self.gridLayout.addWidget(self.label_simu, 0, 0, 1, 1)
        self.pushButton_readme = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_readme.setObjectName("pushButton_readme")
        self.gridLayout.addWidget(self.pushButton_readme, 1, 1, 1, 1)
        self.lineEdit_simu = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_simu.setObjectName("lineEdit_simu")
        self.gridLayout.addWidget(self.lineEdit_simu, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_apply = QtWidgets.QLabel(self.centralwidget)
        self.label_apply.setObjectName("label_apply")
        self.verticalLayout_3.addWidget(self.label_apply)
        self.listWidget_apply = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_apply.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget_apply.setObjectName("listWidget_apply")
        self.verticalLayout_3.addWidget(self.listWidget_apply)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_sche = QtWidgets.QLabel(self.centralwidget)
        self.label_sche.setObjectName("label_sche")
        self.verticalLayout.addWidget(self.label_sche)
        self.listWidget_sche = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_sche.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget_sche.setObjectName("listWidget_sche")
        self.verticalLayout.addWidget(self.listWidget_sche)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_create = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create.setObjectName("pushButton_create")
        self.verticalLayout_2.addWidget(self.pushButton_create)
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.verticalLayout_2.addWidget(self.pushButton_delete)
        self.pushButton_apply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.verticalLayout_2.addWidget(self.pushButton_apply)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_remove = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.verticalLayout_4.addWidget(self.pushButton_remove)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayout_4.addWidget(self.pushButton_start)
        self.pushButton_abort = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_abort.setObjectName("pushButton_abort")
        self.verticalLayout_4.addWidget(self.pushButton_abort)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_current_scheme = QtWidgets.QLabel(self.centralwidget)
        self.label_current_scheme.setObjectName("label_current_scheme")
        self.verticalLayout_5.addWidget(self.label_current_scheme)
        self.textEdit_current_scheme = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_current_scheme.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit_current_scheme.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit_current_scheme.setReadOnly(True)
        self.textEdit_current_scheme.setObjectName("textEdit_current_scheme")
        self.verticalLayout_5.addWidget(self.textEdit_current_scheme)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 5)
        self.verticalLayout_7.setStretch(2, 5)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_log = QtWidgets.QLabel(self.centralwidget)
        self.label_log.setObjectName("label_log")
        self.verticalLayout_6.addWidget(self.label_log)
        self.textEdit_log = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_log.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit_log.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit_log.setReadOnly(True)
        self.textEdit_log.setObjectName("textEdit_log")
        self.verticalLayout_6.addWidget(self.textEdit_log)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1060, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "猫三国夜光助手"))
        self.label_simu.setText(_translate("MainWindow", "模拟器窗口名称："))
        self.pushButton_readme.setText(_translate("MainWindow", "使用说明"))
        self.lineEdit_simu.setText(_translate("MainWindow", "MuMu模拟器12"))
        self.label_apply.setText(_translate("MainWindow", "应用列表："))
        self.label_sche.setText(_translate("MainWindow", "方案列表："))
        self.pushButton_create.setText(_translate("MainWindow", "新建方案"))
        self.pushButton_delete.setText(_translate("MainWindow", "删除方案"))
        self.pushButton_apply.setText(_translate("MainWindow", "应用方案"))
        self.pushButton_remove.setText(_translate("MainWindow", "移除方案"))
        self.pushButton_start.setText(_translate("MainWindow", "启动脚本"))
        self.pushButton_abort.setText(_translate("MainWindow", "终止脚本"))
        self.label_current_scheme.setText(_translate("MainWindow", "当前方案概览："))
        self.label_log.setText(_translate("MainWindow", "工作日志："))
        self.textEdit_log.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ff0000;\">欢迎使用猫三国夜光助手</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">快速使用指南：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1、输入正确的模拟器窗口名称，配置<span style=\" color:#ff0000;\">正确的窗口格式（详见&quot;使用说明&quot;）</span>，并打开游戏至洗兵符界面，点掉游戏自带的提示。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2、新建想要的兵符方案，并应用之。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3、启动脚本，开始洗兵符。</p></body></html>"))