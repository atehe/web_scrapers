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

time.sleep(2)
location_drop_down = driver.find_element(
    by=By.XPATH,
    value="(//button[@class='btn btn-primary toggle-button'])[2]",
)

action = ActionChains(driver)
action.move_to_element(to_element=location_drop_down)
action.click()
print("clicked")
action.perform()
print("performed, waiting...")

time.sleep(5)

location_id = 20
while True:
    location = driver.find_element(
        by=By.XPATH, value=f"//div[@scrollid={str(location_id)}]"
    )
    location.click()
    location_id += 1
    practice_area_id = 3
    while True:

        practice_area_drop_down = driver.find_element(
            by=By.XPATH, value="(//button[@class='btn btn-primary toggle-button'])[3]"
        )
        action = ActionChains(driver)
        action.move_to_element(to_element=practice_area_drop_down)
        action.click()
        print("clicked")
        action.perform()
        print("performed, waiting...")

        time.sleep(5)

        practice_area = driver.find_element(
            by=By.XPATH, value=f"//div[@scrollid={str(practice_area_id)}]"
        )
        practice_area.click()

        time.sleep(100)


print(locations)
time.sleep(100)
driver.quit()
