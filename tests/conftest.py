import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from Utilities import ReadConfigurations

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),name="failed_test",attachment_type=AttachmentType.PNG)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_"+ rep.when, rep)
    return rep

@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info","browser").strip().lower()
    global driver
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    # Or we can also write the same statement in different way
    # elif browser == "edge": (both are same)
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")
    driver.maximize_window()
    app_url=ReadConfigurations.read_configuration("basic info","url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()