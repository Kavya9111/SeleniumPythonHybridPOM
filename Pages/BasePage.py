from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self,driver):
        self.driver=driver

    # def type(self,text,locator):
    #     element=None
    #     if locator.__contains__("_id"):
    #         element=self.driver.find_element(By.ID,locator)
    #     elif locator.__contains__("_name"):
    #         element=self.driver.find_element(By.NAME,locator)
    #     elif locator.__contains__("_class_name"):
    #         element=self.driver.find_element(By.CLASS_NAME,locator)
    #     elif locator.__contains__("_link_text"):
    #         element=self.driver.find_element(By.LINK_TEXT,locator)
    #     elif locator.__contains__("_xpath"):
    #         element=self.driver.find_element(By.XPATH,locator)
    #     elif locator.__contains__("_css"):
    #         element=self.driver.find_element(By.CSS_SELECTOR,locator)
    #     element.click()
    #     element.clear()
    #     element.send_keys(text)  or we can also write.

    def type_into_element(self,text,locator_name,locator_value):
        element=self.get_element(locator_name,locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    # def element_click(self,locator):
    #     element=None
    #     if locator.__contains__("_id"):
    #         element=self.driver.find_element(By.ID,locator)
    #     elif locator.__contains__("_name"):
    #         element=self.driver.find_element(By.NAME,locator)
    #     elif locator.__contains__("_class_name"):
    #         element=self.driver.find_element(By.CLASS_NAME,locator)
    #     elif locator.__contains__("_link_text"):
    #         element=self.driver.find_element(By.LINK_TEXT,locator)
    #     elif locator.__contains__("_xpath"):
    #         element=self.driver.find_element(By.XPATH,locator)
    #     elif locator.__contains__("_css"):
    #         element=self.driver.find_element(By.CSS_SELECTOR,locator)
    #     element.click() or here code is duplicating so we are taking "get" method.

    def element_click(self,locator_name,locator_value):
        element=self.get_element(locator_name,locator_value)
        element.click()

    def check_display_status_of_element(self,locator_name,locator_value):
        element=self.get_element(locator_name,locator_value)
        return element.is_displayed()

    def retrieve_element_text(self,locator_name,locator_value):
        element=self.get_element(locator_name,locator_value)
        return element.text

    def get_element(self,locator_name,locator_value):

        print("================================")
        print("locator_name:", locator_name)
        print("locator_value:", locator_value)
        print("locator_value type:", type(locator_value))
        print("================================")

        element = None

        if locator_name.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)

        elif locator_name.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)

        elif locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)

        elif locator_name.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)

        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)

        elif locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)

        return element


        # if locator_name.__contains__("_id"):
        #     element = self.driver.find_element(By.ID, locator_value)
        # elif locator_name.__contains__("_name"):
        #     element = self.driver.find_element(By.NAME, locator_value)
        # elif locator_name.__endswith__("_xpath"):
        #     element = self.driver.find_element(By.XPATH,locator_value)
        # elif locator_name.__contains__("_class_name"):
        #     element = self.driver.find_element(By.CLASS_NAME, locator_value)
        # elif locator_name.__contains__("_link_text"):
        #     element = self.driver.find_element(By.LINK_TEXT, locator_value)
        # elif locator_name.__contains__("_xpath"):
        #     element = self.driver.find_element(By.XPATH, locator_value)
        # elif locator_name.__contains__("_css"):
        #     element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        # return element



