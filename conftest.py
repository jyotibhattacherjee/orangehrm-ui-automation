import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser_instance():
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    option.add_argument("start-maximized")
    driver = webdriver.Chrome(options=option)
    #driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com")

    yield driver
    driver.quit()