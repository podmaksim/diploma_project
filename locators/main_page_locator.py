from selenium.webdriver.common.by import By


class MainPageLocator:
    LOCATOR_USER_EMAIL_FIELD = (By.XPATH, '//input[@name="email"]')
    LOCATOR_PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')
    LOCATOR_LOGIN_BUTTON = (By.XPATH, '//button[@name="login"]')

    @staticmethod
    def get_first_duck_locator_most_popular(color):
        LOCATOR_CHOICE_DUCK = (By.XPATH, f'//div[@id="box-most-popular"]'
                                         f'//div[@class="content"]'
                                         f'//a[@title="{color}"]')
        return LOCATOR_CHOICE_DUCK
