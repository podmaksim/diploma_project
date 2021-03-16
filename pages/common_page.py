from pages.selection_page import SelectionPage
from locators.common_page_locator import CommonPageLocator


class CommonPage(SelectionPage):

    def click_go_to_cart_link(self):
        link_cart = self.find_element(
            CommonPageLocator.LOCATOR_GO_TO_CART)
        link_cart.click()
