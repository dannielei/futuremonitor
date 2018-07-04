from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
# from qi.data.wind.api import WindApiMarketLoader
from configparser import ConfigParser
from WindPy import *
import datetime

_config = ConfigParser()
_config.read("config.ini",encoding="utf-8")
# loader=WindApiMarketLoader()

browser=webdriver.Chrome()
wait=WebDriverWait(browser, 5)

def search(start, end):
    try:

        w.start()
        result = w.tdays(start, end, "").Times

        l = ['text','wt']
        for wi in l:

            # 账户密码
            browser.get('https://investorservice.cfmmc.com/')

            user = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,  'body > form > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(1) > td.formtext > input[type="text"]')))
            user.send_keys(dict(_config.items(wi)).get('user'))


            key = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > form > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(2) > td.formtext > input[type="password"]')))
            key.send_keys(dict(_config.items(wi)).get('password'))

            print('当前账户为：',wi)

            # 手动输入验证码
            code=input("请输入验证码:")
            value = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > form > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(3) > td.formtext > input[type="text"]')))
            value.send_keys(code)

            # 登录
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#s > input[type="image"]:nth-child(1)')))
            submit.click()
            sleep(1)

            # 获取从start到end之间的交易日历calendar
            # calendar = loader.load_date_sequence(from_=start, to_=end, calendar_type="TradingCalendar",exchange="SSE", frequency="D")
            #转化日期格式
            # result = ['{}-{}-{}'.format(item[:4], item[4:6], item[6:]) for item in calendar]
            # w.start()
            # result =w.tdays(start, end, "").Times

            for i in result:
                str = i.strftime('%Y-%m-%d')
                print(str)
                # 输入日期
                date = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                  '#SearchForm > form > input[type="text"]:nth-child(2)')))
                date.clear()
                date.send_keys(str)
                sleep(1)

                #点击“提交”
                select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#SearchForm > form > input.button')))
                select.click()
                sleep(1)

                #点击“下载“
                down = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#waitBody > table > tbody > tr:nth-child(1) > td > a')))
                down.click()
                sleep(1)

    except TimeoutException:
        return search()


if __name__ == '__main__':
    search(start="20180501", end="20180508")



