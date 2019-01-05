#!/usr/bin/env python
# -*- coding:utf-8-*-
#@author:蜜蜜
#@file: test_recharge.py 
#@time: 2018/12/25 
#@email:1402686685@qq.com
import unittest
import json
from common.do_execl import DoExecl
from common.basic_data import DoRegex,Context
from common.mysql_util import MysqlUtil
from common import contants
from common.request import Request
from ddt import ddt,data

do_execl = DoExecl(contants.cases_file)  # 实例化为一个DoExecl对象
cases = do_execl.get_cases('recharge')

@ddt
class TestRecharge(unittest.TestCase):
    def setUp(self):
        # 充值前账户余额记录
        self.mysql = MysqlUtil()
        # 查询投资用户的账户信息
        self.sql = 'select * from future.member where mobilephone = {0}'.format(Context.normal_user)
        self.before_amount = self.mysql.fetch_one(self.sql)['LeaveAmount']  # 账户余额
        print("充值前的金额", self.before_amount)

    @data(*cases)
    def test_recharge(self, case):
        # 参数化处理
        data = DoRegex.replace(case.data)
        # 将字符串序列化成字典
        data = json.loads(data)
        if hasattr(Context, 'cookies'):  # 判断是否有cookies
            cookies = getattr(Context, 'cookies')  # 获取放到上下文里面的cookies
        else:
            cookies = None
        resp = Request(method=case.method, url=case.url, data=data, cookies=cookies)  # 通过封装的Request类来完成接口的调用
        # 判断有没有cookie
        if resp.get_cookies():  # 判断返回里面是否有cookies
            setattr(Context, 'cookies', resp.get_cookies())  # 放入到上下文中
        resp_dict = resp.get_json()  # 获取请求响应，字典
        self.assertEqual(case.expected, int(resp_dict['code']))  # 判断响应返回的code 是否与期望结果一致

        actual = self.mysql.fetch_one(self.sql)['LeaveAmount']  # 再次获取账户余额
        print("测试{0}后的金额".format(case.title), actual)
        # 充值成功，判断余额增加
        if resp_dict['code'] == '10001' and resp_dict['msg'] == "充值成功":
            amount = float(data['amount'])  # 充值金额
            print('充值金额', amount)
            expect = float(self.before_amount) + amount  # 充值成功，期望的账户余额= 原来余额 + 充值金额
            self.assertEqual(expect, actual)  # 判断期望结果与实际结果是否一致
        elif resp_dict['code'] != '10001':
            expect = self.before_amount  # 充值失败，期望结果：余额未增加
            self.assertEqual(expect, actual)  # 判断期望结果与实际结果是否一致

    def tearDown(self):
        self.mysql.close()

