import pytest
import os
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Login:
    baseURL = ReadConfig.getApplicationURL()
    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("******* Starting test_002_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.targetpage = self.lp.isMyAccountPageExists()

        if self.targetpage is True:
            self.logger.info("******* Login Test Passed **********")
            self.driver.close()
            assert True
        else:
            screenshot_path = os.path.join(os.getcwd(), "screenshots", "test_login.png")
            self.driver.save_screenshot(screenshot_path)
            self.logger.error("******* Login Test Failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of test_002_login **********")
