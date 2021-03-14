from selenium.webdriver.common.by import By


class MainPageLocator:

    LOCATOR_USER_EMAIL_FIELD = (By.XPATH, '//input[@name="email"]')
    LOCATOR_PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')
    LOCATOR_LOGIN_BUTTON = (By.XPATH, '//button[@name="login"]')
    LOCATOR_CHOICE_RED_DUCK = (By.XPATH,
                               '//div[@class="image-wrapper"]'
                               '/img[@alt="Red Duck"]')
