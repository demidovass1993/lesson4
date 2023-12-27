# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id('username').send_keys('sveta@mail.ru')
# driver.find_element_by_id("password").send_keys('123Sveta!')
# driver.find_element_by_css_selector('[name="login"]').click()
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector('[title="Mastering HTML5 Forms"]').click()
# text_header = driver.find_element_by_tag_name('h1').text
# assert text_header == "HTML5 Forms"
# driver.quit()


# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id('username').send_keys('sveta@mail.ru')
# driver.find_element_by_id("password").send_keys('123Sveta!')
# driver.find_element_by_css_selector('[name="login"]').click()
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector('.cat-item-19>a').click()
# items_count = driver.find_elements_by_class_name("product")
# assert len(items_count) == 3
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id('username').send_keys('sveta@mail.ru')
# driver.find_element_by_id("password").send_keys('123Sveta!')
# driver.find_element_by_css_selector('[name="login"]').click()
# driver.find_element_by_id("menu-item-40").click()
# sort = driver.find_element_by_css_selector("[name='orderby']")
# sort_value = sort.get_attribute("value")
# assert sort_value == 'menu_order'
# selector_sort = Select(sort)
# selector_sort.select_by_value('price-desc')
# sort = driver.find_element_by_css_selector("[name='orderby']")
# sort_value = sort.get_attribute("value")
# assert sort_value == ('price-desc')
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id('username').send_keys('sveta@mail.ru')
# driver.find_element_by_id("password").send_keys('123Sveta!')
# driver.find_element_by_css_selector('[name="login"]').click()
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector('[title="Android Quick Start Guide"]').click()
# old_price = driver.find_element_by_css_selector('.price del>span').text
# new_price = driver.find_element_by_css_selector('.price ins>span').text
# assert old_price == ('₹600.00')
# assert new_price == ('₹450.00')
# cover_book = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.CLASS_NAME, 'images')))
# cover_book.click()
# cover_book_close = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')))
# cover_book_close.click()
# driver.quit()


# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector('[data-product_id="182"]').click()
# time.sleep(2)
# count_item =driver.find_element_by_class_name('cartcontents').text
# amount =driver.find_element_by_class_name('amount').text
# assert count_item == '1 Item'
# assert amount == '₹180.00'
# driver.find_element_by_id('wpmenucartli').click()
# subtotal_text= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-title="Subtotal"] > span'), '₹180.00'))
# total_text= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'strong > span'), '₹183.60'))
# driver.quit()

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector('[data-product_id="182"]').click()
# driver.execute_script("window.scrollBy(0, 300);")
# time.sleep(3)
# driver.find_element_by_css_selector('[data-product_id="180"]').click()
# driver.find_element_by_id('wpmenucartli').click()
# time.sleep(3)
# driver.find_element_by_css_selector('[data-product_id="182"]').click()
# time.sleep(3)
# driver.find_element_by_css_selector('.woocommerce-message>a').click()
# count = driver.find_element_by_css_selector('.cart_item:nth-child(1)  input')
# count.clear()
# count.send_keys(3)
# driver.find_element_by_css_selector('[name="update_cart"]').click()
# time.sleep(3)
# count = driver.find_element_by_css_selector('.cart_item:nth-child(1)  input')
# value_count = count.get_attribute('value')
# assert value_count == '3'
# time.sleep(3)
# driver.find_element_by_css_selector('[name="apply_coupon"]').click()
# time.sleep(3)
# error_text=WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-error > li'), 'Please enter a coupon code.'))
# driver.quit()

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(3)
driver.find_element_by_id('wpmenucartli').click()
driver.find_element_by_class_name('checkout-button').click()
first_name = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.ID, 'billing_first_name')))
first_name.send_keys("Sveta")
last_name = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.ID, 'billing_last_name')))
last_name.send_keys("Demidova")
email = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.ID, 'billing_email')))
email.send_keys("sveta@mail.ru")
phone = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.ID, 'billing_phone')))
phone.send_keys("79998885555")
driver.find_element_by_css_selector('[href="javascript:void(0)"]').click()
driver.find_element_by_id('s2id_autogen1_search').send_keys('Russia')
driver.find_element_by_id('select2-results-1').click()
driver.find_element_by_id('billing_address_1').send_keys('Leninskiy')
driver.find_element_by_id('billing_city').send_keys('SPB')
driver.find_element_by_id('billing_state').send_keys('Russia')
driver.find_element_by_id('billing_postcode').send_keys('111111')
driver.find_element_by_id('payment_method_cheque').click()
driver.find_element_by_id('place_order').click()
text= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'), 'Thank you. Your order has been received.'))
payment= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'tr:nth-child(3) >td'), 'Check Payments'))


