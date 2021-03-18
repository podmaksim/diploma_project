from pages.main_page import MainPage
from pages.user_page import UserPage
from pages.account_page import AccountPage
from pages.DB.db_def import check_change_user


def test_change_user(browser, user_change_config_data):
    user_email, user_password, \
    new_first_name, new_last_name = user_change_config_data
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.login(user_email, user_password)

    user_page = UserPage(browser)
    user_page.button_edit_account_click()

    account_page = AccountPage(browser)
    account_page.change_firstname_field(new_first_name)
    account_page.change_lastname_field(new_last_name)
    account_page.save_change()

    check_change_user(new_first_name, new_last_name)
