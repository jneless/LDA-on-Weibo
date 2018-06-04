# -*- coding: UTF-8 -*-
import re
import os


#生成两个 正则表达式
#获取格式为"数字："开头的字符串
pattern1 = re.compile('\d+:.*')
#获取格式为"数字数字：数字数字"的字符串
pattern2 = re.compile('\d\d:\d\d')


#制定路径
walk = os.walk('weibo')

r=[]

#读取路径下全部文件
for root, dirs, files in walk:

    #遍历全部文件
    for name in files:

        #按顺序一个个打开文件
        f = open(os.path.join(root, name), 'r')
        for line in open(os.path.join(root, name), 'r'):

            #读取文件一行
            content=f.readline()

            #得到全部满足正则表达式1的字符串
            x=pattern1.findall(content)
            r.extend(x)

output=[]
for con in r:
    rr= pattern2.findall(con)


    # 如果数字：数字匹配成功，则不操作
    if len(rr) != 0:
        pass

    # 如果数字：数字匹配不成功，说明是文字
    # 还有一种不成的情况，因为con本身是空
    if len(rr) == 0 and con != []:
        output.append(con)

# fileObject = open('weibo/output.txt', 'wb')
fileObject = open('output1/output.txt', 'wb')
for co in output:
    fileObject.write(co)
    fileObject.write('\n')
fileObject.close()