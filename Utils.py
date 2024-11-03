# -*- coding: utf-8 -*-

#实用函数

def strList2str(strList):
    fstr = ''
    for s in iter(strList):
        fstr = fstr + s + ' '
    return fstr

#如果一组checkbox均为被选择，就返回true
def boxGroupNoCheck(boxgroup):
    for box in iter(boxgroup):
        if box.isChecked():
            return False
    return True

#返回一组checkboxgroup被选择的数量
def boxGroupCheckedNum(boxgroup):
    CheckedNum = 0
    for box in iter(boxgroup):
        if box.isChecked():
            CheckedNum = CheckedNum + 1
    return CheckedNum

#返回listwidget中的所有项（字符串列表）
def getListWidgetItems(listWidget):
    widgetres = []
    count = listWidget.count()
    for i in range(count):
        widgetres.append(listWidget.item(i).text())
    return widgetres