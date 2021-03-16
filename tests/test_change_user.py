from pages.main_page import MainPage
from pages.user_page import UserPage
from pages.account_page import AccountPage


def test_change_user(browser):
    user_email = 'podmaksim@gmail.com'
    user_password = '1111'
    new_first_name = 'Ilon'
    new_last_name = 'Mask'

    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.login(user_email, user_password)

    user_page = UserPage(browser)
    user_page.button_edit_account_click()

    account_page = AccountPage(browser)
    account_page.change_firstname_field(new_first_name)
    account_page.change_lastname_field(new_last_name)
    account_page.save_change()

    account_page.check_change_user(new_first_name, new_last_name)
