#coding:utf-8
"""
设置显示的颜色
"""
class colors: 
    def __init__(self):
        self.green = "\033[92m" 
        self.blue = "\033[94m"
        self.bold = "\033[6m"
        self.yellow = "\033[93m"
        self.red = "\033[91m"
        self.end = "\033[0m"
ga = colors()