# ожидание нужного текста на странице
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pyperclip
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока стоимость не станет оптимальной
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )

btn_book = browser.find_element_by_tag_name("button")
btn_book.click()

x_em = browser.find_element_by_xpath("//span[@id='input_value']")
x = x_em.text
y = calc(x)

input = browser.find_element_by_xpath("//input[@type='text']")
input.send_keys(y)

btn_send = browser.find_element_by_xpath("//button[@id='solve']")
btn_send.click()

alert = browser.switch_to.alert
alert_text = alert.text
text = alert_text.split(': ')[-1]
pyperclip.copy(text)
print(pyperclip.paste())
