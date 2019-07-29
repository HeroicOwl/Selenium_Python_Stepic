# unittest
from selenium import webdriver
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

def test(link):
	browser = webdriver.Chrome()
	browser.get(link)

	# Код, который заполняет обязательные поля
	input1 = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
	input1.send_keys("Ivan")
	input2 = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
	input2.send_keys("Petrov")
	input3 = browser.find_element_by_xpath("//input[@class='form-control third' and @required]")
	input3.send_keys("Petrov@mail.ru")

	# Отправляем заполненную форму
	button = browser.find_element_by_css_selector("button.btn")
	button.click()

	# Проверяем, что смогли зарегистрироваться
	# ждем загрузки страницы
	time.sleep(1)

	# находим элемент, содержащий текст
	welcome_text_elt = browser.find_element_by_tag_name("h1")
	# записываем в переменную welcome_text текст из элемента welcome_text_elt
	welcome_text = welcome_text_elt.text
		
	# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
	assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
	#self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!")

class TestAbs(unittest.TestCase):
	def test_link1(self):
		test(link1)
	
	def test_link2(self):
		test(link2)		

if __name__ == "__main__":
    unittest.main()