import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


@pytest.fixture(scope='session')
def setup(browser):
    # Browser initialization
    if browser.lower() == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--incognito")
        # chrome_options.add_argument("disable-infobars")
        # chrome_options.add_argument("ignore-certificate-errors")
        driver = webdriver.Chrome(options=chrome_options)
        logging.info("Launching Chrome browser")

    elif browser.lower() == 'edge':
        edge_options = EdgeOptions()
        edge_options.add_argument("inPrivate")
        # edge_options.add_argument("disable-infobars")
        # edge_options.add_argument("ignore-certificate-errors")
        driver = webdriver.Edge(options=edge_options)
        logging.info("Launching Edge browser")

    else:
        chrome_options = ChromeOptions()
        # chrome_options.add_argument("--incognito")
        # chrome_options.add_argument("disable-infobars")
        # chrome_options.add_argument("ignore-certificate-errors")
        driver = webdriver.Chrome(options=chrome_options)
        logging.info("Launching Chrome browser by default")

    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    # teardown
    driver.quit()
    logging.info('Closing browser')


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome, firefox, edge")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
