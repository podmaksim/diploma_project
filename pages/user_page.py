from pages.main_page import MainPage
from locators.user_page_locator import UserPageLocator


class UserPage(MainPage):

    def button_edit_account_click(self):
        button_edit_account = self.find_element(
            UserPageLocator.LOCATOR_BUTTON_EDIT_ACCOUNT)
        button_edit_account.click()
