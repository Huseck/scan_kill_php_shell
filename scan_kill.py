#coding:utf-8
import os,sys,time,hashlib
from tampers.setColors import *
reload(sys)
sys.setdefaultencoding('utf-8') #设置字符编码
"""
1.首先是查找文件代码段所在位置

"""
def ls_allfile(path):
    filename_l=[]
    for root, dirs, files in os.walk(path):
        for filename in files:
            # print os.path.join(root,filename)
            filename_l.append(os.path.join(root,filename))
    return filename_l
def find_code(filename):
    with open(filename) as f:
        return f.read()
def print_lines(string):

    filelist = ls_allfile(sys.argv[1])
    for src in filelist:
        count=1
        for value in find_code(src).split('\n'):
            if string in value:
                print ga.green+src+ga.end+'\n',value,'-------->The value in '+ga.red+'%s' % count+ga.end+' line'
                print '\n'
            count+=1
"""
2.备份文件的md5值和最后修改时间进行文件内容的匹配查找，使用BP的对比功能可以很快的查找变动的地方
后续的使用python代码来分析两次备份的文件来显示变动的内容
"""
def getMD5(filepath):
    fh=open(filepath,'rb')
    m=hashlib.md5()
    while True:
        data =fh.read(8192)
        if not data:
            break
        m.update(data)
    fh.close()
    return m.hexdigest()
def getFileTime(filepath):
    fileModifyTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(filepath)))
    return fileModifyTime
"""
3.使用动态监控文件的改动情况从备份的文件进行周期性对比
"""



"""
5.动态加载插件---->自行构造webshell木马的正则匹配
插件保存到tampers文件下动态加载
"""
def scan(file_path):
    result=0
    for root,path,filename in os.walk('tampers'):
        for file in filename:
            if file[-3:]=='.py' and file[:6]=='tamper':
                tampers=file[:-3]
                if tampers=='__init__':
                    continue
                __import__('tampers.'+tampers)
                path_file=ls_allfile(file_path)
                for file_value in ls_allfile(file_path):
                    filestr=find_code(file_value)

                    if sys.modules['tampers.'+tampers].Scan(filestr,file_value) >=1:
                            result+=1
    print ga.blue+ga.bold+"The scan result is [%s] webshells,hope can help you!" %result +ga.end


if __name__ == '__main__':

    print ga.green+"""
__________________________________
/\                              /\\
\_|    Thank you for             |
  |    Using ScanWebshell!       |
  |    By:Seck                   |
  |  ____________________________|
  \_/____________________________/
"""+ga.end
    if len(sys.argv)<=1:
        print ga.green+"[!] Input -h can help you!"+ga.end
    elif sys.argv[1]=='-h':
        print ga.green+"[#------------------------------------------------------]"
        print "find the 'code':scan_kill.py filenames 'codevalue'"
        print "find webshell:scan_kill.py -s filename"
        print "backup filetime webshell:scan_kill.py -t filename time_log.txt"
        print "[#]"+ga.end
    elif sys.argv[1]=='-s' and sys.argv[2]:
        scan(sys.argv[2])
    elif sys.argv[1]=='-t' and sys.argv[2] and sys.argv[3]:
        all_file=ls_allfile(sys.argv[2])
        f_list=[]
        for file in all_file:
            f_list.append(getFileTime(file)+' '+file+'->'+getMD5(file)+'\r\n')
            with open(sys.argv[3],'w') as f:
                f.writelines(f_list)
            # print getFileTime(file),file
    elif sys.argv[2]:
        print_lines(sys.argv[2])

