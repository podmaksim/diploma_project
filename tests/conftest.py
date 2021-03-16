from selenium import webdriver
import pytest



@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    #options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
