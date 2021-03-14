from pages.user_page import UserPage
from locators.account_page_locator import AccountPageLocator

new_first_name = 'Mask'
new_last_name = 'Ilon'


class AccountPage(UserPage):

    def change_firstname_field(self):
        first_name_field = self.find_element(
            AccountPageLocator.LOCATOR_FIRST_NAME_FIELD)
        self.driver.execute_script(
            "arguments[0].setAttribute('value',arguments[1])",
            first_name_field, new_first_name)

    def change_lastname_field(self):
        last_name_field = self.find_element(
            AccountPageLocator.LOCATOR_LAST_NAME_FIELD)
        self.driver.execute_script(
            "arguments[0].setAttribute('value',arguments[1])",
            last_name_field, new_last_name)

    def save_change(self):
        button_save = self.find_element(
            AccountPageLocator.LOCATOR_BUTTON_SAVE)
        button_save.click()
