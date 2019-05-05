import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QLineEdit, QPushButton, QRadioButton, QButtonGroup
from PyQt5.QtCore import *


class ForecastBigSmall(QMainWindow):

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
        self.label_forecast_wan = QLabel(r'万位大小', self)
        self.label_forecast_thousand = QLabel(r'千位大小', self)
        self.label_forecast_hundred = QLabel(r'百位大小', self)
        self.label_forecast_ten = QLabel(r'十位大小', self)
        self.label_forecast_unit = QLabel(r'个位大小', self)

        # 预测大小的标签
        # 万位预测大小
        self.label_forecast_wan_big = QLabel(r'大', self)
        self.label_forecast_wan_small = QLabel(r'小', self)
        # 千位预测大小
        self.label_forecast_thousand_big = QLabel(r'大', self)
        self.label_forecast_thousand_small = QLabel(r'小', self)
        # 百位预测大小
        self.label_forecast_hundred_big = QLabel(r'大', self)
        self.label_forecast_hundred_small = QLabel(r'小', self)
        # 十位预测大小
        self.label_forecast_ten_big = QLabel(r'大', self)
        self.label_forecast_ten_small = QLabel(r'小', self)
        # 个位预测大小
        self.label_forecast_unit_big = QLabel(r'大', self)
        self.label_forecast_unit_small = QLabel(r'小', self)

        # 预测准确率的输入文本框
        # 万位预测号码
        self.lineEdit_forecast_wan_big_ratio = QLineEdit(self)
        self.lineEdit_forecast_wan_small_ratio = QLineEdit(self)
        # 千位预测号码
        self.lineEdit_forecast_thousand_big_ratio = QLineEdit(self)
        self.lineEdit_forecast_thousand_small_ratio = QLineEdit(self)
        # 百位预测号码
        self.lineEdit_forecast_hundred_big_ratio = QLineEdit(self)
        self.lineEdit_forecast_hundred_small_ratio = QLineEdit(self)
        # 十位预测号码
        self.lineEdit_forecast_ten_big_ratio = QLineEdit(self)
        self.lineEdit_forecast_ten_small_ratio = QLineEdit(self)
        # 个位预测号码
        self.lineEdit_forecast_unit_big_ratio = QLineEdit(self)
        self.lineEdit_forecast_unit_small_ratio = QLineEdit(self)
        # 预测号码按钮
        self.pushButton_forecast_big_small = QPushButton(r'预测开奖大小', self)

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
        self.label_forecast_wan.setFixedSize(60, 25)
        self.label_forecast_wan.move(10, 65)
        self.label_forecast_wan_big.setFixedSize(50, 25)
        self.label_forecast_wan_big.move(200, 65)
        self.label_forecast_wan_big.setAlignment(Qt.AlignCenter)
        self.lineEdit_forecast_wan_big_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_big_ratio.move(260, 65)
        self.label_forecast_wan_small.setFixedSize(50, 25)
        self.label_forecast_wan_small.move(440, 65)
        self.label_forecast_wan_small.setAlignment(Qt.AlignCenter)
        self.lineEdit_forecast_wan_small_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_wan_small_ratio.move(500, 65)

        # 千位部分
        self.label_forecast_thousand.setFixedSize(60, 25)
        self.label_forecast_thousand.move(10, 95)
        self.label_forecast_thousand_big.setFixedSize(50, 25)
        self.label_forecast_thousand_big.move(200, 95)
        self.label_forecast_thousand_big.setAlignment(Qt.AlignCenter)
        self.lineEdit_forecast_thousand_big_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_big_ratio.move(260, 95)
        self.label_forecast_thousand_small.setFixedSize(50, 25)
        self.label_forecast_thousand_small.move(440, 95)
        self.label_forecast_thousand_small.setAlignment(Qt.AlignCenter)
        self.lineEdit_forecast_thousand_small_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_thousand_small_ratio.move(500, 95)

        # 百位部分
        self.label_forecast_hundred.setFixedSize(60, 25)
        self.label_forecast_hundred.move(10, 125)
        self.label_forecast_hundred_big.setFixedSize(50, 25)
        self.label_forecast_hundred_big.move(200, 125)
        self.label_forecast_hundred_big.setAlignment(Qt.AlignCenter)
        self.lineEdit_forecast_hundred_big_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_big_ratio.move(260, 125)
        self.label_forecast_hundred_small.setFixedSize(50, 25)
        self.label_forecast_hundred_small.move(440, 125)
        self.label_forecast_hundred_small.setAlignment(Qt.AlignCenter)
        self.lineEdit_forecast_hundred_small_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_hundred_small_ratio.move(500, 125)

        # 十位部分
        self.label_forecast_ten.setFixedSize(60, 25)
        self.label_forecast_ten.move(10, 155)
        self.label_forecast_ten_big.setFixedSize(50, 25)
        self.label_forecast_ten_big.move(200, 155)
        self.label_forecast_ten_big.setAlignment(Qt.AlignCenter)
        self.lineEdit_forecast_ten_big_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_big_ratio.move(260, 155)
        self.label_forecast_ten_small.setFixedSize(50, 25)
        self.label_forecast_ten_small.move(440, 155)
        self.label_forecast_ten_small.setAlignment(Qt.AlignCenter)
        self.lineEdit_forecast_ten_small_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_ten_small_ratio.move(500, 155)

        # 个位部分
        self.label_forecast_unit.setFixedSize(60, 25)
        self.label_forecast_unit.move(10, 185)
        self.label_forecast_unit_big.setFixedSize(50, 25)
        self.label_forecast_unit_big.move(200, 185)
        self.label_forecast_unit_big.setAlignment(Qt.AlignCenter)
        self.lineEdit_forecast_unit_big_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_big_ratio.move(260, 185)
        self.label_forecast_unit_small.setFixedSize(50, 25)
        self.label_forecast_unit_small.move(440, 185)
        self.label_forecast_unit_small.setAlignment(Qt.AlignCenter)
        self.lineEdit_forecast_unit_small_ratio.setFixedSize(50, 25)
        self.lineEdit_forecast_unit_small_ratio.move(500, 185)

        self.pushButton_forecast_big_small.setFixedSize(110, 25)
        self.pushButton_forecast_big_small.move(290, 215)

        # 在线投注部分
        # 设置用户信息与购买信息
        self.label_website.setFixedSize(60, 25)
        self.label_website.move(10, 245)
        self.lineEdit_website.setFixedSize(110, 25)
        self.lineEdit_website.move(80, 245)
        self.label_user_name.setFixedSize(50, 25)
        self.label_user_name.move(200, 245)
        self.label_user_name.setAlignment(Qt.AlignCenter)
        self.lineEdit_user_name.setFixedSize(50, 25)
        self.lineEdit_user_name.move(260, 245)
        self.label_user_password.setFixedSize(50, 25)
        self.label_user_password.move(320, 245)
        self.label_user_password.setAlignment(Qt.AlignCenter)
        self.lineEdit_user_password.setFixedSize(50, 25)
        self.lineEdit_user_password.move(380, 245)
        self.label_start_money.setFixedSize(50, 25)
        self.label_start_money.move(440, 245)
        self.label_start_money.setAlignment(Qt.AlignCenter)
        self.lineEdit_start_money.setFixedSize(50, 25)
        self.lineEdit_start_money.move(500, 245)
        self.label_stop_money.setFixedSize(50, 25)
        self.label_stop_money.move(560, 245)
        self.label_stop_money.setAlignment(Qt.AlignCenter)
        self.lineEdit_stop_money.setFixedSize(50, 25)
        self.lineEdit_stop_money.move(620, 245)

        # 显示投注信息
        self.label_current_lottery_time.setFixedSize(80, 25)
        self.label_current_lottery_time.move(10, 275)
        self.lineEdit_current_lottery_time.setFixedSize(40, 25)
        self.lineEdit_current_lottery_time.move(90, 275)
        self.label_current_lottery_money.setFixedSize(80, 25)
        self.label_current_lottery_money.move(140, 275)
        self.lineEdit_current_lottery_money.setFixedSize(40, 25)
        self.lineEdit_current_lottery_money.move(220, 275)
        self.label_history_max_wrong_time.setFixedSize(80, 25)
        self.label_history_max_wrong_time.move(270, 275)
        self.lineEdit_history_max_wrong_time.setFixedSize(40, 25)
        self.lineEdit_history_max_wrong_time.move(350, 275)
        self.label_history_max_lottery_money.setFixedSize(80, 25)
        self.label_history_max_lottery_money.move(400, 275)
        self.lineEdit_history_max_lottery_money.setFixedSize(40, 25)
        self.lineEdit_history_max_lottery_money.move(480, 275)
        self.label_profit_money.setFixedSize(80, 25)
        self.label_profit_money.move(530, 275)
        self.lineEdit_profit_money.setFixedSize(40, 25)
        self.lineEdit_profit_money.move(610, 275)

        # 设置用户购买方式
        self.label_lottery_bet_mode.setFixedSize(60, 25)
        self.label_lottery_bet_mode.move(10, 305)
        self.radioButton_buy_yuan.setFixedSize(50, 25)
        self.radioButton_buy_yuan.move(80, 305)
        self.radioButton_buy_corner.setFixedSize(50, 25)
        self.radioButton_buy_corner.move(140, 305)
        self.radioButton_buy_cent.setFixedSize(50, 25)
        self.radioButton_buy_cent.move(200, 305)
        self.label_lottery_risk_mode.setFixedSize(60, 25)
        self.label_lottery_risk_mode.move(260, 305)
        self.radioButton_low_risk.setFixedSize(110, 25)
        self.radioButton_low_risk.move(320, 305)
        self.radioButton_medium_risk.setFixedSize(110, 25)
        self.radioButton_medium_risk.move(440, 305)
        self.radioButton_high_risk.setFixedSize(110, 25)
        self.radioButton_high_risk.move(560, 305)

        self.label_lottery_buy_number_mode.setFixedSize(60, 25)
        self.label_lottery_buy_number_mode.move(10, 335)
        self.radioButton_forecast_four_bit.setFixedSize(50, 25)
        self.radioButton_forecast_four_bit.move(80, 335)
        self.radioButton_forecast_five_bit.setFixedSize(50, 25)
        self.radioButton_forecast_five_bit.move(140, 335)
        self.radioButton_forecast_six_bit.setFixedSize(50, 25)
        self.radioButton_forecast_six_bit.move(200, 335)
        self.radioButton_forecast_seven_bit.setFixedSize(50, 25)
        self.radioButton_forecast_seven_bit.move(260, 335)
        self.label_lottery_follow_mode.setFixedSize(50, 25)
        self.label_lottery_follow_mode.move(320, 335)
        self.radioButton_forecast_one_period.setFixedSize(50, 25)
        self.radioButton_forecast_one_period.move(380, 335)
        self.radioButton_forecast_two_period.setFixedSize(50, 25)
        self.radioButton_forecast_two_period.move(440, 335)
        self.radioButton_forecast_three_period.setFixedSize(50, 25)
        self.radioButton_forecast_three_period.move(500, 335)
        self.radioButton_forecast_four_period.setFixedSize(50, 25)
        self.radioButton_forecast_four_period.move(560, 335)
        self.radioButton_forecast_five_period.setFixedSize(50, 25)
        self.radioButton_forecast_five_period.move(620, 335)

        # 在线购买彩票
        self.pushButton_purchase_lottery.setFixedSize(110, 25)
        self.pushButton_purchase_lottery.move(290, 365)
        # 界面全局设置
        self.setGeometry(500, 300, 680, 400)
        self.setWindowTitle(r'重庆时时彩预测大小软件')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    lottery = ForecastBigSmall()
    lottery.show()
    sys.exit(app.exec_())

