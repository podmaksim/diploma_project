from pages.selection_page import SelectionPage
from locators.cart_page_locator import CartPageLocator

new_quantity = '3'
new_cost = '$60.00'


class CartPage(SelectionPage):

    def change_quantity(self):
        change_quantity_field = self.find_element(
            CartPageLocator.LOCATOR_CHANGE_QUANTITY)
        self.driver.execute_script(
            "arguments[0].setAttribute('value',arguments[1])",
            change_quantity_field, new_quantity)

    def update_cart(self):
        button_update = self.find_element(
            CartPageLocator.LOCATOR_UPDATE_BUTTON)
        button_update.click()

    def check_quantity(self):
        quantity_field = self.find_element(
            CartPageLocator.LOCATOR_QUANTITY_IN_CART)
        assert quantity_field.text == new_quantity

    def cart_cost(self):
        cost_field = self.find_element(
            CartPageLocator.LOCATOR_COST_CART)
        assert cost_field.text == new_cost

    def remove_cart(self):
        button_remove = self.find_element(
            CartPageLocator.LOCATOR_BUTTON_REMOVE)
        button_remove.click()

    def check_empty_cart(self):
        empty_cart_field = self.find_element(
            CartPageLocator.LOCATOR_EMPTY_CART)
        assert empty_cart_field.text == 'There are no items in your cart.'
