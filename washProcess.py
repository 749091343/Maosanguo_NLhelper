# -*- coding: utf-8 -*-

import sys
import json
import os
import codecs

#作为被调用的子进程，这里需要导入两个参数：
#1、窗口名:windowName
#2、兵符方案集:schemes
if __name__ == '__main__':
    #调整编码
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

    print("初始化OCR库中...")
    #刷新输出
    sys.stdout.flush()

    import cvLib
    import time
    import Schemes
    import Verifier

    print("OCR库初始化完成。")
    #刷新输出
    sys.stdout.flush()


#预设参数读入方案如下：

    windowName = sys.argv[1]
    schemes = []

    #载入json
    for filepath in iter(os.listdir(r'./AppliedTemp')):
        with open('./AppliedTemp/' + filepath, 'r', encoding='utf-8') as jsonfile:
            schemes.append(json.load(jsonfile))

    #清空AppliedTemp目录
    folder_path = "AppliedTemp"
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)


#预设参数到此为止

    print("验证兵符配置是否合法中...")
    if(not Verifier.verifySchemeisLegal(schemes)):
        print("方案合法性验证未通过，方案可能发生损坏，请尝试删除并重新配置方案！")
        sys.exit(1)
    for scheme in iter(schemes):
        print(Schemes.transSchemeToString(scheme))
    print("方案应用功能无误。")
    #刷新输出
    sys.stdout.flush()

    print("校正窗口大小中...")
    #刷新输出
    sys.stdout.flush()
    cvLib.adjustWindowSize2Standard(windowName,cvLib.offsetGroup_MuMu12_900_1600)
    #截图缓冲
    time.sleep(1)

    rawtolly = cvLib.getRawTollyFromWindow(windowName,cvLib.offsetGroup_MuMu12_900_1600)
    print("验证OCR功能是否正常中...")
    if(not Verifier.verifyTollyisLegal(rawtolly)):
        print("OCR功能验证未通过，请确认游戏窗口已按要求配置好！")
        sys.exit(1)
    print("OCR功能无误。")
    #刷新输出
    sys.stdout.flush()

    #洗符次数
    washCnt = 0

    while(True):
        rawtolly = cvLib.getRawTollyFromWindow(windowName,cvLib.offsetGroup_MuMu12_900_1600)

        tolly = Schemes.transRawtollyToTolly(rawtolly)
        print(Schemes.transTollyToRawtolly(tolly))

        if(Verifier.matchTollyandSchemes(tolly,schemes)):
            break
        cvLib.simulateClick(windowName,cvLib.offsetGroup_MuMu12_900_1600)
        washCnt = washCnt + 1
        print("%s 已洗第 %d 次" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),washCnt))
        #刷新输出
        sys.stdout.flush()

        time.sleep(2.5)

    
