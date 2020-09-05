#两种处理命令参数的方法
import sys
import argparse

#老式的sys.argv
# sys.argv[0]代表程序文件路径本身，
# sys.argv[]，一个从程序外部获取参数的桥梁



#python的argparse包
'''
1.创建Argumentparser()对象
2.调用add_argument()方法
3.使用parse_args()解析添加的参数
'''

#add_argument 参数含义
'''
action参数的'store_true'指的是：触发action时为真，不触发则为假。即储存了一个bool变量，默认为false，触发不用赋值即变为true
type:指定参数类别，默认是str，传入数字要定义
help：是一些提示信息
default：是默认值
metavar: 在 usage 说明中的参数名称，对于必选参数默认就是参数名称，对于可选参数默认是全大写的参数名称.
'''
parser = argparse.ArgumentParser();

parser.add_argument('integers',metavar='N',type=int,nargs='+')
parser.add_argument('-B','--Boo',help='Boo help')
parser.add_argument('-c','--cmd',help='cmd help')
parser.add_argument('-m','--mod',help='mod help')
parser.add_argument('-s','--site',action='store_true')
parser.add_argument('-t','--tab',action='store_false')
parser.add_argument('-v','--verbose',action='store_true')

args = parser.parse_args()

print(args)
