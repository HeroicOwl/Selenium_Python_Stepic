# Взаимодействие с алертом

from selenium import webdriver
import math
#библиотека для копирования
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button1 = browser.find_element_by_tag_name("button")
button1.click()

confirm = browser.switch_to.alert
confirm.accept()

x_em = browser.find_element_by_xpath("//span[@id='input_value']")
x = x_em.text
y = calc(x)

input = browser.find_element_by_xpath("//input[@type='text']")
input.send_keys(y)

button2 = browser.find_element_by_tag_name("button")
button2.click()

# дальнейший код распарсивает из алерта число и заносит в буфер

alert = browser.switch_to.alert
# копируем весь текст алерта
alert_text = alert.text
# достаем нужное число
# split разделяет на две части ['какой-то текст', 'искомое число']
# [-1] вернет последний элемент т е 'искомое число'
text = alert_text.split(': ')[-1]
# копируем число
pyperclip.copy(text)
#проверка что текст действительно скопировался
print(pyperclip.paste())