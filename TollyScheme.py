# -*- coding: utf-8 -*-

from TollyScheme_UI import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,QMessageBox
from PyQt5.QtCore import Qt,QObject, pyqtSignal
from PyQt5.QtGui import QIcon
import Schemes
import Utils
import json

class TollyScheme(QMainWindow,Ui_Form):

    #自定义信号：方案创建完成，将方案返回给父窗口的 addSchemes 函数
    signal_SchemeCreatedDone = pyqtSignal(dict)

    def __init__(self,parent=None):
        super(TollyScheme,self).__init__(parent)
        self.setupUi(self)
        self.setupSignal()
        #设置窗体图标
        self.setWindowIcon(QIcon('./icons/nighter_icon2_256x256.ico'))

        self.mainBoxGroup = [
            self.checkBox_main_1,self.checkBox_main_2,self.checkBox_main_3
        ]
        self.subBoxGroup = [
            self.checkBox_sub_1,self.checkBox_sub_2,self.checkBox_sub_3,self.checkBox_sub_4,self.checkBox_sub_5,
            self.checkBox_sub_6,self.checkBox_sub_7,self.checkBox_sub_8,self.checkBox_sub_9
        ]
        self.mustBoxGroup = [
            self.checkBox_must_1,self.checkBox_must_2,self.checkBox_must_3,self.checkBox_must_4,self.checkBox_must_5,
            self.checkBox_must_6,self.checkBox_must_7,self.checkBox_must_8,self.checkBox_must_9,self.checkBox_must_10,
            self.checkBox_must_11,self.checkBox_must_12,self.checkBox_must_13,self.checkBox_must_14,self.checkBox_must_15,
            self.checkBox_must_16,self.checkBox_must_17,self.checkBox_must_18,self.checkBox_must_19,self.checkBox_must_20,
            self.checkBox_must_21,self.checkBox_must_22,self.checkBox_must_23,self.checkBox_must_24,self.checkBox_must_25,
            self.checkBox_must_26,self.checkBox_must_27,self.checkBox_must_28,self.checkBox_must_29,self.checkBox_must_30,
            self.checkBox_must_31,self.checkBox_must_32,self.checkBox_must_33,self.checkBox_must_34,self.checkBox_must_35,
            self.checkBox_must_36,self.checkBox_must_37,self.checkBox_must_38,self.checkBox_must_39,self.checkBox_must_40,
            self.checkBox_must_41,self.checkBox_must_42,self.checkBox_must_43,self.checkBox_must_44,self.checkBox_must_45,
            self.checkBox_must_46,self.checkBox_must_47,self.checkBox_must_48,self.checkBox_must_49,self.checkBox_must_50,
            self.checkBox_must_51,self.checkBox_must_52,self.checkBox_must_53,self.checkBox_must_54,self.checkBox_must_55,
            self.checkBox_must_56,self.checkBox_must_57,self.checkBox_must_58,self.checkBox_must_59,self.checkBox_must_60,
        ]
        self.chooseBoxGroup = [
            self.checkBox_choose_1,self.checkBox_choose_2,self.checkBox_choose_3,self.checkBox_choose_4,self.checkBox_choose_5,
            self.checkBox_choose_6,self.checkBox_choose_7,self.checkBox_choose_8,self.checkBox_choose_9,self.checkBox_choose_10,
            self.checkBox_choose_11,self.checkBox_choose_12,self.checkBox_choose_13,self.checkBox_choose_14,self.checkBox_choose_15,
            self.checkBox_choose_16,self.checkBox_choose_17,self.checkBox_choose_18,self.checkBox_choose_19,self.checkBox_choose_20,
            self.checkBox_choose_21,self.checkBox_choose_22,self.checkBox_choose_23,self.checkBox_choose_24,self.checkBox_choose_25,
            self.checkBox_choose_26,self.checkBox_choose_27,self.checkBox_choose_28,self.checkBox_choose_29,self.checkBox_choose_30,
            self.checkBox_choose_31,self.checkBox_choose_32,self.checkBox_choose_33,self.checkBox_choose_34,self.checkBox_choose_35,
            self.checkBox_choose_36,self.checkBox_choose_37,self.checkBox_choose_38,self.checkBox_choose_39,self.checkBox_choose_40,
            self.checkBox_choose_41,self.checkBox_choose_42,self.checkBox_choose_43,self.checkBox_choose_44,self.checkBox_choose_45,
            self.checkBox_choose_46,self.checkBox_choose_47,self.checkBox_choose_48,self.checkBox_choose_49,self.checkBox_choose_50,
            self.checkBox_choose_51,self.checkBox_choose_52,self.checkBox_choose_53,self.checkBox_choose_54,self.checkBox_choose_55,
            self.checkBox_choose_56,self.checkBox_choose_57,self.checkBox_choose_58,self.checkBox_choose_59,self.checkBox_choose_60,           
        ]
        self.exclBoxGroup = [
            self.checkBox_exclude_1,self.checkBox_exclude_2,self.checkBox_exclude_3,self.checkBox_exclude_4
        ]
        #记录已有的方案名，用于防止方案名重复
        self.currentSchemesName = []

    #设置所有的信号与绑定的槽函数
    def setupSignal(self):
        self.pushButton_cancel.clicked.connect(self.close)
        self.pushButton_save.clicked.connect(self.saveSchemeDetect)

    #根据页面的选择产生一个方案
    def createScheme(self):
        scheme = {'name':self.lineEdit_schemeName.text()}
        scheme['main'] = [index + 1 for index, box in enumerate(self.mainBoxGroup) if box.isChecked()]
        scheme['sub'] = {}
        scheme['sub']['subNum'] = self.spinBox_subproperty.value()
        scheme['sub']['subPros'] = [index + 1 for index, box in enumerate(self.subBoxGroup) if box.isChecked()]
        scheme['must'] = [index + 1 for index, box in enumerate(self.mustBoxGroup) if box.isChecked()]
        scheme['choose'] = {}
        scheme['choose']['chooseNum'] = self.spinBox_choose.value()
        scheme['choose']['chooseSkills'] = [index + 1 for index, box in enumerate(self.chooseBoxGroup) if box.isChecked()]
        #排除一些负面技能
        scheme['excl'] = []
        if self.checkBox_exclude_1.isChecked():
            scheme['excl'] = scheme['excl'] + [3,33]
        if self.checkBox_exclude_2.isChecked():
            scheme['excl'] = scheme['excl'] + [10,40]
        if self.checkBox_exclude_3.isChecked():
            scheme['excl'] = scheme['excl'] + [22,52]
        if self.checkBox_exclude_4.isChecked():
            scheme['excl'] = scheme['excl'] + [9,39]
        return scheme
    
    #将要保存该兵符时，验证其合法性
    def saveSchemeDetect(self):

        #检测方案是否合法：
        #illegal1:未选择主属性
        if Utils.boxGroupNoCheck(self.mainBoxGroup):
            reply = QMessageBox.critical(self,"兵符构建错误","请选择至少一个满足条件的主属性！")
            return
        #illegal2:未选择副属性
        if Utils.boxGroupNoCheck(self.subBoxGroup) and self.spinBox_subproperty.value() != 0:
            reply = QMessageBox.critical(self,"兵符构建错误","请选择至少一个满足条件的副属性，或设置副属性技能需求为0！")
            return
        #illegal3:技能选择过多
        if Utils.boxGroupCheckedNum(self.mustBoxGroup) + self.spinBox_choose.value() > 3:
            reply = QMessageBox.critical(self,"兵符构建错误","需求技能过多，请确保必选技能和可选技能需求数之和不大于3！")
            return
        #illegal4:未命名或命名重复
        if self.lineEdit_schemeName.text() == '':
            reply = QMessageBox.critical(self,"兵符构建错误","请为兵符方案命名！")
            return
        if self.lineEdit_schemeName.text() in self.currentSchemesName:
            reply = QMessageBox.critical(self,"兵符构建错误","方案名与已有的方案名重复！")
            return

        #构造一个合法的方案并准备写入
        scheme = self.createScheme()
        print(scheme)

        #发出信号，将scheme传递给父窗口
        self.signal_SchemeCreatedDone.emit(scheme)

        self.close()