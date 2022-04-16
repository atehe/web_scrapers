from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import bs4
import time


DRIVER = webdriver.Chrome()

LOCATION_DROP_DOWN = 2  # location dropdown identifier
PRACTICE_AREA_DROP_DOWN = 3  # practice area dropdown identifier
LOCATIONS = 81  # number of locations in dropdown


def drop_n_click(drop_down_id, value_id):
    drop_down = WebDriverWait(DRIVER, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"(//button[@class='btn btn-primary toggle-button'])[{drop_down_id}]",
            )
        )
    )
    action = ActionChains(DRIVER)
    action.move_to_element(to_element=drop_down)
    action.click()
    action.perform()

    value = WebDriverWait(DRIVER, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//div[@scrollid='{value_id}']"))
    )
    if drop_down_id == 1:
        print(f"REGION: {value.text}")
    elif drop_down_id == 2:
        print(f"LOCATION: {value.text}")
    elif drop_down_id == 3:
        print(f"PRACTICE: {value.text}")

    # checks for last value in dropdown (anchor doesn't have nested div)
    try:
        DRIVER.find_element(
            by=By.XPATH,
            value=f"//div[@scrollid='{value_id}']/following-sibling::div/div",
        )
        value.click()

    except:
        value.click()
        return True


def click_search():
    WebDriverWait(DRIVER, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@class='btn btn-chambers-light-blue mt-1 w-100']",
            )
        )
    ).click()


def go_to_tab(tab):
    WebDriverWait(DRIVER, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                f"//li[@class='nav-item']/span[contains(text(), '{tab}')]",
            )
        )
    ).click()


def main():

    DRIVER.get("https://chambers.com/legal-guide/usa-5")

    # Accepts cookies if popped up
    try:
        WebDriverWait(DRIVER, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
            )
        ).click()
    finally:
        print("Cookies handled")

    DRIVER.implicitly_wait(20)  # wait for dropdown to be populated

    for location_id in range(LOCATIONS):
        try:
            drop_n_click(LOCATION_DROP_DOWN, location_id)
            DRIVER.implicitly_wait(10)

            practice_area_id = 0
            while True:
                last_item = drop_n_click(PRACTICE_AREA_DROP_DOWN, practice_area_id)
                click_search()
                go_to_tab("Ranked Lawyers")

                # TO_DO: Extract data
                print("Scraping")

                practice_area_id += 1
                if last_item:
                    break
                continue

        except:
            print(f"Error, Location: {location_id}")
            continue

    DRIVER.quit()


if __name__ == "__main__":
    main()


# seearch_xpath_value="(//button[@class='btn btn-chambers-light-blue w-100' and contains(text(),'Search')])[1]"
# driver.get("https://chambers.com/legal-guide/usa-5")
