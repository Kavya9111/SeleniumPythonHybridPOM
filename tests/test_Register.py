import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.HomePage import HomePage
from Pages.RegisterPage import RegisterPage
from Pages.AccountSuccessPage import AccountSuccess
from Utilities import ExcelUtils
from tests.BaseTest import BaseTest


class TestRegister(BaseTest):
    # def setup_method(self):
    #     self.driver.get("https://tutorialsninja.com/demo/")

    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page=home_page.navigate_to_register_page()
        account_success_page=register_page.register_an_account(
            ExcelUtils.get_cell_data("ExcelFiles/TutorialsNinja1.xlsx","RegisterTest",2,1),
            ExcelUtils.get_cell_data("ExcelFiles/TutorialsNinja1.xlsx","RegisterTest",2,2),
            self.generate_email_with_time_stamp(),
            ExcelUtils.get_cell_data("ExcelFiles/TutorialsNinja1.xlsx","RegisterTest",2,3),
            "kavya567","kavya567","no","select")

        expected_text = "Your Account Has Been Created!"
        actual_text = account_success_page.retrieve_account_creation_message()
        assert expected_text == actual_text

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page=home_page.navigate_to_register_page()
        account_success_page=register_page.register_an_account("Kavyasaireddy","Oni",self.generate_email_with_time_stamp(),"7123080905","kavya678","kavya678","yes","select")
        expected_text = "Your Account Has Been Created!"
        actual_text = account_success_page.retrieve_account_creation_message()
        assert expected_text == actual_text

    def test_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page=home_page.navigate_to_register_page()
        register_page.register_an_account("KavyaSai","Nellipudi","kavyanellipudi1991@gmail.com","7123050999","kavya123","kavya123","yes","select")
        expected_text = "Warning: E-Mail Address is already registered!"
        actual_text = register_page.retrieve_duplicate_email_warning_message()
        assert expected_text == actual_text

    def test_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        register_page=home_page.navigate_to_register_page()
        register_page.register_an_account("","","","","","","no","no")
        register_page.wait_and_load_warning_message((By.XPATH,register_page.privacy_policy_warning_xpath))
        assert register_page.verify_all_warnings("Warning: You must agree to the Privacy Policy!",
                                                 "First Name must be between 1 and 32 characters!",
                                                 "Last Name must be between 1 and 32 characters!",
                                                 "E-Mail Address does not appear to be valid!",
                                                 "Telephone must be between 3 and 32 characters!",
                                                 "Password must be between 4 and 20 characters!"
                                                 )








