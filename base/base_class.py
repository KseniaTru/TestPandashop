from datetime import datetime
from selenium.webdriver import ActionChains, Keys


class Base():
    def __init__(self, driver):
        self.driver = driver

    """GET CURRENT URL"""
    def get_current_url(self):
        url = self.driver.current_url
        print("Current url: " + url)

    """CHECK WORD"""
    def check_word(self, real_word, expect_word):
        real_word_text = real_word.text
        assert real_word_text == expect_word
        print("True word")

    """CHECK URL"""
    def check_url(self, expect_url):
        url = self.driver.current_url
        assert url == expect_url
        print("True url")

    """GET SCREENSHOT"""
    def get_screenshot(self):
        now_date = datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot" + now_date + ".png"
        self.driver.save_screenshot('/Users/Ksenia/PycharmProjects/homework_7_15/screen/' + name_screenshot)
        print("Screenshot done")

    """TURNING INTO TEXT"""
    def turning_into_text(self, locator):
        locator_text = locator.text
        print(locator_text)

    """CLICK, HOLD, SCROLL AND RELEASE"""
    def move_slider(self, locator, x, y):
        action = ActionChains(self.driver)
        action.click_and_hold(locator).move_by_offset(x, y).release().perform()
        print('Slider is moved')

    """CLEAR THE FIELD"""
    def clear_the_field(self, locator):
        locator.clear()
        print("Field is cleared")

    """DOWN THE LIST"""
    def down_the_list(self, locator):
        locator.send_keys(Keys.DOWN)
        print("Down the list")

    """POSITION SELECTION"""
    def position_selection(self, locator):
        locator.send_keys(Keys.RETURN)
        print("Position is selected")
