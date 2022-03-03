from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from to_import import acceptConsent, URL_FM, sendEmail, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

kartaHoteluXpath = "//*[@class='splide__slide splide__slide--clone']"
rowKartyHoteluXpath = "//*[@class='sdo-tile-section']"

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
        time.sleep(5)
        rowKartyHoteluElement = self.driver.find_elements_by_xpath(rowKartyHoteluXpath)
        try:
            rowKartyHoteluElement = self.driver.find_elements_by_xpath(kartaHoteluXpath)
            if rowKartyHoteluElement[0].is_displayed():
                for WebElement in rowKartyHoteluElement:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        print("JDOU VIDET")
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Problem s FM - zajezdy se neukazuji " + url
                        sendEmail(msg)
                        print("else rowKartyHotelu")
        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s FM - zajezdy se neukazuji " + url
            print("NoSuchElementException - rowKartyHotelu")
            sendEmail(msg)

        assert rowKartyHoteluElement[0].is_displayed() == True