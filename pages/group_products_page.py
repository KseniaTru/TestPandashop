import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class GroupProductsPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    subgroup_products_button = '/html/body/div[1]/div[2]/div/div[2]/div[1]/div/nav/ul/li[5]/div/a'
    title_subgroup_products = '/html/body/div[1]/div[2]/div/div[2]/div[1]/div/h1'

    # Getters
    def get_subgroup_products_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.subgroup_products_button)))

    def get_title_subgroup_products(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.title_subgroup_products)))

    # Actions
    def click_subgroup_products_button(self):
        self.get_subgroup_products_button().click()
        print('Click subgroup products button')

    # Methods
    def selection_subgroup_products(self):
        self.get_current_url()
        time.sleep(3)
        self.click_subgroup_products_button()
        time.sleep(3)
        self.check_word(self.get_title_subgroup_products(), 'Сковороды')
