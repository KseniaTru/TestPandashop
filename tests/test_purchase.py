import time
from selenium import webdriver

from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.group_products_page import GroupProductsPage
from pages.last_page import LastPage
from pages.login_page import LoginPage
from pages.order_registration_page import OrderRegistrationPage
from pages.profile_page import ProfilePage
from pages.subcategory_page import SubcategoryPage
from pages.subgroup_products_with_filters_page import SubgroupProductsWithFiltersPage


def test_purchase(set_up):
    driver = webdriver.Firefox()

    """AUTHORIZATION"""
    lp = LoginPage(driver)
    lp.login()

    """SELECTION CATEGORY"""
    pp = ProfilePage(driver)
    pp.selection_category()

    """SELECTION SUBCATEGORY"""
    cp = CategoryPage(driver)
    cp.selection_subcategory()

    """SELECTION GROUP OF PRODUCTS"""
    sp = SubcategoryPage(driver)
    sp.selection_group_products()

    """SELECTION SUBGROUP OF PRODUCTS"""
    gpp = GroupProductsPage(driver)
    gpp.selection_subgroup_products()

    """APPLYING FILTERS AND SELECTION PRODUCT"""
    spwfp = SubgroupProductsWithFiltersPage(driver)
    spwfp.applying_filters_and_selection_product()

    """ORDER REGISTRATION"""
    cp = CartPage(driver)
    cp.order_registration()

    """INPUT USER`S INFO AND MAKING ORDER"""
    orp = OrderRegistrationPage(driver)
    orp.making_order()

    """LAST PAGE INFO"""
    # last_page = LastPage(driver)
    # last_page.check_order_number()

    time.sleep(3)

    driver.close()
