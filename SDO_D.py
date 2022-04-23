from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from to_import import acceptConsent, closeExponeaBanner, URL_SDO, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
import requests
from import_test_units_Xpaths import rowKarty_imgHoteluKarty_D

SDOsectionXpath = "//*[@class='sdo-section']"

def SDO_D(self, driver):
    generalDriverWaitImplicit(self.driver)
    rowKarty_imgHoteluKarty_D(self, self.driver)

    SDOsectionElement = self.driver.find_element_by_xpath(SDOsectionXpath)

    assert SDOsectionElement.is_displayed() == True
    print("sdo section visible true :  " + str(SDOsectionElement.is_displayed()))
class TestSDO_D(unittest.TestCase):
    def setUp(self):
        setUp(self)
    def tearDown(self):
        tearDown(self)
    def test_SDO_D(self):
        self.driver.maximize_window()
        self.driver.get(URL_SDO)

        time.sleep(0.3)
        acceptConsent(self.driver)
        SDO_D(self, self.driver)
