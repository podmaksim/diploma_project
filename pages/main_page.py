from pages.base_page import BasePage
from locators.main_page_locator import MainPageLocator

user_email = 'podmaksim@gmail.com'
password = '1111'


class MainPage(BasePage):

    def enter_email(self):
        email_field = self.find_element(
            MainPageLocator.LOCATOR_USER_EMAIL_FIELD)
        email_field.send_keys(user_email)

    def enter_password(self):
        password_field = self.find_element(
            MainPageLocator.LOCATOR_PASSWORD_FIELD)
        password_field.send_keys(password)

    def click_log(self):
        log_button = self.find_element(
            MainPageLocator.LOCATOR_LOGIN_BUTTON)
        log_button.click()

    def choice_duck(self):
        red_duck = self.find_element(
            MainPageLocator.LOCATOR_CHOICE_RED_DUCK)
        red_duck.click()
