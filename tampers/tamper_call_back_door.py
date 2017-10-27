#coding:utf-8
import re
from setColors import *
print ga.green+"************************************************"
print "From call_back_door.py scan the result ","********"
print "************************************************"+ga.end
rulelist =r'((call_user_func|preg_replace_callback|register_shutdown_function|register_tick_function|mb_ereg_replace_callback|filter_var|preg_replace_callback|ob_start|usort|uksort)[\S\s\n]{0,20}(GET|POST|REQUEST|system).{0,15})'
def Scan(filestr,filepath):
    """
    filestr 是主脚本中遍历的文件的内容
    filepath 是所遍历文件的地址
    """
    result=0
    count=1
    rule_r=re.search(rulelist,filestr)
    if rule_r!=None and ('\n' in rule_r.group()):
        #这里提取根据正则[\S\s\n]有换行提取无法显示行数，可以自行添加
        for line in filestr.split('\n'):
            count+=1
        print ga.yellow+u"文件位置：","[",filepath,"]"+ga.end
        print ga.red+u"回调函数：可能存在风险！\n"+ga.end,rule_r.group(),"---------> The code in %s line" % count
        print '\n'
        result+=1
    elif rule_r!=None and ('\n' not in  rule_r.group()):
        for line in filestr.split('\n'):
            if rule_r.group() in  line:
                print ga.yellow+u"文件位置：","[",filepath,"]"+ga.end
                print ga.red+u"回调函数：可能存在后门的风险！" +ga.end
                print rule_r.group(),"---------> The code in %s line"% count
                print '\n'
                # break
                result+=1
            count+=1
    return result