import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service = Service("geckodriver.exe")
driver = webdriver.Firefox(service=service)
driver.get('http://127.0.0.1:5000/login')
time.sleep(3)
driver.find_element(By.NAME, 'email').send_keys("john@simplylift.co")
driver.find_element(By.TAG_NAME, 'button').click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, 'book').click()
time.sleep(3)
driver.find_element(By.NAME, 'places').send_keys('4')
time.sleep(3)
driver.find_element(By.TAG_NAME, 'button').click()
time.sleep(3)
response_message = driver.find_element(By.CLASS_NAME, 'message')
assert "Great-booking complete!" in response_message.text
driver.find_element(By.CLASS_NAME, 'book').click()
time.sleep(3)
driver.find_element(By.NAME, 'places').send_keys('10')
time.sleep(3)
driver.find_element(By.TAG_NAME, 'button').click()
time.sleep(3)
response_message = driver.find_element(By.CLASS_NAME, 'message')
assert "Impossible to buy more places than you own" in response_message.text
driver.find_elements(By.ID, 'logout')[0].click()
time.sleep(3)
driver.quit()
