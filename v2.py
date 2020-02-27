# coding:utf-8
# !/usr/bin/env python
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime


class FK:
    def __init__(self):
        # 初始信息
        self.alias = '×××'  # 名字，或者给自己起个昵称吧
        self.user_name = '××××××××××××'  # 学号
        self.password = '××××××××'  # 密码
        self.body_temperature = str(randint(362, 370) / 10)  # 随机生成一个36.2~37.0的体温

    def get_in(self):
        # 打开网站

        # --------------------------------------------------------------------------------------------------------------
        # 如果用正常模式，把这块取消注释，并且注释掉下一个块

        driver = webdriver.Chrome()

        # --------------------------------------------------------------------------------------------------------------
        # 如果用无头模式在服务器中跑，把这块取消注释，并且注释掉上一个块

        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # driver = webdriver.Chrome(chrome_options=chrome_options)

        # --------------------------------------------------------------------------------------------------------------

        # driver.maximize_window()  # 窗口最大化，可要可不要
        driver.get('http://tb.bucea.edu.cn:8075/WebReport/ReportServer?op=fs')
        driver.implicitly_wait(120)  # 我等你120秒

        # 填入学号、密码
        driver.find_element_by_class_name('fs-login-username').send_keys(self.user_name)
        driver.find_element_by_class_name('fs-login-password').send_keys(self.password)

        # 勾选记住登陆并登陆
        # driver.find_element_by_class_name('fs-login-remember').click()
        # time.sleep(1)           # 这行也是可以不要的
        driver.find_element_by_id('fs-login-btn').click()
        driver.implicitly_wait(120)  # 我再等你120秒

        # 进入表单界面
        driver.find_element_by_xpath('//*[@id="fs-frame-menu"]/div[1]/div[1]/div/ul/li/a').click()
        driver.find_element_by_xpath('//*[@id="fs-frame-menu"]/div[1]/div[1]/div/ul/li/ul/li/a').click()
        driver.find_element_by_xpath('//*[@id="fs-frame-content"]/div/div[2]/div/ul/li/div').click()

        # 利用js脚本切换到表单框架
        form_url = driver.find_element_by_class_name('fs-tab-content-toolbar').get_attribute('src')
        js_open_new_window = 'window.open("' + str(form_url) + '");'
        driver.execute_script(js_open_new_window)
        driver.switch_to.window(driver.window_handles[1])
        driver.implicitly_wait(30)  # 加个隐性等待，防止进表单界面排队导致出错

        # 载入表格
        driver.find_element_by_xpath('//*[@id="0"]/tbody')

        return driver

    def check(self):
        # 进入
        driver = self.get_in()
        # 找到最下行开头日期并判断是否为今天
        driver.find_element_by_class_name('fr-radio-radiooff').click()  # 点了这个才能获取到class dirty，莫名其妙
        raw_id = driver.find_element_by_class_name('dirty').get_attribute('id')  # 获取行数ID
        id_of_date = 'A' + str(int(raw_id[:-4][1:]) - 1) + raw_id[-4:]
        date = driver.find_element_by_id(id_of_date).text
        if date != today:
            print(self.alias, "Not Completed! Processing...", today)
            self.process(driver, raw_id)
            self.check()
        else:
            print(self.alias, "Already Completed!", today)
            driver.quit()

    def process(self, driver, raw_id):
        # 填入其余两项必需（现在只用再填写个体温）
        id_of_temperature = 'D' + raw_id[1:]  # 体温ID
        # id_of_difficulty = 'Q' + raw_id[1:]                                                  # 思想状况ID
        driver.find_element_by_id(id_of_temperature).click()  # 这里比较坑，
        driver.find_element_by_id(id_of_temperature).click()  # 同一个元素要点击两次才能send_keys
        # driver.find_element_by_id(id_of_temperature).send_keys(self.body_temperature)
        driver.find_element_by_class_name('fr-texteditor').send_keys(self.body_temperature)  # 填入体温
        # selector = '#content-container > div > div.x-editor > div > input'
        # driver.find_element_by_css_selector(selector).send_keys(self.body_temperature)

        # driver.find_element_by_id(id_of_difficulty).click()                                  # 坑死了
        # driver.find_element_by_id(id_of_difficulty).click()                                  # 代码不规范，自动化两行泪。
        # driver.find_element_by_class_name('fr-trigger-center').click()
        # button = driver.find_elements_by_class_name('fr-combo-list')[0].click()                     # lst[0]。。拿到表单了~
        # ActionChains(driver).move_to_element_with_offset(button, 50, 20).click().perform()  # 用动作链移动坐标点击“正常”位置

        # 点击提交
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="fr-btn-Submit"]/div/em/button').click()
        time.sleep(8)  # 防止运行太快提交没点上从而进入死循环
        # msg = driver.switch_to.alert.text
        # if msg == "提交成功":
        #     driver.quit()
        #     print(self.alias, "Done!", today)
        # else:
        driver.implicitly_wait(10)
        driver.quit()


if __name__ == '__main__':
    today = str(datetime.date.today())
    fk = FK()
    fk.check()
