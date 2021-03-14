from selenium.webdriver.common.by import By

new_first_name = 'Mask'
new_last_name = 'Ilon'


class CustomersPageLocator:

    LOCATOR_FIND_USER = (By.XPATH,
                         '//form[@name="customers_form"]'
                         '//tr[3]//td[5]//a[@href="http:'
                         '//localhost/litecart/admin'
                         '/?app=customers&doc='
                         'edit_customer&page=1&customer_id=3"]')
