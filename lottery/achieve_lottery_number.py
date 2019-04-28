# -*- coding:utf-8 -*-
import requests
import xlwt
import xlrd
import os
import time
from lxml import etree
from xlutils.copy import copy

def achieve_lottery_number(aim_url):

    # 获取开奖信息
    response = requests.get(aim_url)
    html = etree.HTML(response.text, etree.HTMLParser())
    lottery_period = html.xpath('//*[@id="jrkj"]/li[1]/dl/dt/text()')
    lottery_time = html.xpath('//*[@id="jrkj"]/li[1]/dl/dd/text()')
    lottery_wan_bit = html.xpath('//*[@id="jrkj"]/li[1]/p/span[1]/text()')
    lottery_thousand_bit = html.xpath('//*[@id="jrkj"]/li[1]/p/span[2]/text()')
    lottery_hundred_bit = html.xpath('//*[@id="jrkj"]/li[1]/p/span[3]/text()')
    lottery_ten_bit = html.xpath('//*[@id="jrkj"]/li[1]/p/span[4]/text()')
    lottery_unit_bit = html.xpath('//*[@id="jrkj"]/li[1]/p/span[5]/text()')
    lottery_number = lottery_wan_bit[0] + lottery_thousand_bit[0] + lottery_hundred_bit[0] + lottery_ten_bit[0] + lottery_unit_bit[0]
    print("开奖时间: " + lottery_time[0] + "  开奖期数: " + lottery_period[0] + "  开奖号码: " + lottery_number)

    # 存储开奖信息
    current_year = time.strftime('%Y', time.localtime(time.time()))
    current_month = time.strftime('%m', time.localtime(time.time()))
    file_name = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    path_year = os.path.join(os.getcwd() + '/' + current_year)
    if not os.path.exists(path_year):
        os.makedirs(current_year)

    path_month = os.path.join(os.getcwd() + '/' + current_year + '/' + current_month)
    if not os.path.exists(path_month):
        os.makedirs(path_month)

    path_file = os.path.join(os.getcwd() + '/' + current_year + '/' + current_month + '/' + file_name + '.xls')
    if not os.path.exists(path_file):
        lottery_excel = xlwt.Workbook(encoding="utf-8", style_compression=0)
        lottery_sheet = lottery_excel.add_sheet(file_name)
        lottery_sheet.write(0, 0, label=r"开奖时间")
        lottery_sheet.write(0, 1, label=r"开奖期号")
        lottery_sheet.write(0, 2, label=r"万位")
        lottery_sheet.write(0, 3, label=r"千位")
        lottery_sheet.write(0, 4, label=r"百位")
        lottery_sheet.write(0, 5, label=r"十位")
        lottery_sheet.write(0, 6, label=r"个位")
        lottery_excel.save(path_file)
    else:
        lottery_excel_last = xlrd.open_workbook(path_file)
        lottery_excel_current = copy(lottery_excel_last)
        lottery_sheet_current = lottery_excel_current.get_sheet(0)
        current_row = lottery_excel_last.sheet_by_index(0).nrows
        lottery_sheet_current.write(current_row, 0, lottery_time[0])
        lottery_sheet_current.write(current_row, 1, lottery_period[0][1:-1])
        lottery_sheet_current.write(current_row, 2, lottery_wan_bit[0])
        lottery_sheet_current.write(current_row, 3, lottery_thousand_bit[0])
        lottery_sheet_current.write(current_row, 4, lottery_hundred_bit[0])
        lottery_sheet_current.write(current_row, 5, lottery_ten_bit[0])
        lottery_sheet_current.write(current_row, 6, lottery_unit_bit[0])
        lottery_excel_current.save(path_file)


if __name__ == "__main__":
    url = "https://m.ssqzj.com/kaijiang/cqssc/"
    achieve_lottery_number(url)

