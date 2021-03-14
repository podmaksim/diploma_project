from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseAdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_admin_page = 'http://localhost/litecart/admin/'

    def open_admin_page(self):
        self.driver.get(self.base_admin_page)

    def find_element(self, locator: tuple, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            f'Can not find element {locator}')

    def find_elements(self, locator: tuple, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            f'Can not find element {locator}')
