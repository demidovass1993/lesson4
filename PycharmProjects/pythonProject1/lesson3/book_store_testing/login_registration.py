# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id('reg_email').send_keys('sveta@mail.ru')
# driver.find_element_by_id("reg_password").send_keys('123Sveta!')
# driver.find_element_by_css_selector('[name="register"]').click()
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id('username').send_keys('sveta@mail.ru')
driver.find_element_by_id("password").send_keys('123Sveta!')
driver.find_element_by_css_selector('[name="login"]').click()
text = EC.text_to_be_present_in_element((By.CSS_SELECTOR, "(href='https://practice.automationtesting.in/my-account/customer-logout/')"), "Logout")
driver.quit()