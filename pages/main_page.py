from pages.base_page import BasePage
from locators.main_page_locator import MainPageLocator


class MainPage(BasePage):

    def login(self, email, passwd):
        email_field = self.find_element(
            MainPageLocator.LOCATOR_USER_EMAIL_FIELD)
        email_field.send_keys(email)

        password_field = self.find_element(
            MainPageLocator.LOCATOR_PASSWORD_FIELD)
        password_field.send_keys(passwd)

        log_button = self.find_element(
            MainPageLocator.LOCATOR_LOGIN_BUTTON)
        log_button.click()

    def choice_duck(self, color):
        duck = self.find_element(
            MainPageLocator.get_first_duck_locator_most_popular(color))
        duck.click()
