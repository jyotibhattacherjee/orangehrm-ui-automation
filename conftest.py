import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser_instance():
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    option.add_argument("--headless")
    option.add_argument("--window-size=1920,1080")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("start-maximized")
    driver = webdriver.Chrome(options=option)
    #driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com")

    yield driver
    driver.quit()