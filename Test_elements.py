import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
login = driver.find_element_by_id("txtUsername")
login.send_keys("Admin")
password = driver.find_element_by_id("txtPassword")
password.send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

driver.find_element_by_id("menu_pim_viewPimModule").click() # переход на Employee List

# нажали на третьего в списке работника, открылась страница Personal Details
driver.find_elements_by_xpath("//div[@id='tableWrapper']//tbody//a")[7].click()

# проверка на ошибки в радиокнопках Gender
gender_1 = driver.find_elements_by_xpath("//li[@class='radio']//input")[0]
gender_2 = driver.find_elements_by_xpath("//li[@class='radio']//input")[1]
# проверяем, выбраны ли радиокнопки
gender_1_checked = gender_1.get_attribute("checked")
gender_2_checked = gender_2.get_attribute("checked")
print("Value 'Checked' of Male is:",gender_1.get_attribute("checked"))
print("Value 'Checked' of Female is:",gender_2.get_attribute("checked"))
genderBeforeChange = None
# если выбрана первая, проверяем, заблокирована ли вторая
if gender_1_checked is not None:
    genderBeforeChange = "male"
    gender_2_dis = gender_2.get_attribute("disabled")
    if gender_2_dis is not None:
        print("OK: Male is selected, Female is disabled")
    else:
        print("Error: Male is selected, but Female is enabled")
# если выбрана вторая, проверяем, заблокирована ли первая
elif gender_2_checked is not None:
    genderBeforeChange = "female"
    gender_1_dis = gender_1.get_attribute("disabled")
    if gender_1_dis is not None:
        print("OK: Female is checked, Male is disabled")
    else:
        print("Error: Female is checked, but Male is enabled")
else:
    genderBeforeChange = "none"
    print("Attention: Gender is not selected")

# проверяем, доступен ли селектор Nationality
nation = driver.find_element_by_id("personal_cmbNation")
nation_dis = nation.get_attribute("disabled")
if nation_dis is not None:
    print("OK: Nationality selector is disabled")
else:
    print("Error: Nationality selector is enabled")

# заходим в редактирование карточки
driver.find_element_by_id("btnSave").click()

# меняем пол на противоположный
genderAfterChange = None
if genderBeforeChange == "male":
    gender_2.click()
    genderAfterChange = "female"
    print("\nChange1: Male was selected, Female is chosen now")
    gender_2.is_selected() # проверяем, что радиокнопка действительно выбрана
    if gender_2:
        print("OK: Female is selected")
elif genderBeforeChange == "female":
    gender_1.click()
    genderAfterChange = "male"
    print("\nChange1: Female was selected, Male is chosen now")
    gender_1.is_selected() # проверяем, что радиокнопка действительно выбрана
    if gender_1:
        print("OK: Male is selected")
elif genderBeforeChange == "none":
    gender_1.click()
    genderAfterChange = "male"
    print("\nChange1: gender wasn't selected; Male is chosen now")
    gender_1.is_selected() # проверяем, что радиокнопка действительно выбрана
    if gender_1:
        print("OK: Male is selected")

# выбираем самую последнюю национальность в списке
nation = driver.find_element_by_id("personal_cmbNation")
select = Select(nation)
selectLen = len(select.options)
select.select_by_index(selectLen-1)
lastNation = select.first_selected_option.get_attribute("value")
print("\nChange2: last in list nationality is chosen:",(Select(driver.find_element_by_id("personal_cmbNation")).first_selected_option.text))

# проверяем, выбрана ли последняя страна в списке
curNation = Select(driver.find_element_by_id("personal_cmbNation")).first_selected_option.get_attribute('value')
if (lastNation != curNation):
    print("Error: last nation is not checked")
else:
    print("OK: nationality is",(Select(driver.find_element_by_id("personal_cmbNation")).first_selected_option.text))

# возвращаем пол сотрудника как было
gender_1 = driver.find_elements_by_xpath("//li[@class='radio']//input")[0]
gender_2 = driver.find_elements_by_xpath("//li[@class='radio']//input")[1]
if genderBeforeChange == "male":
    gender_1.click()
    print("\nChange3: Female was chosen, Male is returned now")
elif genderBeforeChange == "female":
    gender_2.click()
    print("\nChange3: Male was chosen, Female is returned now")
elif genderBeforeChange == "none":
    gender_2.click()
    print("\nChange3: gender wasn't selected; then Male was chosen; now Female is selected")
#не получилось разобраться, как снова сделать кнопку невыделенной
#    gender_1.deselect_by_visible_text("Male") - no such attribute. Select has this one, but don't works with <input>
#    print("\nChange3: gender wasn't selected; then Male was chosen; now gender is not selected again")

# меняем национальность на -- Select --
nation = driver.find_element_by_id("personal_cmbNation")
select = Select(nation)
select.select_by_value("0")
print("Change4: nationality is not selected now")

# сохраняем изменения
driver.find_element_by_id("btnSave").click()

driver.quit()