
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from to_import import acceptConsent, closeExponeaBanner, URL_SRL, sendEmail, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
import pyautogui as p
p.FAILSAFE = False
totalPriceXpath = "//*[@class='price-amount']"
odNejdrazsihoSorterXpath = "//*[contains(text(), 'od nejdražšího')]"
zobrazitNaMapeXpath = "//*[@class='c_btn white']"
detailHoteluButtonXpath = "//*[@class='c_btn inline ellipsis green']"
detailHoteluCenaAllXpath = "//*[@class='text-h3 text-green font-bold']"
detailHoteluCross = "//*[@class='f_icon f_icon--cross']"
class Test_SRL_C(unittest.TestCase):
    def setUp(self):
        setUp(self)
    def tearDown(self):
        tearDown(self)
    def test_SRL_sort_cheapest(self):

        self.driver.get(URL_SRL)
        wait = WebDriverWait(self.driver, 150)
        self.driver.maximize_window()
        acceptConsent(self.driver)
        cenaZajezduAllList = []  ##one list that takes prices from the srl
        cenaZajezduAllListSorted = []
        cenaZajezduAll = self.driver.find_elements_by_xpath(totalPriceXpath)
        poziceHotelu =0
        for WebElement in cenaZajezduAll:
            cenaZajezduAllString = cenaZajezduAll[poziceHotelu].text
            #enaZajezduAllString = cenaZajezduAllString[:-3]
            cenaZajezduAllString = ''.join(cenaZajezduAllString.split())  ##delete spaces
            cenaZajezduAllString = int(cenaZajezduAllString)  ##convert to int to do sort easily
            poziceHotelu = poziceHotelu + 1
            cenaZajezduAllList.append(cenaZajezduAllString)
            cenaZajezduAllListSorted.append(cenaZajezduAllString)

        cenaZajezduAllListSorted.sort()  ##sorting second list low to high

        if cenaZajezduAllListSorted == cenaZajezduAllList:  ##compare first list to second list, if is equal = good
            print("Razeni od nejlevnejsiho je OK")

        else:
            print("Razeni od nejlevnejsiho je spatne")

        #print(cenaZajezduAllList)
        #print(cenaZajezduAllListSorted)

        assert cenaZajezduAllListSorted == cenaZajezduAllList
    def test_SRL_sort_expensive(self):
        self.driver.get(URL_SRL)
        wait = WebDriverWait(self.driver, 1500)
        self.driver.maximize_window()
        acceptConsent(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(odNejdrazsihoSorterXpath))).click()
        time.sleep(4.5)   ##waits not working, for now just time sleep

        #wait.until(EC.visibility_of(self.driver.find_element_by_xpath(totalPriceXpath)))
        cenaZajezduAllList = []  ##one list that takes prices from the srl
        cenaZajezduAllListSorted = []
        cenaZajezduAll = self.driver.find_elements_by_xpath(totalPriceXpath)


        poziceHotelu = 0

        for WebElement in cenaZajezduAll:
            cenaZajezduAllString = cenaZajezduAll[poziceHotelu].text
            cenaZajezduAllString = ''.join(cenaZajezduAllString.split())  ##delete spaces
            cenaZajezduAllString = int(cenaZajezduAllString)  ##convert to int to do sort easily
            poziceHotelu = poziceHotelu + 1
            cenaZajezduAllList.append(cenaZajezduAllString)
            cenaZajezduAllListSorted.append(cenaZajezduAllString)

        cenaZajezduAllListSorted.sort(reverse=True)

        if cenaZajezduAllListSorted == cenaZajezduAllList:  ##compare first list to second list, if is equal = good
            print("Razeni od nejdrazsiho je OK")

        else:
            print("Razeni od nejdrazsiho je spatne")

        print(cenaZajezduAllList)
        print(cenaZajezduAllListSorted)

        assert cenaZajezduAllListSorted == cenaZajezduAllList
    def test_SRL_map(self):
        driver = self.driver
        driver.get(URL_SRL)
        wait = WebDriverWait(driver, 12)
        time.sleep(5)
        self.driver.maximize_window()
        acceptConsent(driver)
        #time.sleep(10)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(zobrazitNaMapeXpath))).click()



        time.sleep(4)  ##try except na kolecko, pokud ok tak click, nenajde tak pokracovat dal
        ##kolecka jsou definovany podle velikosti - small, medium, large; vzdy se meni v class name

        ##2x vyvolani na large kolecko (jsou destinace kde se musim kliknout na large vickrat
        ##ve vsech except je pass aby to nespadlo kdyby se large nenasel, goal toho testu je se pres mapu proklikat na detail hotelu
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-large leaflet-zoom-animated leaflet-interactive']"))).click()

        except NoSuchElementException:
            print("nenasel se large kolecko")
            pass
        except TimeoutException:
            print("nenasel se large kolecko")
            pass
        except ElementNotInteractableException:
            print("nenasel se medium kolecko ElementNotInteractableException")
            pass

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-large leaflet-zoom-animated leaflet-interactive']"))).click()

        except NoSuchElementException:
            print("nenasel se large kolecko")
            pass
        except TimeoutException:
            print("nenasel se large kolecko")
            pass
        except ElementNotInteractableException:
            print("nenasel se medium kolecko ElementNotInteractableException")
            pass

        ##Medium kolecko

        try:
            mediumKolecko = driver.find_elements_by_xpath(
                "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-medium leaflet-zoom-animated leaflet-interactive']")
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-medium leaflet-zoom-animated leaflet-interactive']"))).click()
            # wait.until(EC.element_to_be_clickable((By.XPATH,
            # "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-medium leaflet-zoom-animated leaflet-interactive']"))).execute_script("arguments[0].click();", mediumKolecko[1])
        except NoSuchElementException:
            print("nenasel se medium kolecko-NoSuchElementException")
            pass
        except TimeoutException:
            print("nenasel se medium kolecko - TimeoutExceptio")
            pass
        except ElementNotInteractableException:
            print("nenasel se medium kolecko ElementNotInteractableException")
            pass

        ##small kolecko

        try:
            koleckoCisloSmall = driver.find_element_by_xpath(
                "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-small leaflet-zoom-animated leaflet-interactive']")
            koleckoCisloSmall.click()
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-small leaflet-zoom-animated leaflet-interactive']"))).click()
        except NoSuchElementException:
            print("nenasel se small kolecko")
            pass
        except TimeoutException:
            print("nenasel se small kolecko")
            pass
        except ElementNotInteractableException:
            print("nenasel se small kolecko ElementNotInteractableException")
            pass

        time.sleep(3)

        actualHotelPin = driver.find_element_by_xpath(
            "//*[@class='leaflet-marker-icon leaflet-zoom-animated leaflet-interactive']")
        driver.execute_script("arguments[0].click();", actualHotelPin)  ##at this point im at detail hotelu na mapě

        try:
            imgMissing = driver.find_element_by_xpath(
                "//*[@class='f_image f_image--missing']")  ##when theres no photo on the detail on map theres actually class that says it is missing
            if imgMissing.is_displayed():  ##so if I dont find this class = good
                hotelBubble = driver.find_element_by_xpath("//*[@class='leaflet-popup-content'] //*[@class='f_bubble']")
                msg = "V mape v bublibně hotelu se nezobrazuje fotka hotelu " + hotelBubble.text
                sendEmail(msg)

        except NoSuchElementException:
            print("actually OK")


        hotelBubble = driver.find_element_by_xpath("//*[@class='leaflet-popup-content'] //*[@class='f_bubble']")
        hotelBubble.click()

        time.sleep(5)


        #assert (self.driver.current_url) != URL_SRL
        self.driver.switch_to.window(self.driver.window_handles[1]) ##gotta switch to new window
        currentUrl = self.driver.current_url
        print(currentUrl)
        print(URL_SRL)
        assert currentUrl != URL_SRL

    def test_srl_C(self):
        self.driver.get(URL_SRL)
        wait = WebDriverWait(self.driver, 150000)

        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(2)
        closeExponeaBanner(self.driver)


        try:
            wait.until(EC.visibility_of(self.driver.find_elements_by_xpath(totalPriceXpath[0])))
        except NoSuchElementException:
            url = self.driver.current_url
            msg = " Problem SRL hotelyAllKarty" + url
            sendEmail(msg)
        x = 4
        for WebElement in self.driver.find_elements_by_xpath(totalPriceXpath):

            print("|||||HOTEL CISLO|||||||")
            print(x + 1)
            print(x + 1)
            print(x + 1)

            wait.until(EC.visibility_of(self.driver.find_elements_by_xpath(totalPriceXpath)[0]))
            cenaZajezduAll = self.driver.find_elements_by_xpath(totalPriceXpath)
            cenaZajezduAllString = cenaZajezduAll[x].text
            print(cenaZajezduAllString)
            xBiggerThanFive = False
            if x > 4 :
                p.press("pagedown")

                time.sleep(3)
                xBiggerThanFive = True
                xBigger5end = True
            else:
                pass
            if x >10 and xBiggerThanFive == True:
                p.press("pagedown")
            else:
                pass
            if x > 15:
                p.press("pagedown", presses=3)
            else:
                pass

            wait.until(EC.visibility_of(self.driver.find_elements_by_xpath(detailHoteluButtonXpath)[x])).click()




            time.sleep(5)
            detailCenaAll = self.driver.find_element_by_xpath(detailHoteluCenaAllXpath)
            detailCenaAllString = detailCenaAll.text
            detailCenaAllString = detailCenaAllString[:-3]
            print(detailCenaAllString)



            assert detailCenaAllString == cenaZajezduAllString
            if detailCenaAllString == cenaZajezduAllString:
                print("ceny all sedi srl vs detail")

            else:
                print("ceny all NESEDÍ srl vs detail")

            ##todod click na cancle
            wait.until(EC.visibility_of(self.driver.find_element_by_xpath(detailHoteluCross))).click()

            x = x + 1
            print(x)
