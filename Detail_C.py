from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from to_import import acceptConsent, closeExponeaBanner, URL_detail, sendEmail, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
import requests
imageDetailFirstXpath = "//*[@id='splide01-slide01']/img"
terminyAcenyScrollMenuXpath = "/html/body/div[@id='app']/div/div[@class='c_hotel-anchor-nav']/div[@class='c_container']/ul[@class='c_customScroll']/li[2]/a"
stravovaniBoxTerminyAcenyXpath = "//*[contains(text(), 'Stravování')][1]"
class TestDetailHotelu_C(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def omlouvamese_paragraph(self):
        time.sleep(1)
        try:
            omlouvameParagraph = self.driver.find_element_by_xpath(
                "//*[@class='fshr-paragraph fshr-paragraph--centered']")
            if omlouvameParagraph.is_displayed():
                return

        except NoSuchElementException:
            pass

    def test_detail_fotka(self):
        self.driver.get(URL_detail)
        acceptConsent(self.driver)
        time.sleep(1)
        closeExponeaBanner(self.driver)
        imageDetail = self.driver.find_element_by_xpath(imageDetailFirstXpath)
        imageDetailSrc = imageDetail.get_attribute("src")
        print( imageDetailSrc)
        try:
            self.driver.set_page_load_timeout(5)
            self.driver.get(imageDetailSrc)
        except TimeoutException:
            url = self.driver.current_url
            msg = "Problem s fotkou src, detailhotelu,  TimeoutException " + url
            sendEmail(msg)
        try:
            image = self.driver.find_element_by_xpath("/html/body/img")
            assert image.is_displayed() == True
            if image.is_displayed():
                print("its ok")
        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s fotkou src, detailhotelu,  NoSuchElementException " + url
            sendEmail(msg)
        response = requests.get(imageDetailSrc)
        assert response.status_code == 200

    def test_detail_terminy_filtr_meal(self):
        self.driver.get(URL_detail)
        wait = WebDriverWait(self.driver, 150000)
        acceptConsent(self.driver)
        time.sleep(1)
        closeExponeaBanner(self.driver)
        try:
            terminyCeny = self.driver.find_element_by_xpath(terminyAcenyScrollMenuXpath)
            wait.until(EC.visibility_of(terminyCeny))
            ##terminyCeny.click()
            self.driver.execute_script("arguments[0].click();", terminyCeny)
        except NoSuchElementException:
            url = self.driver.current_url
            msg = "terminyAcenyScrollMenuXpath faild click " + url
            sendEmail(msg)
        try:
            stravovaniBox = self.driver.find_element_by_xpath(stravovaniBoxTerminyAcenyXpath)
            wait.until(EC.visibility_of(stravovaniBox))
            self.driver.execute_script("arguments[0].click();", stravovaniBox)
            time.sleep(20)
            try:
                stravyBox = self.driver.find_elements_by_xpath("//*[@name='detailFilterCatering']")

                self.driver.execute_script("arguments[0].click();", stravyBox[1])

                try:
                    self.driver.execute_script("arguments[0].click();",
                                               stravovaniBox)  ##workaround, klikni na box to confirm the choice

                except NoSuchElementException:
                    url = self.driver.current_url
                    msg = "stravaBox, potvrzeni stravy na detailu hotelu problém, NoSuchElementException " + url
                    sendEmail(msg)

            except NoSuchElementException:
                url = self.driver.current_url
                msg = "allInclusiveBox, zvolení stravy na detailu hotelu problém, NoSuchElementException " + url
                sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "stravovaniBox, otevření filtru stravování detail hotelu, NoSuchElementException " + url
            sendEmail(msg)

        zvolenaStravaVboxu = self.driver.find_element_by_xpath("//*[@class='js-subvalue f_text--highlighted']")
        zvolenaStravaVboxuString = zvolenaStravaVboxu.text
        print(zvolenaStravaVboxuString)

        stravaVterminech = self.driver.find_elements_by_xpath(
            "//*[@class='fshr-termin-catering js-tooltip js-tooltip--onlyDesktop']")
        stravaVterminechString = []

        ##ty for loopy se nezapnou pokud pocet vysledku bude 0
        ##takze treba exim a dx bude casto takto jelikoz se tam nabizi vsechny
        ##stravy, ne jen ty available
        x = 0
        for _ in stravaVterminech:
            stringos = stravaVterminech[x].text
            stravaVterminechString.append(stringos)
            x = x + 1

        time.sleep(1)  ###eroror element is not attached ?  tak chvilku cekacka mozna to solvne

        print(stravaVterminechString)
        y = 0
        for _ in stravaVterminechString:
            assert stravaVterminechString[y] == zvolenaStravaVboxuString
            if stravaVterminechString[y] == zvolenaStravaVboxuString:
                print("ok")
                ##print(y)
                y = y + 1
            else:
                url = self.driver.current_url
                msg = "na detailu jsem vyfiltroval stravu " + zvolenaStravaVboxuString + "ale pry to nesedi říká python" + url
                sendEmail(msg)
                y = y + 1
        time.sleep(1)
        ##print(stravaVterminech)