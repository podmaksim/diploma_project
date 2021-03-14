from selenium.webdriver.common.by import By


class UserPageLocator:

    LOCATOR_BUTTON_EDIT_ACCOUNT = (By.XPATH,
                                   '//div[@class="content"]'
                                   '//a[@href="http://localhost/litecart'
                                   '/en/edit_account"]')
