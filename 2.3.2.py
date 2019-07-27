# переход на новую вкладку

from selenium import webdriver
import math
#библиотека для копирования
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button1 = browser.find_element_by_tag_name("button")
button1.click()

#получаем имя второй открытой вкладки
new_window = browser.window_handles[1]
#переходим на эту вкладку
browser.switch_to.window(new_window)

x_em = browser.find_element_by_xpath("//span[@id='input_value']")
x = x_em.text
y = calc(x)

input = browser.find_element_by_xpath("//input[@type='text']")
input.send_keys(y)

button2 = browser.find_element_by_tag_name("button")
button2.click()


alert = browser.switch_to.alert
alert_text = alert.text
text = alert_text.split(': ')[-1]
pyperclip.copy(text)
print(pyperclip.paste())