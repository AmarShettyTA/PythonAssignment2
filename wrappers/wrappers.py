import logging
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def enter_using_xpath(driver, locator, value, message):
    try:
        driver.find_element(By.XPATH, locator).clear()
        driver.find_element(By.XPATH, locator).send_keys(value)
        logging.info(message)
    except Exception as e:
        logging.error(locator)
        logging.error(e)
        driver.save_screenshot("error.png")


def click_using_xpath(driver, locator, message):
    try:
        driver.find_element(By.XPATH, locator).click()
        logging.info(message)
    except Exception as e:
        logging.error(locator)
        logging.error(e)
        driver.save_screenshot("error.png")


def is_element_displayed(driver, locator):
    try:
        element = driver.find_element(By.XPATH, locator)
        assert element.is_displayed(), "The element is not visible"
    except Exception as e:
        logging.error(locator)
        logging.error(e)
        driver.save_screenshot("error.png")


def click_using_actions_and_xpath(driver, locator, message):
    try:
        action = ActionChains(driver)
        action.move_to_element(driver.find_element(By.XPATH, locator)).click().perform()
        time.sleep(5)
        logging.info(message)
    except Exception as e:
        logging.error(locator)
        logging.error(e)
        driver.save_screenshot("error.png")
