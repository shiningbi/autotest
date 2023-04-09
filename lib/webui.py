from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def loginAndCheck(username,password):
    wb = webdriver.Chrome()
    wb.get('http://127.0.0.1/mgr/sign.html')
    if username is not None:
        wb.find_element(By.ID,'username').send_keys(username)
    if password is not None:
        wb.find_element(By.ID,'password').send_keys(password)
    wb.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    alertText=wb.switch_to.alert.text
    return alertText