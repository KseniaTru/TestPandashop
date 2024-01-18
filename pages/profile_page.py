import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class ProfilePage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    catalog_button = '//span[@class="headerMain-barsCnt-link"]'
    category_button = '/html/body/div[1]/header/div/div/div[2]/div/div/div[1]/div[1]/ul/li[3]/a/span[2]'
    title_category = '//h1[@class="h-lnkBack"]'

    # Getters
    def get_catalog_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_category_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.category_button)))

    def get_title_category(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.title_category)))

    # Actions
    def click_catalog_button(self):
        self.get_catalog_button().click()
        print('Click catalog button')

    def click_category_button(self):
        self.get_category_button().click()
        print('Click category button')

    # Methods
    def selection_category(self):
        self.get_current_url()
        time.sleep(3)
        self.click_catalog_button()
        time.sleep(3)
        self.click_category_button()
        time.sleep(3)
        self.check_word(self.get_title_category(), 'Дом и сад')
