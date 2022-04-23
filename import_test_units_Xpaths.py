from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from to_import import acceptConsent, URL_FM, sendEmail, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

kartaHoteluXpath = "//*[@class='splide__slide splide__slide--clone']"
rowKartyHoteluXpath = "//*[@class='sdo-tile-section']"
#imgHotelKartaXpath = "//*[@class='c_tile-hotel-image'and not(@style='display: none;')]"
imgHotelKartaXpath = "//*[@class='splide__slide is-visible']"
destinationXpath = "//*[@class='destination-list']"
gridDestinationXpath = "//*[@class='c_grid cols-2']"


def rowKarty_imgHoteluKarty_D(self, driver):
    self.driver = driver
    wait = WebDriverWait(self.driver, 25)

    driver.implicitly_wait(150)
    wait.until(EC.visibility_of(self.driver.find_element_by_xpath(rowKartyHoteluXpath)))
    print("wait done")
    try:
        print("TRY block start")
        generalDriverWaitImplicit(self.driver)
        rowKartyHoteluElement = self.driver.find_elements_by_xpath(rowKartyHoteluXpath)
        #if rowKartyHoteluElement[2].is_displayed():
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

    driver.implicitly_wait(150)
    wait.until(EC.visibility_of(self.driver.find_element_by_xpath(imgHotelKartaXpath)))
    print("wait done")
    try:
        print("TRY block start")
        generalDriverWaitImplicit(self.driver)
        imgHoteluElement = self.driver.find_elements_by_xpath(imgHotelKartaXpath)
        if imgHoteluElement[3].is_displayed():
            for WebElement in imgHoteluElement:
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