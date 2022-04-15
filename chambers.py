from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


def drop_n_click(drop_down_id, value_id):
    drop_down = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"(//button[@class='btn btn-primary toggle-button'])[{str(drop_down_id)}]",
            )
        )
    )
    action = ActionChains(driver)
    action.move_to_element(to_element=drop_down)
    action.click()
    action.perform()

    value = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//div[@scrollid={str(value_id)}]"))
    )
    if drop_down_id == 1:
        print(f"REGION: {value.text}")
    elif drop_down_id == 2:
        print(f"LOCATION: {value.text}")
    if drop_down_id == 3:
        print(f"PRACTICE: {value.text}")
    value.click()


driver = webdriver.Chrome()
# driver.get("https://chambers.com/legal-guide/usa-5")
driver.get("https://chambers.com/legal-rankings/construction-alaska-5:15:11887:1")

# Accepts cookies if popped up
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        )
    ).click()
finally:
    print("Cookies handled")


LOCATION_DROP_DOWN = 2
PRACTICE_AREA_DROP_DOWN = 3


location_id = 0
practice_area_id = 0
while True:
    try:
        drop_n_click(LOCATION_DROP_DOWN, location_id)
        driver.implicitly_wait(10)
        drop_n_click(PRACTICE_AREA_DROP_DOWN, practice_area_id)

        # seearch_xpath_value="(//button[@class='btn btn-chambers-light-blue w-100' and contains(text(),'Search')])[1]"
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@class='btn btn-chambers-light-blue mt-1 w-100']")
            )
        )
        search_button.click()

        ranked_lawyers = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//li[@class='nav-item']/span[contains(text(), 'Ranked Lawyers')]",
                )
            )
        )
        ranked_lawyers.click()
        time.sleep(5)

        # TO_DO: Extract data
    except:
        print("not found")
    finally:
        location_id += 1
        practice_area_id += 1
driver.quit()
