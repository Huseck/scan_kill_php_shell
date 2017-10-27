#coding:utf-8
import re
from setColors import *
print ga.green+"************************************************"
print "From encode_door.py scan the result ","***********"
print "************************************************"+ga.end
rulelist=[
    r'(((chr\((99|104|114)\))|(chr\((99|104|114)\)))[.\r\n\S]{0,40})',
    r'((chr\((80|79|83|84)\))[.\r\n\S]{0,40})',
    r'(\"a\"\.\"s\"\.\"s\"\.\"e\"\.\"r\"\.\"t\").{1,20}\$_(GET|POST|REQUEST).{0,15}',
    r'((\'P\'\.\'O\'\.\'S\'\.\'T\')[.\r\n\S]{0,20})',
    r'((\"g\"\.\"e\"\.\"t\")[.\r\n\S]{0,20})',

]
def Scan(filestr,filepath):
    """
    filestr 是主脚本中遍历的文件的内容
    filepath 是所遍历文件的地址
    """
    result=0
    for rule in rulelist:
        rule_r=re.search(rule,filestr,re.IGNORECASE)
        if rule_r!=None:
            print ga.yellow+u"文件位置："+ga.end,filepath
            print ga.red+u"混淆的代码:"+ga.end,rule_r.group()
            print '\n'
            result+=1
    return result