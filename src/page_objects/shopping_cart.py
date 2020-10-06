from selenium.webdriver.support import expected_conditions as EC

from src.locators.shopping_cart_locators import ShoppingCartLocator
from src.page import Page


class ShoppingCart(Page):

    def bin_btn(self):
        return self.wait.until(EC.element_to_be_clickable(ShoppingCartLocator.bin_btn_locator))

    def empty_state(self):
        return self.wait.until(EC.presence_of_element_located(ShoppingCartLocator.empty_state_locator))
