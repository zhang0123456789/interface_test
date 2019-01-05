#!/usr/bin/env python
# -*- coding:utf-8-*-
#@author:蜜蜜
#@file: study_re.py 
#@time: 2018/12/23 
#@email:1402686685@qq.com

import  re
'''re.match 尝试从字符串的起始位置匹配一个模式，
如果不是起始位置匹配成功的话，match()就返回none。'''

# s='{"mobilephone":"15800447656","pwd":"12345678"}'
# s1='hello world'
# pattern='hello'#正则表达式
# res=re.match(pattern=pattern,string=s1)#最开始位置查找
# print(res)

# s='{"mobilephone":"15800447656","pwd":"12345678"}'
# s1='world hello world'
# pattern='hello'#正则表达式
# res=re.match(pattern=pattern,string=s1)#最开始位置查找
# print(res)  #返回none

'''和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，
并把它们作为一个迭代器返回。'''

# s='{"mobilephone":"15800447656","pwd":"12345678"}'
# s1='hello world hello'
# pattern='hello'#正则表达式
# res=re.match(pattern=pattern,string=s1)#最开始位置查找
# print(res)
# res_1=re.findall(pattern=pattern,string=s1)
# print(res_1)


'''re.search 扫描整个字符串并返回第一个成功的匹配。'''

'''re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，
则匹配失败，函数返回None；
而re.search匹配整个字符串，直到找到一个匹配。'''
# s1='world hello'
# pattern='hello'#正则表达式
# res=re.match(pattern=pattern,string=s1)#最开始位置查找
# print(res)
# res_1=re.findall(pattern=pattern,string=s1)#查找全部字符串，并返回
# print(res_1)
# res_2=re.search(pattern=pattern,string=s1)#从任意位置找
# print(res_2)

# s1='hello world hello'
# pattern='hello'#正则表达式
# res=re.match(pattern=pattern,string=s1)#最开始位置查找
# print(res)
# res_1=re.findall(pattern=pattern,string=s1)#查找全部字符串，并返回
# print(res_1)
# res_2=re.search(pattern=pattern,string=s1)#从任意位置找
# print(res_2)


# s='{"mobilephone":"15800447656","pwd":"12345678"}'
# res_4=re.findall(pattern='(\d)',string=s)
# print(res_4)

# s='{"mobilephone":"15800447656","pwd":"12345678"}'
# res_4=re.findall(pattern='(\d*)',string=s)
# print(res_4)

# s='{"mobilephone":"15800447656","pwd":"12345678"}'
# res_4=re.findall(pattern='(\d{11})',string=s)
# print(res_4[0])
# mobilephone=res_4[0]
# print(mobilephone)
# ss=s.replace(mobilephone,"15800447656")
# print(ss)


# s='{"mobilephone":"${register}","pwd":"12345678"}'
# res_5=re.findall(pattern='\$\{(.*?)\}',string=s)
# print(res_5)


#正则表达式分组
# s4='www.lemonban.com'
# p='(w)(ww)'#（）进行分组
# m=re.search(p,s4)
# print(m)
# print(m.group())#全部匹配==print(m.group())=print(m.group(0))
# print(m.group(1))#拿到第一个分组里面的字符
# print(m.group(2))#拿到第二个分组里面的字符

s='{"mobilephone":"${normal_user}","pwd":"${pwd}"}'
p='\$\{(.*?)\}'
m=re.search(p,s)
print(m.group())
print(m.group(1))
key=m.group(1)

while re.search(p,s):#找到一个就返回match
    m=re.search(p,s)
    print(m.group())
    print(m.group(1))#取第一个分组里面的字符
    from common.basic_data import Context
    user=getattr(Context,key)
    print(user)
    s=re.sub(p,user,s,count=1)#count=1  找到就替换了
    print(s)