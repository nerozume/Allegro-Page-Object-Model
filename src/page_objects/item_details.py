from selenium.webdriver.support import expected_conditions as EC

from src.locators.item_details_locators import ItemDetailsLocators
from src.page import Page


class ItemDetails(Page):

    def add_to_cart_btn(self):
        return self.wait.until(EC.presence_of_element_located(ItemDetailsLocators.add_to_cart_btn_locator))

    def shopping_cart_btn(self):
        return self.wait.until(EC.element_to_be_clickable(ItemDetailsLocators.shopping_cart_btn_locator))
