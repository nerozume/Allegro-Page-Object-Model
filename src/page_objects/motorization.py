from selenium.webdriver.support import expected_conditions as EC

from src.locators.motorization_locators import MotorizationLocators
from src.page import Page


class Motorization(Page):

    def winter_tire_btn(self):
        return self.wait.until(EC.presence_of_element_located(MotorizationLocators.winter_tires_btn_locator))
