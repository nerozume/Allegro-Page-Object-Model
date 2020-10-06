import unittest
import datetime
import pyderman as driver
from selenium import webdriver

from src.page_objects.item_details import ItemDetails
from src.page_objects.shopping_cart import ShoppingCart
from src.page_objects.subcategory import SubCategory
from src.page_objects.homepage import Homepage
from src.page_objects.motorization import Motorization


class TestAllegro(unittest.TestCase):

    def setUp(self):
        path = driver.install(browser=driver.firefox)
        self.driver = webdriver.Firefox(executable_path=path)
        print("Browser Started at :" + str(datetime.datetime.now()))
        self.driver.get("https://allegro.pl")
        cookies = Homepage(self.driver)
        cookies.cookie_btn().click()

    def testAddToCart(self):
        Homepage(self.driver).motorization_btn().click()
        Motorization(self.driver).winter_tire_btn().click()
        subcategory = SubCategory(self.driver)
        subcategory.minimum_price_textbox(200)
        subcategory.select_8th_item().click()
        add_to_cart = ItemDetails(self.driver)
        add_to_cart.add_to_cart_btn().click()
        add_to_cart.shopping_cart_btn().click()
        shopping_cart = ShoppingCart(self.driver)
        assert not (shopping_cart.empty_state()).is_displayed()
        self.driver.close()
