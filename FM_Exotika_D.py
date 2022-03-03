from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from to_import import acceptConsent, URL_FM, sendEmail, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

kartaHoteluXpath = "//*[@class='splide__slide splide__slide--clone']"

class Test_FM_Exotika_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_FM_exotika_D(self):
        self.driver.get(URL_FM)
        wait = WebDriverWait(self.driver, 150)
        self.driver.maximize_window()
        acceptConsent(self.driver)
        try:
            kartaHoteluElement = self.driver.find_elements_by_xpath(kartaHoteluXpath)
            if kartaHoteluElement[0].is_displayed():
                for WebElement in kartaHoteluElement:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Problem s FM - zajezdy se neukazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s FM - zajezdy se neukazuji " + url
            sendEmail(msg)

        assert kartaHoteluElement[0].is_displayed() == True