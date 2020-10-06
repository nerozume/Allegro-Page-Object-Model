import time

from selenium.webdriver.support import expected_conditions as EC

from src.locators.subcategory_locators import Subcategory_locator
from src.page import Page


class SubCategory(Page):

    def minimum_price_textbox(self, value):
        self.wait.until(EC.presence_of_element_located((Subcategory_locator.minimum_price_textbox_locator))).send_keys(
            value)

    def select_8th_item(self):
        time.sleep(3)
        return self.driver.find_element(*Subcategory_locator.select_8th_item_locator)
