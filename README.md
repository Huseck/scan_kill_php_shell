# scan_kill_php_shell
针对PHP网马的正则查杀
# 主要实现的特征
1.代码内容查找、时间更改查找

多线程自定义查找php代码及日志情况，以及文件的修改时间


2.动态加载插件  tamper 文件下的插件
直接复用模块，手动自己添加正则就ok 了

能匹配一些常规、已知、熟知的webshell 代码块
simple.py  简单的匹配一句话和base64编码特征的webshell
正则这里参考一下  Seay 大大的正则
call_back_door.py  匹配一些调用回调函数的后门

array_map_door.py  匹配以array开头的这一类函数

encode_door.py     匹配编码、组合、混淆的后门

编写规则
    1.文件名以tamper开头
    2.调用颜色函数 from setColors.py import * 例如ga.red+字符串+ga.end结束
    3.文集里包含Scan函数。具体看tamper_simple.py的样式

3.动态添加模糊哈希动态库





4.实现文件备份与比对，扫描日志的保存

备份每一个文件的md5值，如果文件被修改或者写入webshell 文件或者上传的文件，都会被比对出来
思路：首先是记录每一个初始文件的md5值，保存为md5.log
      之后如果md5.log存在，然后就创建一个md51.log
      再然后比对这两个日志文件，有异同，说明文件被更改过，然后拿出异常的文件做内容上的比对、检查文件

      另一个功能就是踩点监控，实时监控web网站目录文件，文件的增加，减少，改动都被监控下来，与之前文件相比对
5.分析 nginx apache  和waf.php 所抓取的web访问日志

# 有待完善






