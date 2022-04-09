from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from to_import import acceptConsent, URL_FM, sendEmail, setUp, tearDown, URL_LM, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from import_test_units_Xpaths import rowKarty_imgHoteluKarty_D, imgHotelKartaXpath, destinationXpath, gridDestinationXpath

class Test_LM_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_LM_D(self):
        self.driver.get(URL_LM)
        self.driver.maximize_window()
        acceptConsent(self.driver)
        rowKarty_imgHoteluKarty_D(self, self.driver)
        generalDriverWaitImplicit(self.driver)
        assert (self.driver.find_element_by_xpath(destinationXpath)).is_displayed() == True