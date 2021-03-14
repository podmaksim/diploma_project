from selenium.webdriver.common.by import By


class CartPageLocator:

    LOCATOR_CHANGE_QUANTITY = (By.CSS_SELECTOR, '[name="quantity"]')
    LOCATOR_UPDATE_BUTTON = (By.XPATH, '//button[@name="update_cart_item"]')
    LOCATOR_QUANTITY_IN_CART = (By.XPATH,
                                '//div[@id="order_confirmation-wrapper"]'
                                '//td[@style="text-align: center;"]')
    LOCATOR_COST_CART = (By.XPATH,
                         '//div[@id="order_confirmation-wrapper"]'
                         '//td[@class="sum"]')
    LOCATOR_BUTTON_REMOVE = (By.XPATH, '//button[@name="remove_cart_item"]')
    LOCATOR_EMPTY_CART = (By.XPATH, '//div[@id="checkout-cart-wrapper"]//em')
