from selenium.webdriver.common.by import By


class Subcategory_locator(object):
    minimum_price_textbox_locator = (By.ID, "price_from")
    select_8th_item_locator = (By.XPATH, "//article[8]")
