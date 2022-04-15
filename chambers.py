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
        time.sleep(3)
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

        time.sleep(3)
        search_button = driver.find_element(
            by=By.XPATH, value='//*[@id="searchCollapsable"]/div[2]/div[2]/button'
        )
        search_button.click()

        time.sleep(5)

        # //*[@id="main"]/app-rankings/app-rankings-table/div/div[3]/div/app-rankings-tabs/div[1]/ul/lidriver.find_element(by=By.XPATH, value="(//button[@class='btn btn-chambers-light-blue w-100' and contains(text(),'Search')])[1]")
        ranked_lawyers = driver.find_element(
            by=By.XPATH,
            value="//li[@class='nav-item']/span[contains(text(), 'Ranked Lawyers')]",
        )
        ranked_lawyers.click()
        time.sleep(3)

        time.sleep(100)


print(locations)
time.sleep(100)
driver.quit()
