from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from to_import import acceptConsent, URL_FM, sendEmail, setUp, tearDown, URL_exotika, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from import_test_units_Xpaths import rowKarty_imgHoteluKarty_D, imgHotelKartaXpath, destinationXpath, gridDestinationXpath

class Test_FM_Exotika_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_FM_D(self):
        self.driver.get(URL_FM)
        self.driver.maximize_window()
        time.sleep(0.3)
        acceptConsent(self.driver)
        generalDriverWaitImplicit(self.driver)
        rowKarty_imgHoteluKarty_D(self, self.driver)
        assert (self.driver.find_element_by_xpath(imgHotelKartaXpath)).is_displayed() == True
        assert (self.driver.find_element_by_xpath(destinationXpath)).is_displayed() == True
        assert (self.driver.find_element_by_xpath(gridDestinationXpath)).is_displayed() == True

    def test_Exotika_D(self):
        self.driver.get(URL_exotika)
        self.driver.maximize_window()
        time.sleep(0.3)
        acceptConsent(self.driver)
        rowKarty_imgHoteluKarty_D(self, self.driver)
        assert (self.driver.find_element_by_xpath(imgHotelKartaXpath)).is_displayed() == True
        assert (self.driver.find_element_by_xpath(gridDestinationXpath)).is_displayed() == True