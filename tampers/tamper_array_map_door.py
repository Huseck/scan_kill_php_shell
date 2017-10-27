#coding:utf-8
import re
from setColors import *
print ga.green+"************************************************"
print "From array_map_door.py scan the result ","********"
print "************************************************"+ga.end
rulelist =r'((array_map|array_filter|array_reduce|array_walk|array_diff_ukey)[\s\n]{0,20}\(.{1,5}(eval|assert|ass\\x65rt).{1,20}\$_(GET|POST|REQUEST).{0,15})'
def Scan(filestr,filepath):
    """
    filestr 是主脚本中遍历的文件的内容
    filepath 是所遍历文件的地址
    """
    count=1
    result=0
    rule_r=re.search(rulelist,filestr)
    if rule_r!=None:
        print ga.red+u"文件位置："+ga.end,filepath
        for line in filestr.split('\n'):
            if rule_r.group() in  line:
                print rule_r.group(),"--------->The code in %s line" % count,'\n\n'
                result+=1
            count+=1
    return result
