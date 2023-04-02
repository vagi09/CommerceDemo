from config.config import TestData
from pages.Login_Page import LoginPage
from tests.test_base import BaseTest


class Test_Verify_Login(BaseTest):

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.login = LoginPage(driver)

    def test_title_verify(self):
        self.login = LoginPage(self.driver)
        title = self.login.get_title(TestData.NOPE_TITLE)

        assert title == TestData.NOPE_TITLE

    def test_login_into(self):
        self.login = LoginPage(self.driver)
        self.login.click_on_link()
        self.login.login_website(TestData.EMAIL, TestData.PASSWORD)
