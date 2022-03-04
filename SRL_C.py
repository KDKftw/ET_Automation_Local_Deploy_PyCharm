
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from to_import import acceptConsent, closeExponeaBanner, URL_SRL, sendEmail, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
totalPriceXpath = "//*[@class='price-amount']"
odNejdrazsihoSorterXpath = "//*[contains(text(), 'od nejdražšího')]"
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