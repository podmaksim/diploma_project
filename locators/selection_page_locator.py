from selenium.webdriver.common.by import By


class SelectionPageLocator:

    LOCATOR_ADD_TO_CART_BUTTON = (By.XPATH,
                                  '//button[@name="add_cart_product"]')
    LOCATOR_GO_TO_CART = (By.XPATH,
                          '//div[@id="cart"]//a[@class="link"]')
