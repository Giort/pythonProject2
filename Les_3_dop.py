from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# логин в систему
driver.find_element_by_xpath("//a[contains(text(), 'My Account')]").click()
driver.find_element_by_id("username").send_keys("1@1.com")
driver.find_element_by_id("password").send_keys("Ab<>123&456!=cD")
driver.find_element_by_name("login").click()
# нажать на вкладку Shop
driver.find_element_by_xpath("//a[contains(text(), 'Shop')]").click()




# Отображение, скидка товара
# открыть книгу Android Quick Start Guide
driver.find_element_by_xpath("//h3[contains(text(), 'Android Quick Start Guide')]").click()
# проверка, что содержимое старой цены = ₹600.00
old_price = driver.find_element_by_css_selector(".price > del > span:nth-child(1)").text
assert old_price == "₹600.00"
# проверка, что содержимое новой цены = ₹450.00
new_price = driver.find_element_by_css_selector(".price > ins > span:nth-child(1)").text
assert new_price == "₹450.00"
# открыть обложку книги в предпросмотре - не получилось
# Я знаю, что можно принудительно изменить разрешение экрана на то, для которого будет показана картинка в меньшем
# разрешении, но мне это кажется неправильным вариантом.
# Я попытался с помощью скрипта применить значение для мальнького разрешения к атрибуту srcset, но это не дало эффекта
preview = driver.find_element_by_css_selector(".images > a > img")
driver.execute_script("arguments[0].srcset='http://practice.automationtesting.in/wp-content/uploads/2017/01/Android-Quick-Start-Guide-180x180.png';", preview)
preview.click()
#WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value(((By.CSS_SELECTOR, ".images > a > img"), 'srcset', "http://practice.automationtesting.in/wp-content/uploads/2017/01/Android-Quick-Start-Guide-180x180.png"))).click()
# закрыть окно предпросмотра
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()


