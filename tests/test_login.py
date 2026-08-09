import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.AccountPage import AccountPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities import ExcelUtils
from tests.BaseTest import BaseTest


class TestLogin(BaseTest):
    @pytest.mark.parametrize("email_address,password",ExcelUtils.get_data_from_excel("ExcelFiles/TutorialsNinja1.xlsx","LoginTest"))

    def test_login_with_valid_credentials(self,email_address,password):
        home_page=HomePage(self.driver)
        login_page=home_page.navigate_to_login_page()
        account_page=login_page.login_to_application(email_address,password)
        assert account_page.display_status_of_edit_your_account_information_option()
    # time.sleep(10)

    def test_login_with_invalid_email_and_valid_password(self):
        home_page=HomePage(self.driver)
        login_page=home_page.navigate_to_login_page()
        login_page.login_to_application(self.generate_email_with_time_stamp(),"Kavyareddy")
        login_page.wait_to_load_warning_message()
        expected_warning_message="Warning: No match for E-Mail Address and/or Password."
        actual_warning_message=login_page.retrieve_warning_message()
        assert expected_warning_message == actual_warning_message

    def test_login_with_valid_email_and_invalid_password(self):
        home_page=HomePage(self.driver)
        login_page=home_page.navigate_to_login_page()
        login_page.login_to_application("kavyareddynellipudi@gmail.com","Kavya@202520252025")
        login_page.wait_to_load_warning_message()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        actual_warning_message = login_page.retrieve_warning_message()
        assert expected_warning_message in actual_warning_message

    def test_login_without_entering_credentials(self):
        home_page=HomePage(self.driver)
        login_page=home_page.navigate_to_login_page()
        login_page.login_to_application("","")
        login_page.wait_to_load_warning_message()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        actual_warning_message = login_page.retrieve_warning_message()
        assert expected_warning_message in actual_warning_message







