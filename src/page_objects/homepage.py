from src.locators.homepage_locators import HomepageLocators
from src.page import Page


class Homepage(Page):

    def motorization_btn(self):
        return self.driver.find_element(*HomepageLocators.motorization_btn_locator)

    def cookie_btn(self):
        return self.driver.find_element(*HomepageLocators.cookie_btn_locator)
