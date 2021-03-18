from pages.main_page import MainPage
from pages.selection_page import SelectionPage
from pages.common_page import CommonPage
from pages.cart_page import CartPage

from time import sleep


def test_change_cart(browser):
    duck_quantity = '3'
    duck_cost = '$60.00'
    duck_color = 'Red Duck'

    main_page = MainPage(browser)
    main_page.open_base_page()

    main_page.choice_duck(duck_color)

    selection_page = SelectionPage(browser)
    selection_page.add_to_cart()
    sleep(2)

    common_page = CommonPage(browser)
    common_page.click_go_to_cart_link()
    sleep(2)

    cart_page = CartPage(browser)
    cart_page.set_duck_quantity_in_cart(duck_quantity)
    sleep(3)
    cart_page.click_update_cart_button()
    sleep(3)
    cart_page.check_quantity(duck_quantity)
    sleep(3)
    cart_page.cart_cost(duck_cost)
    sleep(3)
    cart_page.click_remove_cart_button()
    sleep(3)
    cart_page.check_empty_cart()
    sleep(3)
