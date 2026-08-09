from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePage import BasePage


class AccountSuccess(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    account_creation_message_xpath = "//div[@id='content']/h1"

    # def wait_and_display_successful_message(self,locator):
    #     return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))

    def retrieve_account_creation_message(self):
        return self.retrieve_element_text("account_creation_message_xpath",self.account_creation_message_xpath)

