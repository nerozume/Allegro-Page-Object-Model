from selenium.webdriver.common.by import By


class ShoppingCartLocator(object):
    bin_btn_locator = (By.CSS_SELECTOR, "._d8zz0")
    empty_state_locator = (By.XPATH, "//div[@class='main-wrapper']//div[1]/div[2]//span[.='Twój koszyk jest pusty']")
