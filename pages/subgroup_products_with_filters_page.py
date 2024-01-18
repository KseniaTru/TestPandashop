import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class SubgroupProductsWithFiltersPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    manufacturer_slider = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/form/div[1]/div[2]/div[3]/div[2]'
    amt_gastroguss_checkbox = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/form/div[1]/div[2]/div[3]/ul/li[1]/label'
    ballarini_checkbox = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/form/div[1]/div[2]/div[3]/ul/li[6]/label'
    berghoff_checkbox = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/form/div[1]/div[2]/div[3]/ul/li[7]/label'
    berlinger_haus_checkbox = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/form/div[1]/div[2]/div[3]/ul/li[8]/label'
    bollire_checkbox = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/form/div[1]/div[2]/div[3]/ul/li[11]/label'
    cucina_italiana_checkbox = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/form/div[1]/div[2]/div[3]/ul/li[14]/label'
    fissman_checkbox = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/form/div[1]/div[2]/div[3]/ul/li[20]/label'
    price_left_slider = '//div[@aria-valuenow="100"]'
    open_products_type_button = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/form/div[3]/div[1]/div[1]/i'
    universal_checkbox = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/form/div[3]/div[1]/div[3]/ul/li[7]/label'
    open_diameter_button = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/form/div[3]/div[2]/div[1]/i'
    max_diameter_field = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/form/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/input'
    open_material_button = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/form/div[3]/div[3]/div[1]/i'
    aluminum_checkbox = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/form/div[3]/div[3]/div[3]/ul/li[1]/label'
    open_internal_coating_button = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/form/div[3]/div[4]/div[1]/i'
    stone_non_stick_checkbox = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/form/div[3]/div[4]/div[3]/ul/li[3]/label'
    open_features_button = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/form/div[3]/div[5]/div[1]/i'
    cover_included_checkbox = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/form/div[3]/div[5]/div[3]/ul/li[2]/label'
    product_name = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/a/span'
    product_price = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/span[2]'
    add_to_cart_button = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div[1]'
    enter_to_cart_button = '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div[2]/a'
    title_cart = '/html/body/div[1]/div[2]/div/div/form/div[1]/div/div[1]'

    # Getters
    def get_manufacturer_slider(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.manufacturer_slider)))

    def get_amt_gastroguss_checkbox(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.amt_gastroguss_checkbox)))

    def get_ballarini_checkbox(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.ballarini_checkbox)))

    def get_berghoff_checkbox(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.berghoff_checkbox)))

    def get_berlinger_haus_checkbox(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.berlinger_haus_checkbox)))

    def get_bollire_checkbox(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.bollire_checkbox)))

    def get_cucina_italiana_checkbox(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.cucina_italiana_checkbox)))

    def get_fissman_checkbox(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.fissman_checkbox)))

    def get_price_left_slider(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.price_left_slider)))

    def get_open_products_type_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.open_products_type_button)))

    def get_universal_checkbox(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.universal_checkbox)))

    def get_open_diameter_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.open_diameter_button)))

    def get_max_diameter_field(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.max_diameter_field)))

    def get_open_material_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.open_material_button)))

    def get_aluminum_checkbox(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.aluminum_checkbox)))

    def get_open_internal_coating_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.open_internal_coating_button)))

    def get_stone_non_stick_checkbox(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.stone_non_stick_checkbox)))

    def get_open_features_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.open_features_button)))

    def get_cover_included_checkbox(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.cover_included_checkbox)))

    def get_product_name(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.product_name)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.product_price)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_enter_to_cart_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.enter_to_cart_button)))

    def get_title_cart(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.title_cart)))

    # Actions
    def click_amt_gastroguss_checkbox(self):
        self.get_amt_gastroguss_checkbox().click()
        print('Click amt gastroguss checkbox')

    def click_ballarini_checkbox(self):
        self.get_ballarini_checkbox().click()
        print('Click ballarini checkbox')

    def click_berghoff_checkbox(self):
        self.get_berghoff_checkbox().click()
        print('Click berghoff checkbox')

    def click_berlinger_haus_checkbox(self):
        self.get_berlinger_haus_checkbox().click()
        print('Click berlinger haus checkbox')

    def click_bollire_checkbox(self):
        self.get_bollire_checkbox().click()
        print('Click bollire checkbox')

    def click_cucina_italiana_checkbox(self):
        self.get_cucina_italiana_checkbox().click()
        print('Click cucina italiana checkbox')

    def click_fissman_checkbox(self):
        self.get_fissman_checkbox().click()
        print('Click fissman checkbox')

    def click_open_products_type_button(self):
        self.get_open_products_type_button().click()
        print('Click open products type button')

    def click_universal_checkbox(self):
        self.get_universal_checkbox().click()
        print('Click universal checkbox')

    def click_open_diameter_button(self):
        self.get_open_diameter_button().click()
        print('Click open diameter button')

    def input_max_diameter_field(self, max_diameter):
        self.get_max_diameter_field().send_keys(max_diameter)
        print('Input max diameter field')

    def click_open_material_button(self):
        self.get_open_material_button().click()
        print('Click open material button')

    def click_aluminum_checkbox(self):
        self.get_aluminum_checkbox().click()
        print('Click aluminum checkbox')

    def click_open_internal_coating_button(self):
        self.get_open_internal_coating_button().click()
        print('Click open internal coating button')

    def click_stone_non_stick_checkbox(self):
        self.get_stone_non_stick_checkbox().click()
        print('Click stone non stick checkbox')

    def click_open_features_button(self):
        self.get_open_features_button().click()
        print('Click open features button')

    def click_cover_included_checkbox(self):
        self.get_cover_included_checkbox().click()
        print('Click cover included checkbox')

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print('Click add to cart button')

    def click_enter_to_cart_button(self):
        self.get_enter_to_cart_button().click()
        print('Click enter to cart button')

    # Methods
    def applying_filters_and_selection_product(self):
        self.get_current_url()
        time.sleep(3)
        self.driver.execute_script('window.scrollTo(0, 500)')
        print('Scroll down')
        time.sleep(3)
        self.click_amt_gastroguss_checkbox()
        time.sleep(3)
        self.click_ballarini_checkbox()
        time.sleep(3)
        self.click_berghoff_checkbox()
        time.sleep(3)
        self.click_berlinger_haus_checkbox()
        time.sleep(3)
        self.move_slider(self.get_manufacturer_slider(), 0, 30)
        time.sleep(3)
        self.click_bollire_checkbox()
        time.sleep(3)
        self.move_slider(self.get_manufacturer_slider(), 0, 30)
        time.sleep(3)
        self.click_cucina_italiana_checkbox()
        time.sleep(3)
        self.move_slider(self.get_manufacturer_slider(), 0, 30)
        time.sleep(3)
        self.move_slider(self.get_manufacturer_slider(), 0, 30)
        time.sleep(3)
        self.click_fissman_checkbox()
        time.sleep(3)
        self.driver.execute_script('window.scrollTo(0, 700)')
        print('Scroll down')
        time.sleep(3)
        self.move_slider(self.get_price_left_slider(), 10, 0)
        time.sleep(3)
        self.driver.execute_script('window.scrollTo(0, 1000)')
        print('Scroll down')
        time.sleep(3)
        self.click_open_products_type_button()
        time.sleep(3)
        self.click_universal_checkbox()
        time.sleep(3)
        self.driver.execute_script('window.scrollTo(0, 1200)')
        print('Scroll down')
        time.sleep(3)
        self.click_open_diameter_button()
        time.sleep(3)
        self.input_max_diameter_field('30')
        time.sleep(3)
        self.driver.execute_script('window.scrollTo(0, 1500)')
        print('Scroll down')
        time.sleep(3)
        self.click_open_material_button()
        time.sleep(3)
        self.click_aluminum_checkbox()
        time.sleep(3)
        self.click_open_internal_coating_button()
        time.sleep(3)
        self.click_stone_non_stick_checkbox()
        time.sleep(3)
        self.driver.execute_script('window.scrollTo(0, 1700)')
        print('Scroll down')
        time.sleep(3)
        self.click_open_features_button()
        time.sleep(3)
        self.click_cover_included_checkbox()
        time.sleep(3)
        self.driver.execute_script('window.scrollTo(0, 500)')
        print('Scroll up')
        time.sleep(3)
        print('Product name is: ')
        self.turning_into_text(self.get_product_name())
        time.sleep(3)
        print('Product price is: ')
        self.turning_into_text(self.get_product_price())
        time.sleep(3)
        self.click_add_to_cart_button()
        time.sleep(3)
        self.click_enter_to_cart_button()
        time.sleep(3)
        self.check_word(self.get_title_cart(), 'Ваша корзина')
