from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://chambers.com/legal-guide/usa-5")
time.sleep(10)
cookies = driver.find_element(
    by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]'
)
print(cookies.text)
cookies.click()


location_drop_down = driver.find_element(
    by=By.XPATH,
    value='//*[@id="searchCollapsable"]/div[1]/div[2]/cmb-dropdown/div/div/button',
)
# WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable(
#         (
#             By.XPATH,
#             '//*[@id="searchCollapsable"]/div[1]/div[2]/cmb-dropdown/div/div/button',
#         )
#     )
# ).click()
time.sleep(5)
action = ActionChains(driver)
# location_drop_down.click()

action.move_to_element(to_element=location_drop_down)
action.click()
print("clicked")
action.perform()
print("performed, waiting...")
# try:
#     locations = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//div[@class='item d-block']"))
#     )
#     print(locations)
# finally:
#     print(locations)
time.sleep(20)

locations = driver.find_element(by=By.XPATH, value="//div[@class='item d-block']")
print(locations.text)

print(locations)
time.sleep(100)
driver.quit()
