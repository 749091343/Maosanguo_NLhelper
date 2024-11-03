# -*- coding: utf-8 -*-

#该模块主要用于做兵符和方案的验证

import cvLib
import time

#验证该兵符是否合法，合法返回True，反之False
def verifyTollyisLegal(tolly):
    #验证缺少元素
    if (tolly['main'] is None) or (tolly['sub'] is None) or (tolly['skills'] is None):
        return False
    if len(tolly['main']) != 1:
        return False
    if len(tolly['sub']) < 1 or len(tolly['sub']) > 2:
        return False
    if len(tolly['skills']) != 3:
        return False
    return True

#验证方案集合是否合法，合法返回True，反之False
def verifySchemeisLegal(schemes):
    #没有方案 报错
    if len(schemes) == 0:
        return False
    for scheme in iter(schemes):
        #TODO:先写一下简单验证，以防浪费时间，后面再补吧
        if (scheme['main'] is None) or (scheme['sub'] is None) or (scheme['must'] is None) or (scheme['choose'] is None):
            return False
    return True

#对比兵符和单个方案是否匹配，必须全部通过检测才能返回True
def matchTollyandScheme(tolly,scheme):

    #对比主属性
    if not (tolly['main'][0] in scheme['main']):
        return False
    
    #对比副属性
    if scheme['sub']['subNum'] > 0:
        matchesNum = 0
        for p in tolly['sub']:
            if p in scheme['sub']['subPros']:
                matchesNum = matchesNum + 1
        if matchesNum < scheme['sub']['subNum']:
            return False
    
    #对比must技
    if len(scheme['must']) > 0:
        for skill in scheme['must']:
            if not (skill in tolly['skills']):
                return False

            
    #对比choose技
    if scheme['choose']['chooseNum'] > 0:
        matchesNum = 0
        for skill in tolly['skills']:
            if skill in scheme['choose']['chooseSkills']:
                matchesNum = matchesNum + 1
        if matchesNum < scheme['choose']['chooseNum']:
            return False
        
    #对比excl技
    if len(scheme['excl']) > 0:
        for skill in tolly['skills']:
            if skill in scheme['excl']:
                return False
            
    return True

#核心函数
#依次核对兵符是否符合预设方案的要求
def matchTollyandSchemes(tolly,schemes):
    for scheme in iter(schemes):
        if matchTollyandScheme(tolly,scheme):
            #兵符符合这个方案！完成洗符
            print("已找到符合条件的兵符！")
            print("该兵符符合方案："+scheme['name'])
            return True
    return False