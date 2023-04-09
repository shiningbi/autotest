import time
from lib.login import login
from lib.login import logins
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class Test_caidan():
    def test_caidan_001(self):
        print('\ncd用例001')
        elements=login('/html/body/div/aside/section/ul/li')
        for element in elements:
            print(element.text)

    def test_caidan_002(self):
        print('\ncd用例002')
        element=logins('/html/body/div/div/section[2]/div[1]/button')
        element.click()
        time.sleep(2)

    def test_caidan_003(self):
        print('\ncd用例003')
        wb = webdriver.Chrome()
        wb.get('http://127.0.0.1/mgr/sign.html')
        wb.find_element(By.ID, 'username').send_keys('byhy')
        wb.find_element(By.ID, 'password').send_keys('88888888')
        wb.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        elements = wb.find_elements(By.XPATH,'/html/body/div/div/section[2]/div/div/span')
        for element in elements:
            print(element.text)