from selenium.webdriver.common.by import By


class CommonPageLocator:

    LOCATOR_GO_TO_CART = (By.XPATH,
                          '//div[@id="cart"]//a[@class="link"]')
