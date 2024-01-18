import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class CategoryPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    subcategory_button = '/html/body/div[1]/div[2]/div/div/div[1]/div/nav/ul/li[3]/div/a'
    title_subcategory = '//h1[@class="h-lnkBack"]'

    # Getters
    def get_subcategory_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.subcategory_button)))

    def get_title_subcategory(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.title_subcategory)))

    # Actions
    def click_subcategory_button(self):
        self.get_subcategory_button().click()
        print('Click subcategory button')

    # Methods
    def selection_subcategory(self):
        self.get_current_url()
        time.sleep(3)
        self.click_subcategory_button()
        time.sleep(3)
        self.check_word(self.get_title_subcategory(), 'Посуда')
