#!/usr/bin/env python
# -*- coding:utf-8-*-
#@author:蜜蜜
#@file: basic_data.py 
#@time: 2018/12/25 
#@email:1402686685@qq.com
# class Context:
#     normal_user=123#类变量
#     pwd=None#类变量
#
#     # def  __init__(self,normal_user):
#     #     self.normal_user=normal_user#成员变量
#
#     @staticmethod#类名调用，不需要实例就可以调用
#     @classmethod#类名或实例都可以调用
# if __name__ == '__main__':
#     c=Context(456)
#     print(c.normal_user)
import re

class DoRegex:
    @staticmethod
    def replace(target):
        pattern='\$\{(.*?)\}'
        while re.search(pattern, target):  # 找到一个就返回match
            m = re.search(pattern, target)
            key=m.group(1)  #取第一个分组里面的字符，也就是我们需要的key
            from common.basic_data import Context
            user = getattr(Context, key)
            target = re.sub(pattern, user, target, count=1)  # count=1  找到就替换了
        return target

from common.config import ConfigLoader
class Context:
    config= ConfigLoader()
    normal_user=123456#类变量
    pwd=None#类变量

    def __init__(self,a,b):
        self.a=a#成员变量需要实例调用
        self.b=b#成员变量需要实例调用

if __name__ == '__main__':
    #不需要实例 不需要Contest.直接用反射
    normal_user=getattr(Context,'normal_user')#获取变量的值
    print(normal_user)
    # setattr(Context,'admin_user','abc')
    # admin=getattr(Context,'admin_user')
    # print(admin)
    if hasattr(Context,'admin_user'):#判断是否有这个属性值
        delattr(Context,'admin_user')#删除属性值
    else:
        print('没这个属性，不执行删除')
    # print(admin)

