#coding:utf-8
import re,os
from setColors import *
print ga.green+"************************************************"
print "From simple.py scan the result ","****************"
print "************************************************"+ga.end
"""
Private $_regex='(preg_replace.*\/e|`.*?\$.*?`|\bcreate_function\b|\bpassthru\b|\bshell_exec\b|\bexec\b|\bbase64_decode\b|\bedoced_46esab\b|\beval\b|\bsystem\b|\bproc_open\b|\bpopen\b|\bcurl_exec\b|\bcurl_multi_exec\b|\bparse_ini_file\b|\bshow_source\b|cmd\.exe|KAdot@ngs\.ru|小组|专用|提权|木马|PHP\s?反弹|shell\s?加强版|WScript\.shell|PHP\s?Shell|Eval\sPHP\sCode|Udp1-fsockopen|xxddos|Send\sFlow|fsockopen\('(udp|tcp)|SYN\sFlood)';
"""
rulelist = [
    r'(\$_(GET|POST|REQUEST)\[.{0,15}\]\s{0,10}\(\s{0,10}\$_(GET|POST|REQUEST)\[.{0,15}\]\))',
    r'(base64_decode\([\'"][\w\+/=]{200,}[\'"]\))',
    r'(eval(\s|\n)*\(base64_decode(\s|\n)*\((.|\n){1,200})',
    r'((eval|assert)(\s|\n)*\((\s|\n)*\$_(POST|GET|REQUEST)\[.{0,15}\]\))',
    r'(\$[\w_]{0,15}(\s|\n)*\((\s|\n)*\$_(POST|GET|REQUEST)\[.{0,15}\]\))',
    r'(call_user_func\(.{0,15}\$_(GET|POST|REQUEST))',
    r'(preg_replace(\s|\n)*\(.{1,100}[/@].{0,3}e.{1,6},.{0,10}\$_(GET|POST|REQUEST))',
    r'(wscript\.shell)',
    r'(cmd\.exe)',
    r'(shell\.application)',
    r'(documents\s+and\s+settings)',
    r'(system32)',
    r'(serv-u)',
    r'(phpspy)',
    r'(jspspy)',
    r'(webshell)',
    r'(Program\s+Files)',
    r'(小组)',
    r'(专用)',
    r'(提权)',
    r'(反弹)'
    r'(caidao)',
    r'(菜刀)'
]
def Scan(filestr,filepath):
    """
    filestr 是主脚本中遍历的文件的内容
    filepath 是所遍历文件的地址
    """
    result=0
    count=1
    for rule in rulelist:
        rule_r=re.search(rule,filestr)
        if rule_r!=None:
            print ga.red+u"文件位置："+ga.end,filepath
            for line in filestr.split('\n'):
                if rule_r.group() in  line:
                    print rule_r.group()[0:100],"--------->The code in %s line" % count
                    print '\n'
                    result+=1
                count+=1
    return result