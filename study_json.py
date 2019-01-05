#!/usr/bin/env python
# -*- coding:utf-8-*-
#@author:蜜蜜
#@file: study_json.py
#@time: 2018/12/18
#@email:1402686685@qq.com
import json
#eval函数不能自动的识别null 转化为None
#json字符串和dict之间的转化，推荐大家优先使用json
#json序列号与反序列化
#序列化--将dict序列化为str或者file  dumps(str),dump(file)
#反序列化--将str或者file反序列化为dict  loads(),load()

#loads()将包含str类型的JSON文档 ，反序列化为一个python对象
#load()将一个包含JSON格式数据的刻度文件反序列化为一个python对象
# str_test='{"status":0,"code":"20111","data":null}'
# print(type(str_test))
# dict_test=json.loads(str_test)
# print(dict_test['data'])
# print(type(dict_test))

#标准的字符串，包含1、字典必须是{}串起来，2、里面的key必须“”引起来
# str_2='{"a":[1,2,("c","d")]}'
# dict_test=json.loads(str_2)
# print(dict_test)


#一个Python数据结构转换为JSON 字符串
# dict_obj={"status":0,"code":"20111","data":None,"msg":"用户名或密码错误"}
# str_obj=json.dumps(dict_obj,ensure_ascii=False,indent=4)
# print(str_obj)

#一个Python数据结构转换为JSON 字符串
# person = { 'name': 'ACME','sex': 'male',  'height': 100, 'price': 542.23, 'hobby': 'sing'}
# json_str=json.dumps(person,indent=4)
# print(json_str)
# print(type(json_str))


'''dump的功能就是把Python对象encode为json对象，一个编码过程。
注意json模块提供了json.dumps和json.dump方法，
#区别是dump直接到文件，而dumps到一个字符串，
这里的s可以理解为string。'''


#用json.dumps把python格式，序列化为json字符串格式
import json
# dic={'Connection': ['keep-alive'], 'Host': ['127.0.0.1:5000'], 'Cache-Control': ['max-age=0']}
# print(type(dic))  #字典
# jdict= json.dumps({'Connection': ['keep-alive'], 'Host': ['127.0.0.1:5000'], 'Cache-Control': ['max-age=0']})
# print (jdict)#打印出    {"Connection": ["keep-alive"], "Host": ["127.0.0.1:5000"], "Cache-Control": ["max-age=0"]}
# print(type(jdict))  #字符串


#可以用json.dumps序列化列表为json字符串格式
# list = [1, 4, 3, 2, 5]
# print(type(list))
# jlist = json.dumps(list)
# print (jlist)#打印出[1, 4, 3, 2, 5]
# print(type(jlist))

'''json.dump
不仅可以把Python对象编码为string，还可以写入文件。
因为我们不能把Python对象直接写入文件，
这样会报错TypeError: expected a string or other character buffer object
，我们需要将其序列化之后才可以。'''
data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
with open('output.json','w') as fp:
    json.dump(data,fp)

#将一个JSON字典转换为一个Python对象
# class JsonObject:
#     def __init__(self, d):
#         self.__dict__ = d
#
#
# if __name__ == '__main__':
#     s = '{"name": "ACME", "shares": 50, "price": 490.1}'
#     person = json.loads(s, object_hook=JsonObject)
#
#     print(person.name, person.price)
#     print(person)
