import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class LoginPage(Base):

    url = 'https://www.pandashop.md/ru/login/?returnurl=%2fru%2fprofile%2f'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    email = 'txtEmail'
    password = 'txtPassword'
    login_button = 'btnSignIn'
    profile_user_name = '//div[@class="profile-shortInfo-name"]'

    # Getters
    def get_email(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, self.login_button)))

    def get_profile_user_name(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.profile_user_name)))

    # Actions
    def input_email(self, email):
        self.get_email().send_keys(email)
        print('Input email')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input password')

    def click_login_button(self):
        self.get_login_button().click()
        print('Click login button')

    # Methods
    def login(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        time.sleep(3)
        self.input_email('evgenia.ya@ro.ru')
        time.sleep(3)
        self.input_password('123qweQWE')
        time.sleep(3)
        self.click_login_button()
        time.sleep(3)
        self.check_word(self.get_profile_user_name(), 'evgenia.evgenia')
