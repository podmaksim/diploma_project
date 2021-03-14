from selenium.webdriver.common.by import By


class AdminPageLocator:

    LOCATOR_USER_NAME_FIELD = (By.XPATH, '//input[@name="username"]')
    LOCATOR_PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')
    LOCATOR_BUTTON_LOGIN = (By.XPATH, '//button[@name="login"]')
    LOCATOR_CUSTOMERS_ICON = (By.XPATH,
                              '//i[@class="fa fa-user fa-stack-1x icon"]')
