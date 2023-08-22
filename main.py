from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time

driver = webdriver.Chrome()
driver.get("http://tutorialsninja.com/demo/")
#find by tag
search_field = driver.find_element(By.NAME, "search")
search_field.send_keys("iphone")
search_field.send_keys(Keys.RETURN)

add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]')
add_to_cart_button.click()


# driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
shopping_cart_link = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT,"shopping")))
shopping_cart_link = driver.find_element(By.PARTIAL_LINK_TEXT,"shopping")
shopping_cart_link.click()

assert "product 11" in driver.page_source

driver.close()
# time.sleep(5)
# цикл чтобы окно не закрылось
# while True:
#     user_input = input("Введите 'q' для закрытия браузера: ")
#     if user_input.lower() == 'q':
#         break
