import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    product_name_in_cart = '/html/body/div[1]/div[2]/div/div/form/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/a/span'
    product_price_in_cart = '/html/body/div[1]/div[2]/div/div/form/div[1]/div/div[2]/div[2]/div[2]/div/div[2]'
    order_registration_button = 'btnNextStep'
    title_order_registration = '/html/body/div[1]/div[2]/div/div/form/div[1]/div[1]/div[2]/div[1]'

    # Getters
    def get_product_name_in_cart(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.product_name_in_cart)))

    def get_product_price_in_cart(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.product_price_in_cart)))

    def get_order_registration_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, self.order_registration_button)))

    def get_title_order_registration(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.title_order_registration)))

    # Actions
    def click_order_registration_button(self):
        self.get_order_registration_button().click()
        print('Click order registration button')

    # Methods
    def order_registration(self):
        self.get_current_url()
        time.sleep(3)
        print('Product name in cart is: ')
        self.turning_into_text(self.get_product_name_in_cart())
        time.sleep(3)
        print('Product price in cart is: ')
        self.turning_into_text(self.get_product_price_in_cart())
        time.sleep(3)
        self.click_order_registration_button()
        time.sleep(3)
        self.turning_into_text(self.get_title_order_registration())
