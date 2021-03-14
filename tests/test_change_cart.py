from pages.main_page import MainPage
from pages.selection_page import SelectionPage
from pages.cart_page import CartPage
from time import sleep


def test_login(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.choice_duck()
    selection_page = SelectionPage(browser)
    selection_page.add_to_cart()
    sleep(3)
    selection_page.go_to_cart()
    sleep(3)
    cart_page = CartPage(browser)
    cart_page.change_quantity()
    sleep(3)
    cart_page.update_cart()
    sleep(3)
    cart_page.check_quantity()
    sleep(3)
    cart_page.cart_cost()
    sleep(3)
    cart_page.remove_cart()
    sleep(3)
    cart_page.check_empty_cart()
    sleep(3)
