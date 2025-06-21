import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

@pytest.fixture()
def setup(browser):  # browser will come from the CLI option
    if browser == "chrome":
        service = ChromeService("D:\\pythonTesting\\Chrome_driver\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        print("Launching Chrome browser...")
    elif browser == "firefox":
        service = FirefoxService("D:\\pythonTesting\\Firefox_driver\\geckodriver.exe")
        driver = webdriver.Firefox(service=service)
        print("Launching Firefox browser...")
    elif browser == "edge":
        service = EdgeService("D:\\pythonTesting\\Edge_driver\\msedgedriver.exe")
        driver = webdriver.Edge(service=service)
        print("Launching Edge browser...")
    else:
        raise Exception("Browser not supported: " + browser)

    driver.maximize_window()
    return driver
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome | firefox | edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"