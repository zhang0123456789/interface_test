#!/usr/bin/env python
# -*- coding:utf-8-*-
#@author:蜜蜜
#@file: request.py 
#@time: 2018/12/18 
#@email:1402686685@qq.com
import requests
import json

class Request:
    def __init__(self,method,url,data=None,cookies=None,headers=None):
        try:
            if method=='get':
                self.resp=requests.get(url=url,params=data,cookies=cookies,headers=headers)
            elif method=='post':
                self.resp=requests.post(url=url, data=data, cookies=cookies, headers=headers)
            elif method=='delete':
                self.resp = requests.delete(url=url, data=data, cookies=cookies, headers=headers)
        except Exception as e:
            raise e

    def get_status_code(self):
        return  self.resp.status_code

    def get_text(self):
        return self.resp.text

    def get_json(self):
        json_dict=self.resp.json()
        # 通过json.dumps函数将字典转换成格式化后的字符串
        resp_text=json.dumps(json_dict,ensure_ascii=False,indent=4)
        print('response:',resp_text)#打印响应结果
        return self.resp.json()
    def get_cookies(self,key=None):#返回cookies
        return self.resp.cookies