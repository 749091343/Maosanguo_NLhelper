# -*- coding: utf-8 -*-

import win32gui, win32ui, win32con, win32api
import cv2
import sys
import numpy
import pyautogui
import easyocr
from PIL import Image, ImageFilter, ImageEnhance

import Schemes

offsetGroup_MuMu12_900_1600 = {

    'offsetAllSkills':{'rleft':269,'rtop':584,'rwidth':216,'rheight':30},
    'offsetMainProperty':{'rleft':280,'rtop':423,'rwidth':172,'rheight':21},
    'offsetSubProperty1':{'rleft':280,'rtop':444,'rwidth':172,'rheight':21},
    'offsetSubProperty2':{'rleft':280,'rtop':465,'rwidth':172,'rheight':21},
    'offsetClick':{'rleft':358,'rtop':732},

    'offsetAdjust':{'rwidth':527,'rheight':970}
}


#调整窗口的大小以便截图
def adjustWindowSize2Standard(windowName,posDict):
    #获取后台窗口的句柄，注意后台窗口不能最小化
    hWnd = win32gui.FindWindow(0,windowName)
    #没找到窗口？
    if hWnd == 0:
        print("未找到指定的窗口，脚本已退出，请检查模拟器窗口名是否存在。")
        sys.exit(1)
        #raise ValueError('window not found.')

    #获取句柄窗口的大小信息
    #left, top, right, bot = win32gui.GetWindowRect(hWnd)

    win32gui.SetWindowPos(hWnd,win32con.NULL, 0,0,posDict['offsetAdjust']['rwidth'],posDict['offsetAdjust']['rheight'], win32con.SWP_NOZORDER)

    pass


def getSubFigureFromWindow(windowName,savePath,posDict={}):
    assert type(posDict) == dict,"传入的位置信息格式错误！" 

    #获取后台窗口的句柄，注意后台窗口不能最小化
    hWnd = win32gui.FindWindow(0,windowName)
    #没找到窗口？
    if hWnd == 0:
        print("未找到指定的窗口，脚本已退出，请检查模拟器窗口名是否存在。")
        sys.exit(1)
        #raise ValueError('window not found.')
    hWnd_ex = win32gui.FindWindowEx(hWnd,None,None,None)   
    #获取句柄窗口的大小信息
    left, top, right, bot = win32gui.GetWindowRect(hWnd_ex)
    
    #print('窗口pos:',left, top, right, bot)

    if not posDict == {}:
        left = posDict['rleft']
        top = posDict['rtop']
        width = posDict['rwidth']
        height = posDict['rheight']
    else:
        left = 0
        top = 0
        width = right - left
        height = bot - top

    #print('窗口大小:',width,'*',height)

    pyautogui.FAILSAFE = False
    #返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hWndDC = win32gui.GetWindowDC(hWnd_ex)
    #创建设备描述表
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)
    #创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    #创建位图对象准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    #为bitmap开辟存储空间
    saveBitMap.CreateCompatibleBitmap(mfcDC,width,height)
    #将截图保存到saveBitMap中
    saveDC.SelectObject(saveBitMap)
    #保存bitmap到内存设备描述表
    saveDC.BitBlt((0,0), (width,height), mfcDC, (left, top), win32con.SRCCOPY)
    ###获取位图信息
    signedIntsArray = saveBitMap.GetBitmapBits(True)
    #内存释放
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hWnd,hWndDC)
    #保存到文件
    img = numpy.frombuffer(signedIntsArray, dtype = 'uint8')
    img.shape = (height, width, 4)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    cv2.imwrite(savePath,img,[int(cv2.IMWRITE_JPEG_QUALITY), 100])

#从技能图片中提取出技能
#返回一个list
def skillHandler(skillComponent):
    assert type(skillComponent) == list,"参数格式错误！"

    #没有读取到技能，返回空表，由验证函数来处理
    if skillComponent == []:
        return skillComponent

    skills = skillComponent[0].replace(" ","")

    if len(skills) == 12:
        return [skills[0:4],skills[4:8],skills[8:12]]
    else:
        return ['未知技能',skills[-8:-4],skills[-4:]]

#从属性图片中提取出属性
#返回一个str
def propertyHandler(property):
    assert type(property) == list,"参数格式错误！"

    #读到空串，直接返回该空串
    if len(property) == 0:
        return property

    return [(property[0].split('+'))[0]]


#截取所有需要的图片，保存后，利用OCR提取其信息，构成一个完整的兵符信息
#返回一个rawtolly（仅由文本构成的兵符信息）
def getRawTollyFromWindow(windowName,posDictGroup):
    #截图
    getSubFigureFromWindow(windowName,'./FigureTemp/skills.jpg',posDictGroup['offsetAllSkills'])
    getSubFigureFromWindow(windowName,'./FigureTemp/mainp1.jpg',posDictGroup['offsetMainProperty'])
    getSubFigureFromWindow(windowName,'./FigureTemp/subp1.jpg',posDictGroup['offsetSubProperty1'])
    getSubFigureFromWindow(windowName,'./FigureTemp/subp2.jpg',posDictGroup['offsetSubProperty2'])

    #载入视觉识别模型
    reader = easyocr.Reader(['ch_sim'],gpu=True,verbose=False)

    rawtolly = {'main':[],'sub':[],'skills':[]}

    rawtolly['main'] = propertyHandler(reader.readtext('./FigureTemp/mainp1.jpg',detail = 0))
    rawtolly['sub'] =  propertyHandler(reader.readtext('./FigureTemp/subp1.jpg',detail = 0)) + \
                       propertyHandler(reader.readtext('./FigureTemp/subp2.jpg',detail = 0)) 
    rawtolly['skills'] = skillHandler(reader.readtext('./FigureTemp/skills.jpg',detail = 0))

    return rawtolly


#该函数进行一次鼠标模拟点击，用于洗兵符，模拟点击时，不能让窗口最小化，注意！
def simulateClick(windowName,posDictGroup):
    w1hd = win32gui.FindWindow(0,windowName)
    w2hd = win32gui.FindWindowEx(w1hd,None,None,None)  

    #模拟鼠标指针 传送到指定坐标
    long_position = win32api.MAKELONG(posDictGroup['offsetClick']['rleft'],posDictGroup['offsetClick']['rtop'])

    win32api.SendMessage(w2hd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)#模拟鼠标按下
    win32api.SendMessage(w2hd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)#模拟鼠标弹起

if __name__ == '__main__':
    adjustWindowSize2Standard("MuMu模拟器12-1")
    #print((getRawTollyFromWindow('MuMu模拟器12',offsetGroup_MuMu12_900_1600)))

    pass

