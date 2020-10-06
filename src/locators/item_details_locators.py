from selenium.webdriver.common.by import By


class ItemDetailsLocators(object):
    add_to_cart_btn_locator = (By.ID, "add-to-cart-button")
    shopping_cart_btn_locator = (By.XPATH, "//a[.='przejdź do koszyka']")
