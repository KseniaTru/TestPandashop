import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class LastPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    order_number = '/html/body/div[1]/div[2]/div/div/form/div[1]/div/div[2]/div'

    # Getters
    def get_order_number(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.order_number)))

    # Methods
    def check_order_number(self):
        self.get_current_url()
        time.sleep(3)
        print('Order number is: ')
        self.turning_into_text(self.get_order_number())
        time.sleep(3)
        self.check_url('https://www.pandashop.md/ru/cart/3/')
