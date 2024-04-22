import pytest
from selenium import webdriver

@pytest.fixture()


def driver():
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
