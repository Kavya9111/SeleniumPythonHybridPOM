from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.AccountSuccessPage import AccountSuccess
from Pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_filed_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    agree_field_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    yes_radio_button_xpath = "//input[@name='newsletter' and @value='1']"
    duplicate_email_warning_message_xpath="//div[contains(@class,'alert-danger') and (text()='Warning: E-Mail Address is already registered!')]"
    privacy_policy_warning_xpath = "(//div[contains(normalize-space(),'You must agree to the Privacy Policy!')])[2]"
    first_name_warning_message_xpath = "//div[contains(text(),'First Name must be between 1 and 32 characters!')]"
    last_name_warning_message_xpath = "//div[contains(text(),'Last Name must be between 1 and 32 characters!')]"
    email_warning_xpath = "//div[contains(text(),'E-Mail Address does not appear to be valid!')]"
    telephone_warning_xpath = "//div[contains(text(),'Telephone must be between 3 and 32 characters!')]"
    password_warning_xpath = "//div[contains(text(),'Password must be between 4 and 20 characters!')]"

    def enter_first_name(self,first_name_text):
        self.type_into_element(first_name_text,"first_name_field_id",self.first_name_field_id)

    def enter_last_name(self,last_name_text):
        self.type_into_element(last_name_text,"last_name_field_id",self.last_name_field_id)

    def enter_email(self,email_text):
        self.type_into_element(email_text,"email_field_id",self.email_field_id)

    def enter_telephone(self,telephone_text):
        self.type_into_element(telephone_text,"telephone_filed_id",self.telephone_filed_id)

    def enter_password(self,password_text):
        self.type_into_element(password_text,"password_field_id",self.password_field_id)

    def enter_password_confirm(self,password_text):
        self.type_into_element(password_text,"confirm_password_field_id",self.confirm_password_field_id)

    def select_agree_checkbox_field(self):
        self.element_click("agree_field_name",self.agree_field_name)

    def click_on_continue_button(self):
        self.element_click("continue_button_xpath",self.continue_button_xpath)
        return AccountSuccess(self.driver)

    def select_yes_radio_button(self):
        self.element_click("yes_radio_button_xpath",self.yes_radio_button_xpath)

    def register_an_account(self,first_name_text,last_name_text,email_text,telephone_text,password_text,password_confirm_text,yes_or_no,privacy_policy):
        self.enter_first_name(first_name_text)
        self.enter_last_name(last_name_text)
        self.enter_email(email_text)
        self.enter_telephone(telephone_text)
        self.enter_password(password_text)
        self.enter_password_confirm(password_confirm_text)
        if yes_or_no.__eq__("yes"):
            self.select_yes_radio_button()
        if privacy_policy.__eq__("select"):
            self.select_agree_checkbox_field()
        return self.click_on_continue_button()

    def wait_and_load_warning_message(self,locator):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))

    def retrieve_duplicate_email_warning_message(self):
        return self.retrieve_element_text("duplicate_email_warning_message_xpath",self.duplicate_email_warning_message_xpath)

    def retrieve_privacy_policy_warning_message(self):
        return self.retrieve_element_text("privacy_policy_warning_xpath",self.privacy_policy_warning_xpath)

    def retrieve_first_name_warning(self):
        return self.retrieve_element_text("first_name_warning_message_xpath",self.first_name_warning_message_xpath)

    def retrieve_last_name_warning(self):
        return self.retrieve_element_text("last_name_warning_message_xpath",self.last_name_warning_message_xpath)

    def retrieve_email_warning_message(self):
        return self.retrieve_element_text("email_warning_xpath",self.email_warning_xpath)

    def retrieve_telephone_warning(self):
        return self.retrieve_element_text("telephone_warning_xpath",self.telephone_warning_xpath)

    def retrieve_password_warning_message(self):
        return self.retrieve_element_text("password_warning_xpath",self.password_warning_xpath)

    def verify_all_warnings(self,expected_privacy_policy_warning_message,expected_first_name_warning_message,
                            expected_last_name_warning_message,
                            expected_email_message,expected_telephone_warning_message,expected_password_warning_message):
        actual_privacy_warning_message=self.retrieve_privacy_policy_warning_message()
        actual_first_name_warning_message = self.retrieve_first_name_warning()
        actual_last_name_warning_message=self.retrieve_last_name_warning()
        actual_email_warning_message=self.retrieve_email_warning_message()
        actual_telephone_warning_message=self.retrieve_telephone_warning()
        actual_password_warning_message=self.retrieve_password_warning_message()

        status = False

        if expected_privacy_policy_warning_message in actual_privacy_warning_message:
            if expected_first_name_warning_message == actual_first_name_warning_message:
                if expected_last_name_warning_message == actual_last_name_warning_message:
                    if expected_email_message == actual_email_warning_message:
                        if expected_telephone_warning_message == actual_telephone_warning_message:
                            if expected_password_warning_message == actual_password_warning_message:
                                status = True

        return status














