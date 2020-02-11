from random import randint
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# 初始信息
user_name = '××××××××××××'      # 学号
password = '××××××××'           # 密码
body_temperature = str(randint(362, 370) / 10)     # 随机生成一个36.2~37.0的体温

# ————————————————————————————————————————————————————无感情分割线———————————————————————————————————————————————————— #

# 打开网站
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://tb.bucea.edu.cn:8075/WebReport/ReportServer?op=fs')
time.sleep(2)           # 这行可以不要的

# 填入学号、密码
driver.find_element_by_class_name('fs-login-username').send_keys(user_name)
driver.find_element_by_class_name('fs-login-password').send_keys(password)

# 勾选记住登陆
driver.find_element_by_class_name('fs-login-remember').click()
time.sleep(1)           # 这行也是可以不要的

driver.find_element_by_id('fs-login-btn').click()

# ————————————————————————————————————————————————————无感情分割线———————————————————————————————————————————————————— #

# 进入表单界面
driver.find_element_by_xpath('//*[@id="fs-frame-menu"]/div[1]/div[1]/div/ul/li/a').click()
driver.find_element_by_xpath('//*[@id="fs-frame-menu"]/div[1]/div[1]/div/ul/li/ul/li/a').click()
driver.find_element_by_xpath('//*[@id="fs-frame-content"]/div/div[2]/div/ul/li/div').click()

# 利用js脚本切换到表单框架
form_url = driver.find_element_by_class_name('fs-tab-content-toolbar').get_attribute('src')
js_open_new_window = 'window.open("' + str(form_url) + '");'
driver.execute_script(js_open_new_window)
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(30)                                          # 加个隐性等待，防止进表单界面排队导致出错

# 载入表格
driver.find_element_by_xpath('//*[@id="0"]/tbody')

# 找到“与昨日情况一致”按钮并点击
driver.find_element_by_class_name('fr-radio-radiooff').click()

# 填入其余两项必需
raw_id = driver.find_element_by_class_name('dirty').get_attribute('id')             # 获取行数ID
id_of_temperature = 'D' + raw_id[1:]                                                # 体温ID
id_of_difficulty = 'Q' + raw_id[1:]                                                  # 思想状况ID
driver.find_element_by_id(id_of_temperature).click()                                # 这里比较坑，
driver.find_element_by_id(id_of_temperature).click()                                # 同一个元素要点击两次才能send_keys
driver.find_element_by_class_name('fr-texteditor').send_keys(body_temperature)      # 填入体温

driver.find_element_by_id(id_of_difficulty).click()                                  # 坑死了
driver.find_element_by_id(id_of_difficulty).click()                                  # 代码不规范，自动化两行泪。
driver.find_element_by_class_name('fr-trigger-center').click()
button = driver.find_elements_by_class_name('fr-combo-list')[0].click()                     # lst[0]。。拿到表单了~
# ActionChains(driver).move_to_element_with_offset(button, 50, 20).click().perform()  # 用动作链移动坐标点击“正常”位置

# ————————————————————————————————————————————————————无感情分割线———————————————————————————————————————————————————— #

# 提交
driver.find_element_by_xpath('//*[@id="fr-btn-Submit"]/div/em/button').click()
