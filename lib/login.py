from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def login(xpath):
    wb = webdriver.Chrome()
    wb.get('http://127.0.0.1/mgr/sign.html')
    wb.find_element(By.ID, 'username').send_keys('byhy')
    wb.find_element(By.ID, 'password').send_keys('88888888')
    wb.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    elements = wb.find_elements(By.XPATH, xpath)
    return elements

def logins(xpath):
    wb = webdriver.Chrome()
    wb.get('http://127.0.0.1/mgr/sign.html')
    wb.find_element(By.ID, 'username').send_keys('byhy')
    wb.find_element(By.ID, 'password').send_keys('88888888')
    wb.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    element = wb.find_element(By.XPATH, xpath)
    return element