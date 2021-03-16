from pages.selection_page import SelectionPage
from locators.cart_page_locator import CartPageLocator


class CartPage(SelectionPage):

    def set_duck_quantity_in_cart(self, quantity):
        change_quantity_field = self.find_element(
            CartPageLocator.LOCATOR_CHANGE_QUANTITY)
        self.driver.execute_script(
            "arguments[0].setAttribute('value',arguments[1])",
            change_quantity_field, quantity)

    def click_update_cart_button(self):
        button_update = self.find_element(
            CartPageLocator.LOCATOR_UPDATE_BUTTON)
        button_update.click()

    def check_quantity(self, expected_quantity):
        quantity_field = self.find_element(
            CartPageLocator.LOCATOR_QUANTITY_IN_CART)
        assert quantity_field.text == expected_quantity

    def cart_cost(self, expected_cost):
        cost_field = self.find_element(
            CartPageLocator.LOCATOR_COST_CART)
        assert cost_field.text == expected_cost

    def click_remove_cart_button(self):
        button_remove = self.find_element(
            CartPageLocator.LOCATOR_BUTTON_REMOVE)
        button_remove.click()

    def check_empty_cart(self):
        empty_cart_field = self.find_element(
            CartPageLocator.LOCATOR_EMPTY_CART)
        assert empty_cart_field.text == 'There are no items in your cart.'
