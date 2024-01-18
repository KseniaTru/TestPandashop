import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class OrderRegistrationPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    user_name = 'name'
    locality = 'city'
    street = 'street-address'
    house_number = 'street-address-house'
    apartment_number = 'street-address-apartment'
    payment_online_radio_button = '/html/body/div[1]/div[2]/div/div/form/div[1]/div[1]/div[3]/label[4]'
    product_name_in_order = '//div[@class="cart-aside-prod-name"]'
    product_price_in_order = '//span[@class="text-nowrap"]'
    total_sum = 'cartItogoToPay'
    order_button = 'btnNextStep'
    title_last_page = '/html/body/div[1]/div[2]/div/div/form/div[1]/div/div[1]'

    # Getters
    def get_user_name(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, self.user_name)))

    def get_locality(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, self.locality)))

    def get_street(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, self.street)))

    def get_house_number(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, self.house_number)))

    def get_apartment_number(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, self.apartment_number)))

    def get_payment_online_radio_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.payment_online_radio_button)))

    def get_product_name_in_order(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.product_name_in_order)))

    def get_product_price_in_order(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.product_price_in_order)))

    def get_total_sum(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, self.total_sum)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, self.order_button)))

    def get_title_last_page(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.title_last_page)))


    # Actions
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('Input user name')

    def input_locality(self, locality):
        self.get_locality().send_keys(locality)
        print('Input locality')

    def input_street(self, street):
        self.get_street().send_keys(street)
        print('Input street')

    def input_house_number(self, house_number):
        self.get_house_number().send_keys(house_number)
        print('Input house number')

    def input_apartment_number(self, apartment_number):
        self.get_apartment_number().send_keys(apartment_number)
        print('Input apartment number')

    def click_payment_online_radio_button(self):
        self.get_payment_online_radio_button().click()
        print('Click payment online radio button')

    def click_order_button(self):
        self.get_order_button().click()
        print('Click order button')

    # Methods
    def making_order(self):
        self.get_current_url()
        time.sleep(3)
        self.clear_the_field(self.get_user_name())
        time.sleep(3)
        self.input_user_name('Evgenia')
        time.sleep(3)
        self.input_locality('Ungheni')
        time.sleep(3)
        self.input_locality('Ungheni') # вставить город нужно два раза, потому что с первого раза не вставляется
        time.sleep(3)
        self.down_the_list(self.get_locality())
        time.sleep(3)
        self.position_selection(self.get_locality())
        time.sleep(3)
        self.input_street('Mihai Eminescu')
        time.sleep(3)
        self.input_house_number('5')
        time.sleep(3)
        self.input_apartment_number('2')
        time.sleep(3)
        self.driver.execute_script('window.scrollTo(0, 500)')
        print('Scroll down')
        time.sleep(3)
        self.click_payment_online_radio_button()
        time.sleep(3)
        print('Product name in order is: ')
        self.turning_into_text(self.get_product_name_in_order())
        time.sleep(3)
        print('Product price in order is: ')
        self.turning_into_text(self.get_product_price_in_order())
        time.sleep(3)
        self.driver.execute_script('window.scrollTo(0, 900)')
        print('Scroll down')
        time.sleep(3)
        print('Total sum is: ')
        self.turning_into_text(self.get_total_sum())
        # time.sleep(3)
        # self.click_order_button()
        # time.sleep(3)
        # self.check_word(self.get_title_last_page(), 'Спасибо! Ваш заказ успешно оформлен!')

        # часть кода закомментированна, потому что там уже нужно делать настоящий заказ
