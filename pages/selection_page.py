from pages.main_page import MainPage
from locators.selection_page_locator import SelectionPageLocator


class SelectionPage(MainPage):

    def add_to_cart(self):
        button_add = self.find_element(
            SelectionPageLocator.LOCATOR_ADD_TO_CART_BUTTON)
        button_add.click()
