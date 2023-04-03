from config.config import TestData
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    login_link = (By.XPATH, "//a[text()='Log in']")
    email = (By.XPATH, "//input[@id='Email']")
    password = (By.XPATH, "//input[@id='Password']")
    login_btn = (By.XPATH, "//button[normalize-space()='Log in']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_URL)

    def login_pg_title(self, title):
        return self.get_title(title)

    def login_website(self, un, pw, ):
        self.click_on_link(self.login_link)
        self.send_keys(self.email, un)
        self.send_keys(self.password, pw)
        self.click_on_link(self.login_btn)

    def login_btn_exist(self):
        return self.is_displayed(self.login_btn)
