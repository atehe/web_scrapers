from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


LOCATION_DROP_DOWN = 2
PRACTICE_AREA_DROP_DOWN = 3
LOCATIONS = 81


def drop_n_click(drop_down_id, value_id):
    drop_down = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"(//button[@class='btn btn-primary toggle-button'])[{drop_down_id}]",
            )
        )
    )
    action = ActionChains(driver)
    action.move_to_element(to_element=drop_down)
    action.click()
    action.perform()

    value = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//div[@scrollid='{value_id}']"))
    )
    if drop_down_id == 1:
        print(f"REGION: {value.text}")
    elif drop_down_id == 2:
        print(f"LOCATION: {value.text}")
    elif drop_down_id == 3:
        print(f"PRACTICE: {value.text}")
    value.click()


def click_search():
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@class='btn btn-chambers-light-blue mt-1 w-100']",
            )
        )
    ).click()


def go_to_tab(tab):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                f"//li[@class='nav-item']/span[contains(text(), '{tab}')]",
            )
        )
    ).click()


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://chambers.com/legal-rankings/construction-alaska-5:15:11887:1")

# Accepts cookies if popped up
try:
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        )
    ).click()
finally:
    print("Cookies handled")

driver.implicitly_wait(10)  # wait for dropdown to be populated


for location_id in range(LOCATIONS):
    try:
        drop_n_click(LOCATION_DROP_DOWN, location_id)
        driver.implicitly_wait(10)

        practice_area_id = 0
        while True:

            drop_n_click(PRACTICE_AREA_DROP_DOWN, practice_area_id)
            click_search()
            go_to_tab("Ranked Lawyers")

            # TO_DO: Extract data
            print("Scraping")

            time.sleep(3)

            practice_area_id += 1
            continue

    except:
        print("LOCATION: Rendering Error")

driver.quit()


# seearch_xpath_value="(//button[@class='btn btn-chambers-light-blue w-100' and contains(text(),'Search')])[1]"
# driver.get("https://chambers.com/legal-guide/usa-5")
