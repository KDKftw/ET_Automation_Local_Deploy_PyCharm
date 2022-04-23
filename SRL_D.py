from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from to_import import acceptConsent, closeExponeaBanner, URL_SRL, sendEmail, setUp, tearDown, returnLocatorForMealHotelKarty, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
import pyautogui as p


SRLhotelyKartyXpath = "//*[@class='flex']"
#SRLfotkaHoteluXpath = "//*[@class='img-wrap']"
SRLfotkaHoteluXpath= "//*[@class='splide__slide is-active is-visible']"
totalPriceXpath = "//*[@class='price-amount']"

def SRL_D(self, driver):
    self.driver.implicitly_wait(100)
    generalDriverWaitImplicit(self.driver)
    wait = WebDriverWait(self.driver, 150)
    hotelySingle = self.driver.find_element_by_xpath(SRLhotelyKartyXpath)
    try:
        hotelySingle = self.driver.find_element_by_xpath(SRLhotelyKartyXpath)  ##
        hotelyAll = self.driver.find_elements_by_xpath(SRLhotelyKartyXpath)
        wait.until(EC.visibility_of(hotelySingle))
        ##print(hotelyAll)
        if hotelySingle.is_displayed():
            for WebElement in hotelyAll:
                jdouvidet = WebElement.is_displayed()
                print(jdouvidet)
                assert jdouvidet == True
                if jdouvidet == True:
                    pass

                else:
                    url = self.driver.current_url
                    msg = " Problem s hotely v searchi - hotelCard " + url
                    sendEmail(msg)
    except NoSuchElementException:
        url = self.driver.current_url
        msg = "Problem s hotely v searchi - hotelCard " + url
        sendEmail(msg)
    generalDriverWaitImplicit(self.driver)
    assert hotelySingle.is_displayed() == True

    try:
        self.driver.implicitly_wait(100)
        fotkyAll = self.driver.find_elements_by_xpath(SRLfotkaHoteluXpath)  ##
        fotkaSingle = self.driver.find_element_by_xpath(SRLfotkaHoteluXpath)
        wait.until(EC.visibility_of(fotkaSingle))
        ##print(fotkaSingle)
        if fotkaSingle.is_displayed():
            for WebElement in fotkyAll:
                jdouvidet = WebElement.is_displayed()
                print(jdouvidet)
                assert jdouvidet == True
                if jdouvidet == True:
                    pass
                else:
                    url = self.driver.current_url
                    msg = " Problem s fotkami hotelu v searchi " + url
                    sendEmail(msg)

    except NoSuchElementException:
        url = self.driver.current_url
        msg = " Problem s fotkami hotelu v searchi " + url
        sendEmail(msg)

    try:
        self.driver.implicitly_wait(100)
        cenaAll = self.driver.find_elements_by_xpath(totalPriceXpath)  ##
        cenaSingle = self.driver.find_element_by_xpath(totalPriceXpath)
        wait.until(EC.visibility_of(cenaSingle))
        if cenaSingle.is_displayed():
            for WebElement in cenaAll:
                jdouvidet = WebElement.is_displayed()
                assert jdouvidet == True
                if jdouvidet == True:
                    print("ceny")
                    pass

                else:
                    url = self.driver.current_url
                    msg = " Problem s cenami hotelu v searchi " + url
                    sendEmail(msg)


    except NoSuchElementException:
        url = self.driver.current_url
        msg = "Problem s cenami hotelu v searchi " + url
        sendEmail(msg)

    assert cenaAll[0].is_displayed() == True

class TestSRL_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_SRL_D(self):
        wait = WebDriverWait(self.driver, 150)
        self.driver.maximize_window()
        self.driver.get(URL_SRL)

        time.sleep(0.44)
        acceptConsent(self.driver)

        SRL_D(self, self.driver)
