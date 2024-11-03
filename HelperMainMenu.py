# -*- coding: utf-8 -*-

from HelperMainMenu_UI import Ui_MainWindow
from TollyScheme import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt,QObject, pyqtSignal, QProcess
from PyQt5 import QtCore
import Schemes
import Utils
import json
import os

class HelperMainMenu(QMainWindow,Ui_MainWindow):
    #自定义信号：方案已被改变
    signal_SchemeChanged = pyqtSignal()

    def __init__(self,parent=None):
        super(HelperMainMenu,self).__init__(parent)
        self.setupUi(self)

        self.setupSignal()
        #设置窗体图标
        self.setWindowIcon(QIcon('./icons/nighter_icon2_256x256.ico'))

        #载入的所有方案
        self.loadedAllSchemes = []

        #载入的被应用的方案
        self.loadedAppliedSchemes = []

        #载入文件中的方案
        self.loadFileSchemes()

        #暂存日志
        self.log = ''

        self.washProcess = None

    #定义信号
    def setupSignal(self):
        #按钮初设
        self.pushButton_delete.setEnabled(False)
        self.pushButton_apply.setEnabled(False)
        self.pushButton_remove.setEnabled(False)
        self.pushButton_abort.setEnabled(False)


        #影响按钮可用性的信号绑定（lambda函数）
        self.listWidget_sche.itemClicked.connect(lambda :self.pushButton_delete.setEnabled(True))
        self.listWidget_sche.itemClicked.connect(lambda :self.pushButton_apply.setEnabled(True))
        self.listWidget_sche.itemClicked.connect(lambda :self.pushButton_remove.setEnabled(False))

        self.listWidget_apply.itemClicked.connect(lambda :self.pushButton_delete.setEnabled(False))
        self.listWidget_apply.itemClicked.connect(lambda :self.pushButton_apply.setEnabled(False))
        self.listWidget_apply.itemClicked.connect(lambda :self.pushButton_remove.setEnabled(True))

        #启动说明文档
        self.pushButton_readme.clicked.connect(self.helpProcedureStart)

        #启动脚本
        self.pushButton_start.clicked.connect(self.washProcedureStart)

        #终止脚本
        self.pushButton_abort.clicked.connect(self.washProcedureAbort)
        

        #方案变动后，发送一个信号到UI
        self.signal_SchemeChanged.connect(self.updateAllSchemesUI)

        self.listWidget_sche.itemClicked.connect(self.updateSchemeContentUI)
        self.listWidget_apply.itemClicked.connect(self.updateSchemeContentUI)

        #创建按钮发送信号以初始化子窗口
        self.pushButton_create.clicked.connect(self.createSchemeForm)

        #删除按钮
        self.pushButton_delete.clicked.connect(self.deleteSchemes)
        #应用按钮
        self.pushButton_apply.clicked.connect(self.applySchemes)
        #移除按钮
        self.pushButton_remove.clicked.connect(self.removeSchemes)

    #创建兵符搭建子窗口
    def createSchemeForm(self):
        #初始化子窗口
        self.tollyScheme = TollyScheme()
        #将子窗口信号绑定至父窗口的指定处理函数
        self.tollyScheme.signal_SchemeCreatedDone.connect(self.addSchemes)

        self.tollyScheme.setWindowModality(Qt.ApplicationModal)
        self.tollyScheme.currentSchemesName = Utils.getListWidgetItems(self.listWidget_sche)
        self.tollyScheme.show()

    #更新所有方案的UI
    def updateAllSchemesUI(self):
        print("UI已更新")
        #首先移除原本listWidget中的所有项
        self.listWidget_sche.clear()
        self.listWidget_apply.clear()
        for scheme in iter(self.loadedAllSchemes):
            self.listWidget_sche.addItem(scheme['name'])
        for scheme in iter(self.loadedAppliedSchemes):
            self.listWidget_apply.addItem(scheme['name'])

    #展示选中方案详细内容UI于特定窗口
    def updateSchemeContentUI(self,item):
        getscheme = {}
        for scheme in iter(self.loadedAllSchemes):
            if scheme['name'] == item.text():
                getscheme = scheme
        if getscheme != {}:
            print(getscheme)
        else:
            print("error,未找到方案。")
        print("已展示方案的详细信息")

        self.textEdit_current_scheme.clear()
        self.textEdit_current_scheme.setText(Schemes.transSchemeToString(getscheme))
        # self.textEdit_current_scheme.setText(
        #     "详细方案：\n"+
        #     "方案名：" + getscheme['name'] + "\n" +
        #     "目标主属性：" + Utils.strList2str(Schemes.transMainPropertiesID(getscheme['main'])) + "\n" +
        #     "目标副属性符合数：%d" % (getscheme['sub']['subNum']) + "\n" +
        #     "目标副属性数：" + Utils.strList2str(Schemes.transSubPropertiesID(getscheme['sub']['subPros'])) + "\n" +
        #     "必有技能：" + Utils.strList2str(Schemes.transSkillsID(getscheme['must'])) + "\n" +
        #     "可选技能数：%d" % (getscheme['choose']['chooseNum']) + "\n" +
        #     "可选技能：" + Utils.strList2str(Schemes.transSkillsID(getscheme['choose']['chooseSkills'])) + "\n" +
        #     "排除技能：" + Utils.strList2str(Schemes.transSkillsID(getscheme['excl'])) + "\n" 
        #     )



    #载入所有文件中的方案（仅作用于父窗口）
    def loadFileSchemes(self):
        for filepath in iter(os.listdir(r'./Schemes')):
            with open('./Schemes/' + filepath, 'r', encoding='utf-8') as jsonfile:
                self.loadedAllSchemes.append(json.load(jsonfile))
        #TODO:记得补做一下json读入时候的数据格式是否正确
        self.signal_SchemeChanged.emit()

    #从子窗口获取数据，并生成一个新的兵符方案
    def addSchemes(self,scheme):
        #添加方案
        self.loadedAllSchemes.append(scheme)
        #将方案保存为文件
        with open('./Schemes/'+ scheme['name'] +'.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(scheme, jsonfile, ensure_ascii=False, indent=4)
        #发出兵符方案变动信号
        self.signal_SchemeChanged.emit()

    #从备选方案中选择一个，添加到应用方案中
    def applySchemes(self):
        #没有方案就返回
        if self.listWidget_sche.count() == 0:
            return
        #没有选择就返回
        if not self.listWidget_sche.currentItem():
            return 
        currentText = self.listWidget_sche.currentItem().text()
        for scheme in iter(self.loadedAllSchemes):
            if scheme['name'] == currentText and not(currentText in Utils.getListWidgetItems(self.listWidget_apply)):
                if self.listWidget_apply.count() >= 5:
                    QMessageBox.warning(self,"方案限制","至多可应用5个方案，请先移除部分方案。（方案过多会导致洗符卡慢）")
                    return
                else:
                    self.loadedAppliedSchemes.append(scheme)
                    print("已应用方案")
        #发出兵符方案变动信号
        self.signal_SchemeChanged.emit()

    #将已应用的方案移除
    def removeSchemes(self):
        #没有应用方案就返回
        if self.listWidget_apply.count() == 0:
            return
        #没有选择就返回
        if not self.listWidget_apply.currentItem():
            return 
        currentText = self.listWidget_apply.currentItem().text()
        for index , scheme in enumerate(self.loadedAppliedSchemes):
            if scheme['name'] == currentText:
                del self.loadedAppliedSchemes[index]
                print("已移除方案")
                break
        #发出兵符方案变动信号
        self.signal_SchemeChanged.emit()

    #从方案库中删除不需要的方案
    def deleteSchemes(self):
        #没有方案就返回
        if self.listWidget_sche.count() == 0:
            return
        #没有选择就返回
        if not self.listWidget_sche.currentItem():
            return 
        currentText = self.listWidget_sche.currentItem().text()
        reply = QMessageBox.question(self,"确认删除","确实要删除吗？此操作不能撤销。",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        #取消删除
        if reply == QMessageBox.No:
            print("取消删除")
            return
        #删除方案库中的项
        for index , scheme in enumerate(self.loadedAllSchemes):
            if scheme['name'] == currentText:
                del self.loadedAllSchemes[index]
                break
        #如果方案已经被应用，则一并删除
        for index , scheme in enumerate(self.loadedAppliedSchemes):
            if scheme['name'] == currentText:
                del self.loadedAppliedSchemes[index]
                break
        #删除对应方案的文件
        #TODO:验证文件是否还存在
        os.remove('./Schemes/' + currentText +'.json')

        #发出兵符方案变动信号
        self.signal_SchemeChanged.emit()                



    def handleStderr(self):  # 处理报错信息的函数
        if self.washProcess is not None:
            data = self.washProcess.readAllStandardError()
            #stderr = bytes(data).decode("gbk")  # 字符串格式的报错信息
            stderr = bytes(data).decode("utf-8")  # 字符串格式的报错信息
            self.log += stderr
            self.textEdit_log.append(stderr)
            print(stderr)

    def handleStdout(self):  # 处理正常输出信息的函数
        if self.washProcess is not None:
            data = self.washProcess.readAllStandardOutput()
            #stdout = bytes(data).decode("gbk")  # 字符串形式的输出信息
            stdout = bytes(data).decode("utf-8")  # 字符串形式的输出信息
            self.log += stdout
            self.textEdit_log.append(stdout)
            print(stdout)

    #兵符进程终结后的执行
    def washProcedureAfterFinished(self):
        #切换按键状态
        self.pushButton_start.setEnabled(True)
        self.pushButton_abort.setEnabled(False)
        print('脚本已终结')
        QMessageBox.information(self,"洗符结束","洗符脚本已自主退出。")

    #启动兵符进程
    def washProcedureStart(self):
        #并没有任何已经应用的方案
        if len(self.loadedAppliedSchemes) == 0:
            reply = QMessageBox.critical(self,"脚本启动失败","没有应用任何方案！")
            return
        #将已应用的方案打包为文件写入
        folder_path = "AppliedTemp"
        #将预交接的文件夹清空
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        #写入已应用的方案
        for scheme in iter(self.loadedAppliedSchemes):
            with open('./AppliedTemp/'+ scheme['name'] +'.json', 'w', encoding='utf-8') as jsonfile:
                json.dump(scheme, jsonfile, ensure_ascii=False, indent=4)
        print("方案写入完毕。")

        #切换按键状态
        self.pushButton_start.setEnabled(False)
        self.pushButton_abort.setEnabled(True)

        self.washProcess = QProcess()#创建进程
        if self.washProcess is not None:
            self.washProcess.readyReadStandardOutput.connect(self.handleStdout)#绑定正常信息输出函数
            self.washProcess.readyReadStandardError.connect(self.handleStderr)#绑定错误信息输出函数

            args = []

            washProcess_path = r'washProcess.exe'
            #args.append(washProcess_path)
            #将窗口值传到子进程
            if self.lineEdit_simu.text() == '':
                args.append('default')
            else:
                args.append(self.lineEdit_simu.text())

            self.washProcess.start(washProcess_path, args)

            self.washProcess.finished.connect(self.washProcedureAfterFinished)#子进程结束之后会调用的函数,对应的还有一个进程开始时能绑定的函数

    #终止兵符进程
    def washProcedureAbort(self):
        self.washProcess.kill()

    #启动帮助文档进程
    def helpProcedureStart(self):
        print("启动readme")
        #os.system("notepad docs/ReadMe.txt")
        self.readmeProcess = QProcess()
        self.readmeProcess.startDetached("notepad",["./docs/ReadMe.txt"])

if __name__ == '__main__': 
    pass


    

