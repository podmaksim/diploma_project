from pages.base_admin_page import BaseAdminPage
from locators.admin_page_locator import AdminPageLocator

user_name = 'admin'
password = 'admin'


class AdminPage(BaseAdminPage):

    def enter_user_name(self):
        user_name_field = self.find_element(
            AdminPageLocator.LOCATOR_USER_NAME_FIELD)
        user_name_field.send_keys(user_name)

    def enter_password(self):
        password_field = self.find_element(
            AdminPageLocator.LOCATOR_PASSWORD_FIELD)
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.find_element(
            AdminPageLocator.LOCATOR_BUTTON_LOGIN)
        login_button.click()

    def click_customers_icon(self):
        customers_icon = self.find_element(
            AdminPageLocator.LOCATOR_CUSTOMERS_ICON)
        customers_icon.click()
