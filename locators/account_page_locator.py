from selenium.webdriver.common.by import By


class AccountPageLocator:

    LOCATOR_FIRST_NAME_FIELD = (By.CSS_SELECTOR, '[name="firstname"]')
    LOCATOR_LAST_NAME_FIELD = (By.CSS_SELECTOR, '[name="lastname"]')
    LOCATOR_BUTTON_SAVE = (By.XPATH, '//button[@name="save"]')
