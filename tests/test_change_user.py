from pages.main_page import MainPage
from pages.user_page import UserPage
from pages.account_page import AccountPage
from pages.admin_page import AdminPage
from pages.customers_page import CustomersPage
from time import sleep


def test_login(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.enter_email()
    main_page.enter_password()
    main_page.click_log()
    user_page = UserPage(browser)
    user_page.button_edit_account_click()
    account_page = AccountPage(browser)
    account_page.change_firstname_field()
    account_page.change_lastname_field()
    account_page.save_change()
    admin_page = AdminPage(browser)
    admin_page.open_admin_page()
    admin_page.enter_user_name()
    admin_page.enter_password()
    admin_page.click_login()
    sleep(3)
    admin_page.click_customers_icon()
    sleep(3)
    customers_page = CustomersPage(browser)
    customers_page.find_user()
