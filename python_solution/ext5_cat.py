#实现cat命令
'''
1.显示文件内容
2.合并多个文件内容
3.将多个文件内容写入一个新文件
'''

from sys import argv

#读取文件名参数
file_list = argv[1:]

if len(file_list)==0:
    print("plese enter the argument")
else:
    #循环读取所有文件
    i = 0
    while i < len(file_list):
        f = open(file_list[i],'r')
        print(f.read())
        i = i + 1
    f.close()    
