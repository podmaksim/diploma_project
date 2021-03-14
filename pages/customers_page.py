from pages.admin_page import AdminPage
from locators.customers_page_locator import CustomersPageLocator

new_first_name = 'Mask'
new_last_name = 'Ilon'


class CustomersPage(AdminPage):

    def find_user(self):
        our_user = self.find_element(
            CustomersPageLocator.LOCATOR_FIND_USER)
        assert our_user.text == f'{new_first_name} {new_last_name}'
