import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QLineEdit, QPushButton, QRadioButton, QButtonGroup
from PyQt5.QtCore import *


class ForecastDigit(QMainWindow):

    def __init__(self):
        super().__init__()

        # 开奖号码部分
        # 标签部分
        self.label_lottery_number = QLabel(r'开奖号码', self)
        self.label_lottery_wan = QLabel(r'万位', self)
        self.label_lottery_thousand = QLabel(r'千位', self)
        self.label_lottery_hundred = QLabel(r'百位', self)
        self.label_lottery_ten = QLabel(r'十位', self)
        self.label_lottery_unit = QLabel(r'个位', self)
        # 输入文本框部分
        self.lineEdit_lottery_wan = QLineEdit(self)
        self.lineEdit_lottery_thousand = QLineEdit(self)
        self.lineEdit_lottery_hundred = QLineEdit(self)
        self.lineEdit_lottery_ten = QLineEdit(self)
        self.lineEdit_lottery_unit = QLineEdit(self)
        # 获取开奖号码按钮部分
        self.pushButton_get_lottery_number = QPushButton(r'获取开奖号码', self)

        # 预测号码部分
        # 预测位数标签
        self.label_forecast_wan = QLabel(r'万位号码', self)
        self.label_forecast_thousand = QLabel(r'千位号码', self)
        self.label_forecast_hundred = QLabel(r'百位号码', self)
        self.label_forecast_ten = QLabel(r'十位号码', self)
        self.label_forecast_unit = QLabel(r'个位号码', self)
        # 预测位数准确率
        self.label_forecast_wan_rate = QLabel(r'万位概率', self)
        self.label_forecast_thousand_rate = QLabel(r'千位概率', self)
        self.label_forecast_hundred_rate = QLabel(r'百位概率', self)
        self.label_forecast_ten_rate = QLabel(r'十位概率', self)
        self.label_forecast_unit_rate = QLabel(r'个位概率', self)
        # 预测号码的输入文本框
        # 万位预测号码
        self.lineEdit_forecast_wan_first = QLineEdit(self)
        self.lineEdit_forecast_wan_second = QLineEdit(self)
        self.lineEdit_forecast_wan_third = QLineEdit(self)
        self.lineEdit_forecast_wan_fourth = QLineEdit(self)
        self.lineEdit_forecast_wan_fifth = QLineEdit(self)
        self.lineEdit_forecast_wan_sixth = QLineEdit(self)
        self.lineEdit_forecast_wan_seventh = QLineEdit(self)
        self.lineEdit_forecast_wan_eighth = QLineEdit(self)
        self.lineEdit_forecast_wan_ninth = QLineEdit(self)
        self.lineEdit_forecast_wan_tenth = QLineEdit(self)
        # 千位预测号码
        self.lineEdit_forecast_thousand_first = QLineEdit(self)
        self.lineEdit_forecast_thousand_second = QLineEdit(self)
        self.lineEdit_forecast_thousand_third = QLineEdit(self)
        self.lineEdit_forecast_thousand_fourth = QLineEdit(self)
        self.lineEdit_forecast_thousand_fifth = QLineEdit(self)
        self.lineEdit_forecast_thousand_sixth = QLineEdit(self)
        self.lineEdit_forecast_thousand_seventh = QLineEdit(self)
        self.lineEdit_forecast_thousand_eighth = QLineEdit(self)
        self.lineEdit_forecast_thousand_ninth = QLineEdit(self)
        self.lineEdit_forecast_thousand_tenth = QLineEdit(self)
        # 百位预测号码
        self.lineEdit_forecast_hundred_first = QLineEdit(self)
        self.lineEdit_forecast_hundred_second = QLineEdit(self)
        self.lineEdit_forecast_hundred_third = QLineEdit(self)
        self.lineEdit_forecast_hundred_fourth = QLineEdit(self)
        self.lineEdit_forecast_hundred_fifth = QLineEdit(self)
        self.lineEdit_forecast_hundred_sixth = QLineEdit(self)
        self.lineEdit_forecast_hundred_seventh = QLineEdit(self)
        self.lineEdit_forecast_hundred_eighth = QLineEdit(self)
        self.lineEdit_forecast_hundred_ninth = QLineEdit(self)
        self.lineEdit_forecast_hundred_tenth = QLineEdit(self)
        # 十位预测号码
        self.lineEdit_forecast_ten_first = QLineEdit(self)
        self.lineEdit_forecast_ten_second = QLineEdit(self)
        self.lineEdit_forecast_ten_third = QLineEdit(self)
        self.lineEdit_forecast_ten_fourth = QLineEdit(self)
        self.lineEdit_forecast_ten_fifth = QLineEdit(self)
        self.lineEdit_forecast_ten_sixth = QLineEdit(self)
        self.lineEdit_forecast_ten_seventh = QLineEdit(self)
        self.lineEdit_forecast_ten_eighth = QLineEdit(self)
        self.lineEdit_forecast_ten_ninth = QLineEdit(self)
        self.lineEdit_forecast_ten_tenth = QLineEdit(self)
        # 个位预测号码
        self.lineEdit_forecast_unit_first = QLineEdit(self)
        self.lineEdit_forecast_unit_second = QLineEdit(self)
        self.lineEdit_forecast_unit_third = QLineEdit(self)
        self.lineEdit_forecast_unit_fourth = QLineEdit(self)
        self.lineEdit_forecast_unit_fifth = QLineEdit(self)
        self.lineEdit_forecast_unit_sixth = QLineEdit(self)
        self.lineEdit_forecast_unit_seventh = QLineEdit(self)
        self.lineEdit_forecast_unit_eighth = QLineEdit(self)
        self.lineEdit_forecast_unit_ninth = QLineEdit(self)
        self.lineEdit_forecast_unit_tenth = QLineEdit(self)
        # 预测准确率的输入文本框
        # 万位预测号码
        self.lineEdit_forecast_wan_first_ratio = QLineEdit(self)
        self.lineEdit_forecast_wan_second_ratio = QLineEdit(self)
        self.lineEdit_forecast_wan_third_ratio = QLineEdit(self)
        self.lineEdit_forecast_wan_fourth_ratio = QLineEdit(self)
        self.lineEdit_forecast_wan_fifth_ratio = QLineEdit(self)
        self.lineEdit_forecast_wan_sixth_ratio = QLineEdit(self)
        self.lineEdit_forecast_wan_seventh_ratio = QLineEdit(self)
        self.lineEdit_forecast_wan_eighth_ratio = QLineEdit(self)
        self.lineEdit_forecast_wan_ninth_ratio = QLineEdit(self)
        self.lineEdit_forecast_wan_tenth_ratio = QLineEdit(self)
        # 千位预测号码
        self.lineEdit_forecast_thousand_first_ratio = QLineEdit(self)
        self.lineEdit_forecast_thousand_second_ratio = QLineEdit(self)
        self.lineEdit_forecast_thousand_third_ratio = QLineEdit(self)
        self.lineEdit_forecast_thousand_fourth_ratio = QLineEdit(self)
        self.lineEdit_forecast_thousand_fifth_ratio = QLineEdit(self)
        self.lineEdit_forecast_thousand_sixth_ratio = QLineEdit(self)
        self.lineEdit_forecast_thousand_seventh_ratio = QLineEdit(self)
        self.lineEdit_forecast_thousand_eighth_ratio = QLineEdit(self)
        self.lineEdit_forecast_thousand_ninth_ratio = QLineEdit(self)
        self.lineEdit_forecast_thousand_tenth_ratio = QLineEdit(self)
        # 百位预测号码
        self.lineEdit_forecast_hundred_first_ratio = QLineEdit(self)
        self.lineEdit_forecast_hundred_second_ratio = QLineEdit(self)
        self.lineEdit_forecast_hundred_third_ratio = QLineEdit(self)
        self.lineEdit_forecast_hundred_fourth_ratio = QLineEdit(self)
        self.lineEdit_forecast_hundred_fifth_ratio = QLineEdit(self)
        self.lineEdit_forecast_hundred_sixth_ratio = QLineEdit(self)
        self.lineEdit_forecast_hundred_seventh_ratio = QLineEdit(self)
        self.lineEdit_forecast_hundred_eighth_ratio = QLineEdit(self)
        self.lineEdit_forecast_hundred_ninth_ratio = QLineEdit(self)
        self.lineEdit_forecast_hundred_tenth_ratio = QLineEdit(self)
        # 十位预测号码
        self.lineEdit_forecast_ten_first_ratio = QLineEdit(self)
        self.lineEdit_forecast_ten_second_ratio = QLineEdit(self)
        self.lineEdit_forecast_ten_third_ratio = QLineEdit(self)
        self.lineEdit_forecast_ten_fourth_ratio = QLineEdit(self)
        self.lineEdit_forecast_ten_fifth_ratio = QLineEdit(self)
        self.lineEdit_forecast_ten_sixth_ratio = QLineEdit(self)
        self.lineEdit_forecast_ten_seventh_ratio = QLineEdit(self)
        self.lineEdit_forecast_ten_eighth_ratio = QLineEdit(self)
        self.lineEdit_forecast_ten_ninth_ratio = QLineEdit(self)
        self.lineEdit_forecast_ten_tenth_ratio = QLineEdit(self)
        # 个位预测号码
        self.lineEdit_forecast_unit_first_ratio = QLineEdit(self)
        self.lineEdit_forecast_unit_second_ratio = QLineEdit(self)
        self.lineEdit_forecast_unit_third_ratio = QLineEdit(self)
        self.lineEdit_forecast_unit_fourth_ratio = QLineEdit(self)
        self.lineEdit_forecast_unit_fifth_ratio = QLineEdit(self)
        self.lineEdit_forecast_unit_sixth_ratio = QLineEdit(self)
        self.lineEdit_forecast_unit_seventh_ratio = QLineEdit(self)
        self.lineEdit_forecast_unit_eighth_ratio = QLineEdit(self)
        self.lineEdit_forecast_unit_ninth_ratio = QLineEdit(self)
        self.lineEdit_forecast_unit_tenth_ratio = QLineEdit(self)
        # 预测号码按钮
        self.pushButton_forecast_number = QPushButton(r'预测开奖号码', self)

        # 在线投注部分
        # 标签部分
        self.label_website = QLabel(r'购彩网址', self)
        self.label_user_name = QLabel(r'用户名', self)
        self.label_user_password = QLabel(r'密码', self)
        self.label_start_money = QLabel(r'初始资金', self)
        self.label_stop_money = QLabel(r'止损金额', self)
        self.label_current_lottery_time = QLabel(r'当前投注倍数', self)
        self.label_current_lottery_money = QLabel(r'当前投注金额', self)
        self.label_history_max_wrong_time = QLabel(r'最大错误次数', self)
        self.label_history_max_lottery_money = QLabel(r'最大投注金额', self)
        self.label_profit_money = QLabel(r'当前盈利金额', self)

        self.label_lottery_bet_mode = QLabel(r'投注模式', self)
        self.label_lottery_risk_mode = QLabel(r'风险模式', self)
        self.label_lottery_follow_mode = QLabel(r'跟号模式', self)
        self.label_lottery_buy_number_mode = QLabel(r'购号模式', self)

        # 输入文本框
        self.lineEdit_website = QLineEdit(self)
        self.lineEdit_user_name = QLineEdit(self)
        self.lineEdit_user_password = QLineEdit(self)
        self.lineEdit_start_money = QLineEdit(self)
        self.lineEdit_stop_money = QLineEdit(self)
        self.lineEdit_current_lottery_time = QLineEdit(self)
        self.lineEdit_current_lottery_money = QLineEdit(self)
        self.lineEdit_history_max_wrong_time = QLineEdit(self)
        self.lineEdit_history_max_lottery_money = QLineEdit(self)
        self.lineEdit_profit_money = QLineEdit(self)

        # 投注模式
        self.buttonGroup_buy_unit = QButtonGroup(self)
        self.radioButton_buy_yuan = QRadioButton(r'元', self)
        self.buttonGroup_buy_unit.addButton(self.radioButton_buy_yuan, 11)
        self.radioButton_buy_corner = QRadioButton(r'角', self)
        self.buttonGroup_buy_unit.addButton(self.radioButton_buy_corner, 12)
        self.radioButton_buy_cent = QRadioButton(r'分', self)
        self.buttonGroup_buy_unit.addButton(self.radioButton_buy_cent, 13)

        # 风险模式
        self.buttonGroup_risk = QButtonGroup(self)
        self.radioButton_low_risk = QRadioButton(r'低风险投资模式', self)
        self.buttonGroup_risk.addButton(self.radioButton_low_risk, 21)
        self.radioButton_medium_risk = QRadioButton(r'中风险投资模式', self)
        self.buttonGroup_risk.addButton(self.radioButton_medium_risk, 22)
        self.radioButton_high_risk = QRadioButton(r'高风险投资模式', self)
        self.buttonGroup_risk.addButton(self.radioButton_high_risk, 23)

        # 预测号码的个数
        self.buttonGroup_forecast_bit = QButtonGroup(self)
        self.radioButton_forecast_four_bit = QRadioButton(r'四码', self)
        self.buttonGroup_forecast_bit.addButton(self.radioButton_forecast_four_bit, 31)
        self.radioButton_forecast_five_bit = QRadioButton(r'五码', self)
        self.buttonGroup_forecast_bit.addButton(self.radioButton_forecast_five_bit, 32)
        self.radioButton_forecast_six_bit = QRadioButton(r'六码', self)
        self.buttonGroup_forecast_bit.addButton(self.radioButton_forecast_six_bit, 33)
        self.radioButton_forecast_seven_bit = QRadioButton(r'七码', self)
        self.buttonGroup_forecast_bit.addButton(self.radioButton_forecast_seven_bit, 34)
        # 追号期数
        self.buttonGroup_forecast_period = QButtonGroup(self)
        self.radioButton_forecast_one_period = QRadioButton(r'一期', self)
        self.buttonGroup_forecast_period.addButton(self.radioButton_forecast_one_period, 41)
        self.radioButton_forecast_two_period = QRadioButton(r'二期', self)
        self.buttonGroup_forecast_period.addButton(self.radioButton_forecast_two_period, 42)
        self.radioButton_forecast_three_period = QRadioButton(r'三期', self)
        self.buttonGroup_forecast_period.addButton(self.radioButton_forecast_three_period, 43)
        self.radioButton_forecast_four_period = QRadioButton(r'四期', self)
        self.buttonGroup_forecast_period.addButton(self.radioButton_forecast_four_period, 44)
        self.radioButton_forecast_five_period = QRadioButton(r'五期', self)
        self.buttonGroup_forecast_period.addButton(self.radioButton_forecast_five_period, 45)
        # 在线投注按钮
        self.pushButton_purchase_lottery = QPushButton(r'自动在线投注', self)

        # 初始化界面
        self.initialize()

    def initialize(self):
        # 开奖号码部分
        self.label_lottery_number.setFixedSize(60, 25)
        self.label_lottery_number.move(10, 5)
        self.label_lottery_wan.setFixedSize(50, 25)
        self.label_lottery_wan.move(80, 5)
        self.label_lottery_wan.setAlignment(Qt.AlignCenter)
        self.label_lottery_thousand.setFixedSize(50, 25)
        self.label_lottery_thousand.move(200, 5)
        self.label_lottery_thousand.setAlignment(Qt.AlignCenter)
        self.label_lottery_hundred.setFixedSize(50, 25)
        self.label_lottery_hundred.move(320, 5)
        self.label_lottery_hundred.setAlignment(Qt.AlignCenter)
        self.label_lottery_ten.setFixedSize(50, 25)
        self.label_lottery_ten.move(440, 5)
        self.label_lottery_ten.setAlignment(Qt.AlignCenter)
        self.label_lottery_unit.setFixedSize(50, 25)
        self.label_lottery_unit.move(560, 5)
        self.label_lottery_unit.setAlignment(Qt.AlignCenter)

        self.lineEdit_lottery_wan.setFixedSize(50, 25)
        self.lineEdit_lottery_wan.move(140, 5)
        self.lineEdit_lottery_thousand.setFixedSize(50, 25)
        self.lineEdit_lottery_thousand.move(260, 5)
        self.lineEdit_lottery_hundred.setFixedSize(50, 25)
        self.lineEdit_lottery_hundred.move(380, 5)
        self.lineEdit_lottery_ten.setFixedSize(50, 25)
        self.lineEdit_lottery_ten.move(500, 5)
        self.lineEdit_lottery_unit.setFixedSize(50, 25)
        self.lineEdit_lottery_unit.move(620, 5)

        # 获取开奖号码
        self.pushButton_get_lottery_number.setFixedSize(110, 25)
        self.pushButton_get_lottery_number.move(290, 35)
        # 预测号码部分

        # 万位部分
        # 预测号码部分
        self.label_forecast_wan.setFixedSize(60, 25)
        self.label_forecast_wan.move(10, 65)
        self.lineEdit_forecast_wan_first.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_first.move(80, 65)
        self.lineEdit_forecast_wan_second.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_second.move(140, 65)
        self.lineEdit_forecast_wan_third.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_third.move(200, 65)
        self.lineEdit_forecast_wan_fourth.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_fourth.move(260, 65)
        self.lineEdit_forecast_wan_fifth.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_fifth.move(320, 65)
        self.lineEdit_forecast_wan_sixth.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_sixth.move(380, 65)
        self.lineEdit_forecast_wan_seventh.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_seventh.move(440, 65)
        self.lineEdit_forecast_wan_eighth.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_eighth.move(500, 65)
        self.lineEdit_forecast_wan_ninth.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_ninth.move(560, 65)
        self.lineEdit_forecast_wan_tenth.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_tenth.move(620, 65)
        # 预测概率部分
        self.label_forecast_wan_rate.setFixedSize(60, 25)
        self.label_forecast_wan_rate.move(10, 95)
        self.lineEdit_forecast_wan_first_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_first_ratio.move(80, 95)
        self.lineEdit_forecast_wan_second_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_second_ratio.move(140, 95)
        self.lineEdit_forecast_wan_third_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_third_ratio.move(200, 95)
        self.lineEdit_forecast_wan_fourth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_fourth_ratio.move(260, 95)
        self.lineEdit_forecast_wan_fifth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_fifth_ratio.move(320, 95)
        self.lineEdit_forecast_wan_sixth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_sixth_ratio.move(380, 95)
        self.lineEdit_forecast_wan_seventh_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_seventh_ratio.move(440, 95)
        self.lineEdit_forecast_wan_eighth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_eighth_ratio.move(500, 95)
        self.lineEdit_forecast_wan_ninth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_ninth_ratio.move(560, 95)
        self.lineEdit_forecast_wan_tenth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_tenth_ratio.move(620, 95)

        # 千位部分
        # 预测号码部分
        self.label_forecast_thousand.setFixedSize(60, 25)
        self.label_forecast_thousand.move(10, 125)
        self.lineEdit_forecast_thousand_first.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_first.move(80, 125)
        self.lineEdit_forecast_thousand_second.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_second.move(140, 125)
        self.lineEdit_forecast_thousand_third.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_third.move(200, 125)
        self.lineEdit_forecast_thousand_fourth.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_fourth.move(260, 125)
        self.lineEdit_forecast_thousand_fifth.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_fifth.move(320, 125)
        self.lineEdit_forecast_thousand_sixth.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_sixth.move(380, 125)
        self.lineEdit_forecast_thousand_seventh.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_seventh.move(440, 125)
        self.lineEdit_forecast_thousand_eighth.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_eighth.move(500, 125)
        self.lineEdit_forecast_thousand_ninth.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_ninth.move(560, 125)
        self.lineEdit_forecast_thousand_tenth.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_tenth.move(620, 125)
        # 预测概率部分
        self.label_forecast_thousand_rate.setFixedSize(60, 25)
        self.label_forecast_thousand_rate.move(10, 155)
        self.lineEdit_forecast_thousand_first_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_first_ratio.move(80, 155)
        self.lineEdit_forecast_thousand_second_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_second_ratio.move(140, 155)
        self.lineEdit_forecast_thousand_third_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_third_ratio.move(200, 155)
        self.lineEdit_forecast_thousand_fourth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_fourth_ratio.move(260, 155)
        self.lineEdit_forecast_thousand_fifth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_fifth_ratio.move(320, 155)
        self.lineEdit_forecast_thousand_sixth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_sixth_ratio.move(380, 155)
        self.lineEdit_forecast_thousand_seventh_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_seventh_ratio.move(440, 155)
        self.lineEdit_forecast_thousand_eighth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_eighth_ratio.move(500, 155)
        self.lineEdit_forecast_thousand_ninth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_ninth_ratio.move(560, 155)
        self.lineEdit_forecast_thousand_tenth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_tenth_ratio.move(620, 155)

        # 百位部分
        # 预测号码部分
        self.label_forecast_hundred.setFixedSize(60, 25)
        self.label_forecast_hundred.move(10, 185)
        self.lineEdit_forecast_hundred_first.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_first.move(80, 185)
        self.lineEdit_forecast_hundred_second.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_second.move(140, 185)
        self.lineEdit_forecast_hundred_third.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_third.move(200, 185)
        self.lineEdit_forecast_hundred_fourth.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_fourth.move(260, 185)
        self.lineEdit_forecast_hundred_fifth.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_fifth.move(320, 185)
        self.lineEdit_forecast_hundred_sixth.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_sixth.move(380, 185)
        self.lineEdit_forecast_hundred_seventh.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_seventh.move(440, 185)
        self.lineEdit_forecast_hundred_eighth.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_eighth.move(500, 185)
        self.lineEdit_forecast_hundred_ninth.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_ninth.move(560, 185)
        self.lineEdit_forecast_hundred_tenth.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_tenth.move(620, 185)
        # 预测概率部分
        self.label_forecast_hundred_rate.setFixedSize(60, 25)
        self.label_forecast_hundred_rate.move(10, 215)
        self.lineEdit_forecast_hundred_first_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_first_ratio.move(80, 215)
        self.lineEdit_forecast_hundred_second_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_second_ratio.move(140, 215)
        self.lineEdit_forecast_hundred_third_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_third_ratio.move(200, 215)
        self.lineEdit_forecast_hundred_fourth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_fourth_ratio.move(260, 215)
        self.lineEdit_forecast_hundred_fifth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_fifth_ratio.move(320, 215)
        self.lineEdit_forecast_hundred_sixth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_sixth_ratio.move(380, 215)
        self.lineEdit_forecast_hundred_seventh_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_seventh_ratio.move(440, 215)
        self.lineEdit_forecast_hundred_eighth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_eighth_ratio.move(500, 215)
        self.lineEdit_forecast_hundred_ninth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_ninth_ratio.move(560, 215)
        self.lineEdit_forecast_hundred_tenth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_tenth_ratio.move(620, 215)

        # 十位部分
        # 预测号码部分
        self.label_forecast_ten.setFixedSize(60, 25)
        self.label_forecast_ten.move(10, 245)
        self.lineEdit_forecast_ten_first.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_first.move(80, 245)
        self.lineEdit_forecast_ten_second.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_second.move(140, 245)
        self.lineEdit_forecast_ten_third.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_third.move(200, 245)
        self.lineEdit_forecast_ten_fourth.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_fourth.move(260, 245)
        self.lineEdit_forecast_ten_fifth.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_fifth.move(320, 245)
        self.lineEdit_forecast_ten_sixth.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_sixth.move(380, 245)
        self.lineEdit_forecast_ten_seventh.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_seventh.move(440, 245)
        self.lineEdit_forecast_ten_eighth.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_eighth.move(500, 245)
        self.lineEdit_forecast_ten_ninth.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_ninth.move(560, 245)
        self.lineEdit_forecast_ten_tenth.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_tenth.move(620, 245)
        # 预测概率部分
        self.label_forecast_ten_rate.setFixedSize(60, 25)
        self.label_forecast_ten_rate.move(10, 275)
        self.lineEdit_forecast_ten_first_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_first_ratio.move(80, 275)
        self.lineEdit_forecast_ten_second_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_second_ratio.move(140, 275)
        self.lineEdit_forecast_ten_third_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_third_ratio.move(200, 275)
        self.lineEdit_forecast_ten_fourth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_fourth_ratio.move(260, 275)
        self.lineEdit_forecast_ten_fifth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_fifth_ratio.move(320, 275)
        self.lineEdit_forecast_ten_sixth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_sixth_ratio.move(380, 275)
        self.lineEdit_forecast_ten_seventh_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_seventh_ratio.move(440, 275)
        self.lineEdit_forecast_ten_eighth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_eighth_ratio.move(500, 275)
        self.lineEdit_forecast_ten_ninth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_ninth_ratio.move(560, 275)
        self.lineEdit_forecast_ten_tenth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_tenth_ratio.move(620, 275)

        # 个位部分
        # 预测号码部分
        self.label_forecast_unit.setFixedSize(60, 25)
        self.label_forecast_unit.move(10, 305)
        self.lineEdit_forecast_unit_first.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_first.move(80, 305)
        self.lineEdit_forecast_unit_second.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_second.move(140, 305)
        self.lineEdit_forecast_unit_third.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_third.move(200, 305)
        self.lineEdit_forecast_unit_fourth.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_fourth.move(260, 305)
        self.lineEdit_forecast_unit_fifth.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_fifth.move(320, 305)
        self.lineEdit_forecast_unit_sixth.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_sixth.move(380, 305)
        self.lineEdit_forecast_unit_seventh.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_seventh.move(440, 305)
        self.lineEdit_forecast_unit_eighth.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_eighth.move(500, 305)
        self.lineEdit_forecast_unit_ninth.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_ninth.move(560, 305)
        self.lineEdit_forecast_unit_tenth.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_tenth.move(620, 305)
        # 预测概率部分
        self.label_forecast_unit_rate.setFixedSize(60, 25)
        self.label_forecast_unit_rate.move(10, 335)
        self.lineEdit_forecast_unit_first_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_first_ratio.move(80, 335)
        self.lineEdit_forecast_unit_second_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_second_ratio.move(140, 335)
        self.lineEdit_forecast_unit_third_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_third_ratio.move(200, 335)
        self.lineEdit_forecast_unit_fourth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_fourth_ratio.move(260, 335)
        self.lineEdit_forecast_unit_fifth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_fifth_ratio.move(320, 335)
        self.lineEdit_forecast_unit_sixth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_sixth_ratio.move(380, 335)
        self.lineEdit_forecast_unit_seventh_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_seventh_ratio.move(440, 335)
        self.lineEdit_forecast_unit_eighth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_eighth_ratio.move(500, 335)
        self.lineEdit_forecast_unit_ninth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_ninth_ratio.move(560, 335)
        self.lineEdit_forecast_unit_tenth_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_tenth_ratio.move(620, 335)

        self.pushButton_forecast_number.setFixedSize(110, 25)
        self.pushButton_forecast_number.move(290, 365)

        # 在线投注部分
        # 设置用户信息与购买信息
        self.label_website.setFixedSize(60, 25)
        self.label_website.move(10, 395)
        self.lineEdit_website.setFixedSize(110, 25)
        self.lineEdit_website.move(80, 395)
        self.label_user_name.setFixedSize(50, 25)
        self.label_user_name.move(200, 395)
        self.label_user_name.setAlignment(Qt.AlignCenter)
        self.lineEdit_user_name.setFixedSize(50, 25)
        self.lineEdit_user_name.move(260, 395)
        self.label_user_password.setFixedSize(50, 25)
        self.label_user_password.move(320, 395)
        self.label_user_password.setAlignment(Qt.AlignCenter)
        self.lineEdit_user_password.setFixedSize(50, 25)
        self.lineEdit_user_password.move(380, 395)
        self.label_start_money.setFixedSize(50, 25)
        self.label_start_money.move(440, 395)
        self.label_start_money.setAlignment(Qt.AlignCenter)
        self.lineEdit_start_money.setFixedSize(50, 25)
        self.lineEdit_start_money.move(500, 395)
        self.label_stop_money.setFixedSize(50, 25)
        self.label_stop_money.move(560, 395)
        self.label_stop_money.setAlignment(Qt.AlignCenter)
        self.lineEdit_stop_money.setFixedSize(50, 25)
        self.lineEdit_stop_money.move(620, 395)

        # 显示投注信息
        self.label_current_lottery_time.setFixedSize(80, 25)
        self.label_current_lottery_time.move(10, 425)
        self.lineEdit_current_lottery_time.setFixedSize(40, 25)
        self.lineEdit_current_lottery_time.move(90, 425)
        self.label_current_lottery_money.setFixedSize(80, 25)
        self.label_current_lottery_money.move(140, 425)
        self.lineEdit_current_lottery_money.setFixedSize(40, 25)
        self.lineEdit_current_lottery_money.move(220, 425)
        self.label_history_max_wrong_time.setFixedSize(80, 25)
        self.label_history_max_wrong_time.move(270, 425)
        self.lineEdit_history_max_wrong_time.setFixedSize(40, 25)
        self.lineEdit_history_max_wrong_time.move(350, 425)
        self.label_history_max_lottery_money.setFixedSize(80, 25)
        self.label_history_max_lottery_money.move(400, 425)
        self.lineEdit_history_max_lottery_money.setFixedSize(40, 25)
        self.lineEdit_history_max_lottery_money.move(480, 425)
        self.label_profit_money.setFixedSize(80, 25)
        self.label_profit_money.move(530, 425)
        self.lineEdit_profit_money.setFixedSize(40, 25)
        self.lineEdit_profit_money.move(610, 425)

        # 设置用户购买方式
        self.label_lottery_bet_mode.setFixedSize(60, 25)
        self.label_lottery_bet_mode.move(10, 455)
        self.radioButton_buy_yuan.setFixedSize(50, 25)
        self.radioButton_buy_yuan.move(80, 455)
        self.radioButton_buy_corner.setFixedSize(50, 25)
        self.radioButton_buy_corner.move(140, 455)
        self.radioButton_buy_cent.setFixedSize(50, 25)
        self.radioButton_buy_cent.move(200, 455)
        self.label_lottery_risk_mode.setFixedSize(60, 25)
        self.label_lottery_risk_mode.move(260, 455)
        self.radioButton_low_risk.setFixedSize(110, 25)
        self.radioButton_low_risk.move(320, 455)
        self.radioButton_medium_risk.setFixedSize(110, 25)
        self.radioButton_medium_risk.move(440, 455)
        self.radioButton_high_risk.setFixedSize(110, 25)
        self.radioButton_high_risk.move(560, 455)

        self.label_lottery_buy_number_mode.setFixedSize(60, 25)
        self.label_lottery_buy_number_mode.move(10, 485)
        self.radioButton_forecast_four_bit.setFixedSize(50, 25)
        self.radioButton_forecast_four_bit.move(80, 485)
        self.radioButton_forecast_five_bit.setFixedSize(50, 25)
        self.radioButton_forecast_five_bit.move(140, 485)
        self.radioButton_forecast_six_bit.setFixedSize(50, 25)
        self.radioButton_forecast_six_bit.move(200, 485)
        self.radioButton_forecast_seven_bit.setFixedSize(50, 25)
        self.radioButton_forecast_seven_bit.move(260, 485)
        self.label_lottery_follow_mode.setFixedSize(50, 25)
        self.label_lottery_follow_mode.move(320, 485)
        self.radioButton_forecast_one_period.setFixedSize(50, 25)
        self.radioButton_forecast_one_period.move(380, 485)
        self.radioButton_forecast_two_period.setFixedSize(50, 25)
        self.radioButton_forecast_two_period.move(440, 485)
        self.radioButton_forecast_three_period.setFixedSize(50, 25)
        self.radioButton_forecast_three_period.move(500, 485)
        self.radioButton_forecast_four_period.setFixedSize(50, 25)
        self.radioButton_forecast_four_period.move(560, 485)
        self.radioButton_forecast_five_period.setFixedSize(50, 25)
        self.radioButton_forecast_five_period.move(620, 485)

        # 在线购买彩票
        self.pushButton_purchase_lottery.setFixedSize(110, 25)
        self.pushButton_purchase_lottery.move(290, 515)
        # 界面全局设置
        self.setGeometry(500, 300, 680, 550)
        self.setWindowTitle(r'重庆时时彩预测数字软件')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    lottery = ForecastDigit()
    lottery.show()
    sys.exit(app.exec_())

