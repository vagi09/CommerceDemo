from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_link(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def is_displayed(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

        return bool(element)

    def get_title(self, title):

        WebDriverWait(self.driver, 10).until(EC.title_is(title))

        return self.driver.title

