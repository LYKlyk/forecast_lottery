import requests
import xlwt
import xlrd
import os
import json
import time
from lxml import etree
from xlutils.copy import copy


# 获取预测信息
def get_forecast_info_1():
    # 目标网址
    aim_big_small_url = "http://www.zhonghunwei.com/"
    aim_single_double_url = 'http://www.zhonghunwei.com/danshuang.html'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    # 预测通用信息
    response_big_small = requests.get(aim_big_small_url, headers=header)
    html_big_small = etree.HTML(response_big_small.text, etree.HTMLParser())
    response_single_double = requests.get(aim_single_double_url, headers=header)
    html_single_double = etree.HTML(response_single_double.text, etree.HTMLParser())

    lottery_last_period = html_big_small.xpath('//*[@id="plan_num_cur"]/text()')[0]
    lottery_hundred_number = html_big_small.xpath('//*[@id="kj_haoma"]/span[1]/text()')[0]
    lottery_ten_number = html_big_small.xpath('//*[@id="kj_haoma"]/span[2]/text()')[0]
    lottery_unit_number = html_big_small.xpath('//*[@id="kj_haoma"]/span[3]/text()')[0]

    # 大小预测
    lottery_big_small = html_big_small.xpath('//*[@id="jh_content"]/tbody/tr[1]/td[2]/text()')[0]
    # 单双预测
    lottery_single_double = html_single_double.xpath('//*[@id="jh_content"]/tbody/tr[1]/td[2]/text()')[0]


def get_forecast_info_2():
    # 目标网址
    aim_big_small_url = "http://www.sjfsh.com/"
    aim_single_double_url = 'http://www.sjfsh.com/danshuang.php'
    header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    # 预测通用信息
    response_big_small = requests.get(aim_big_small_url, headers=header)
    html_big_small = etree.HTML(response_big_small.text, etree.HTMLParser())
    response_single_double = requests.get(aim_single_double_url, headers=header)
    html_single_double = etree.HTML(response_single_double.text, etree.HTMLParser())

    lottery_last_period = html_big_small.xpath('/html/body/div[1]/div[2]/div[2]/p/span[1]/text()')[0]
    lottery_hundred_number = html_big_small.xpath('/html/body/div[1]/div[2]/div[2]/p/span[2]/text()')[0]
    lottery_ten_number = html_big_small.xpath('/html/body/div[1]/div[2]/div[2]/p/span[3]/text()')[0]
    lottery_unit_number = html_big_small.xpath('/html/body/div[1]/div[2]/div[2]/p/span[4]/text()')[0]

    # 大小预测
    lottery_big_small = html_big_small.xpath('//*[@id="jh_content"]/tbody/tr[1]/td[2]/text()')[0]
    # 单双预测
    lottery_single_double = html_single_double.xpath('//*[@id="jh_content"]/tbody/tr[1]/td[2]/text()')[0]


def get_forecast_info_3():
    # 目标网址
    aim_url = 'http://47.75.48.179:8090/index.php/index/index/shouye'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    payload_big_small = {'type': '9', 'playmethod': '1',  'jiekou': '1'}
    payload_single_double = {'type': '9', 'playmethod': '2',  'jiekou': '1'}

    # 预测通用信息
    response_big_small = requests.get(aim_url, params=payload_big_small, headers=header)
    json_big_small = response_big_small.json()
    response_single_double = requests.get(aim_url, params=payload_single_double, headers=header)
    json_single_double = response_single_double.json()
    lottery_last_period = json_big_small['TopGame']['gameid']
    lottery_hundred_number = json_big_small['TopGame']['R1']
    lottery_ten_number = json_big_small['TopGame']['R2']
    lottery_unit_number = json_big_small['TopGame']['R3']

    # 大小预测
    lottery_big_small = json_big_small['GameMultiple']['num']
    # 单双预测
    lottery_single_double = json_single_double['GameMultiple']['num']


if __name__ == '__main__':
    get_forecast_info_1()
    # get_forecast_info_2()
    # get_forecast_info_3()

