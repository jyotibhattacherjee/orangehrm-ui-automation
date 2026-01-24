import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser_instance():
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    option.add_argument("start-maximized")
    driver = webdriver.Chrome(options=option)
    #driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com")

    yield driver
    driver.quit()