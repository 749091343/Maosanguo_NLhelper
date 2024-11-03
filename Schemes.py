# -*- coding: utf-8 -*-

import Utils

db_skillNames = {
             0:'未知技能',
             1:'高级迅捷',2:'高级护盾',3:'高级暴击',4:'高级怒火',5:'高级招架',
             6:'高级复仇',7:'高级魔抗',8:'高级物抗',9:'高级生机',10:'高级迟钝',
             11:'高级英勇',12:'高级专注',13:'高级法波',14:'高级法力',15:'高级强力',
             16:'高级暴伤',17:'高级镇压',18:'高级精准',19:'高级净化',20:'高级免控',
             21:'高级破甲',22:'高级命中',23:'高级免伤',24:'高级禁疗',25:'高级灭魂',
             26:'高级驱散',27:'高级减速',28:'高级光辉',29:'高级格挡',30:'高级抗暴',
             31:'超级迅捷',32:'超级护盾',33:'超级暴击',34:'超级怒火',35:'超级招架',
             36:'超级复仇',37:'超级魔抗',38:'超级物抗',39:'超级生机',40:'超级迟钝',
             41:'超级英勇',42:'超级专注',43:'超级法波',44:'超级法力',45:'超级强力',
             46:'超级暴伤',47:'超级镇压',48:'超级精准',49:'超级净化',50:'超级免控',
             51:'超级破甲',52:'超级命中',53:'超级免伤',54:'超级禁疗',55:'超级灭魂',
             56:'超级驱散',57:'超级减速',58:'超级光辉',59:'超级格挡',60:'超级抗暴',
             61:'初级技能',62:'中级技能',1001:'重复技能'
             }

db_mainProperties = {0:'未知属性',1:'血量',2:'攻击',3:'速度'}
db_subProperties  = {0:'未知属性',1:'攻击',2:'暴击',3:'暴击伤害',4:'血量',5:'神圣伤害',6:'格挡',7:'精准',8:'免控率',9:'破甲'}

def getSkillsID(strs):
    assert type(strs) == list,"bad type:list"
    IDList = []
    for skill in iter(strs):
        assert type(skill) == str,"bad type:str"
        #从db中获取技能对应的ID
        checkIDs = [k for k, v in db_skillNames.items() if v == skill]
        #若搜索失败
        if checkIDs == []:
            if skill[0:2] == "初级":
                checkIDs.append(61)
            elif skill[0:2] == "中级":
                checkIDs.append(62)
            else:
                checkIDs.append(0)
        IDList = IDList + checkIDs
    return IDList

def transSkillsID(IDs):
    assert type(IDs) == list,"bad type:list"
    strList = []
    for id in iter(IDs):
        if id in db_skillNames:
            strList.append(db_skillNames[id])
        else:
            strList.append(db_skillNames[0])
    return strList

def getMainPropertiesID(strs):
    assert type(strs) == list,"bad type:list"
    IDList = []
    for skill in iter(strs):
        assert type(skill) == str,"bad type:str"
        #从db中获取属性对应的ID
        checkIDs = [k for k, v in db_mainProperties.items() if v == skill]
        #若搜索失败
        if checkIDs == []:
            checkIDs.append(0)
        IDList = IDList + checkIDs
    return IDList

def transMainPropertiesID(IDs):
    assert type(IDs) == list,"bad type:list"
    strList = []
    for id in iter(IDs):
        if id in db_mainProperties:
            strList.append(db_mainProperties[id])
        else:
            strList.append(db_mainProperties[0])
    return strList

def getSubPropertiesID(strs):
    assert type(strs) == list,"bad type:list"
    IDList = []
    for skill in iter(strs):
        assert type(skill) == str,"bad type:str"
        #从db中获取属性对应的ID
        checkIDs = [k for k, v in db_subProperties.items() if v == skill]
        #若搜索失败
        if checkIDs == []:
            checkIDs.append(0)
        IDList = IDList + checkIDs
    return IDList

def transSubPropertiesID(IDs):
    assert type(IDs) == list,"bad type:list"
    strList = []
    for id in iter(IDs):
        if id in db_subProperties:
            strList.append(db_subProperties[id])
        else:
            strList.append(db_subProperties[0])
    return strList

#将方案转化为明细字符串
def transSchemeToString(getscheme):
    schemeStr =  \
            "方案名：" + getscheme['name'] + "\n" +\
            "目标主属性：" + Utils.strList2str(transMainPropertiesID(getscheme['main'])) + "\n" +\
            "目标副属性符合数：%d" % (getscheme['sub']['subNum']) + "\n" +\
            "目标副属性数：" + Utils.strList2str(transSubPropertiesID(getscheme['sub']['subPros'])) + "\n" +\
            "必有技能：" + Utils.strList2str(transSkillsID(getscheme['must'])) + "\n" +\
            "可选技能数：%d" % (getscheme['choose']['chooseNum']) + "\n" +\
            "可选技能：" + Utils.strList2str(transSkillsID(getscheme['choose']['chooseSkills'])) + "\n" +\
            "排除技能：" + Utils.strList2str(transSkillsID(getscheme['excl'])) + "\n" 
    return schemeStr

#将str兵符转化为数字兵符
#此外，还负责矫正重复的技能
def transRawtollyToTolly(rawtolly):
    #rawtolly有三个键值对，直接翻译即可：
    tolly = {'main':[],'sub':[],'skills':[]}
    tolly['main'] = getMainPropertiesID(rawtolly['main'])
    tolly['sub'] = getSubPropertiesID(rawtolly['sub'])
    tolly['skills'] = getSkillsID(rawtolly['skills'])
    #如果tolly里存在重复的技能，还要将其置为“重复技能”（优先级低于初级，中级，未知）
    for i_index in range(len(tolly['skills'])):
        for j_index in range(i_index + 1,len(tolly['skills'])):
            if tolly['skills'][i_index] == tolly['skills'][j_index] and (not tolly['skills'][i_index] in [0,61,62]):
                tolly['skills'][i_index] = 1001
                break

    return tolly

#将数字兵符转化为str兵符（把上面颠倒一下就是了）
def transTollyToRawtolly(tolly):
    #rawtolly有三个键值对，直接翻译即可：
    rawtolly = {'main':[],'sub':[],'skills':[]}
    rawtolly['main'] = transMainPropertiesID(tolly['main'])
    rawtolly['sub'] = transSubPropertiesID(tolly['sub'])
    rawtolly['skills'] = transSkillsID(tolly['skills'])
    return rawtolly


if __name__ == '__main__': 
    pass
    #print(transTollyToRawtolly(transRawtollyToTolly({'main':['血量'],'sub':['暴击伤害'],'skills':['究极迅捷','高级迅捷','高级迅捷']})))