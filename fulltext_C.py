from selenium.common.exceptions import NoSuchElementException
from to_import import acceptConsent, URL, setUp, tearDown, URL_FT_results, generalDriverWaitImplicit
import time
import unittest
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
query = "Mirage bay"


querySDO = ["Zanzibar", "Řecko", "Turecko", "Egypt", "Kapverdy", "Oman" , "Maledivy", "Dubaj", "Mallorca", "Bulharsko", "Chorvatsko", "Kefalonia", "Attika" ]
queryCommon = ["pojištění",  "parkování", "covid", "Funtazie" ]
queryHotely = ["Mirage bay",  "Prima life", "Prima life makadi", "Pegasos", "Pickalbatros", "Titanic", "mirage", "Bay & Mare",  "A for Art",
               "Porto Skala 7", "Costa Azzurra", "La Cite",  "Stefanos", "Magnolia",  "White Gold", "King Tut Resort", "Blue Waters",
               "Primasol", "Doubletree"]
queryList = querySDO+queryCommon+queryHotely
#queryList = queryHotely
failed_query = ["mitsis","Domes Aulüs","Naftilos", ]

HPLupaFullTextXpath = "//*[@class='f_icon f_icon--magnifier']"
#HPinputBoxFullTextXpath = "//*[@class='flex-grow outline-none px-2 py-2 bg-transparent']"
HPinputBoxFullTextXpath = "//*[@class='grow outline-none px-2 py-2 bg-transparent']"
fullTextNaseptavacKartaHoteluXpath = "//*[@class='aspect-w-16 aspect-h-10']"
fullTextNaseptavacTextResultsXpath = "//*[@class='text-base']"
fullTextResultsKartaHoteluXpath = "//*[@class='aspect-w-16 aspect-h-10']"
fullTextResultsKartaHoteluHrefXpath="//*[@class='my-4 grid gap-4 grid-cols-2 sm:grid-cols-3']/a"
fullTextResultsTextHrefXpath="//*[@class='space-y-2 py-4']/a"
class Test_Fulltext_C(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_fulltext_naseptavac(self):
        wait = WebDriverWait(self.driver, 35)
        poziceQueryItem = 0
        for _ in queryList:
            self.driver.get(URL)

            if poziceQueryItem == 0:
                acceptConsent(self.driver)
                self.driver.maximize_window()
            else:
                pass

            FTlupa = self.driver.find_element_by_xpath(HPLupaFullTextXpath)
            wait.until(EC.visibility_of(FTlupa)).click()
            #inputBox =
            # inputBox.send_keys(queryList[poziceQueryItem])
            time.sleep(0.7)
            generalDriverWaitImplicit(self.driver)
            #wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPinputBoxFullTextXpath))).send_keys(queryList[poziceQueryItem])
            self.driver.find_element_by_xpath(HPinputBoxFullTextXpath).send_keys(queryList[poziceQueryItem])
            time.sleep(0.7)
            # inputBox.send_keys(Keys.ENTER)
            print(queryList[poziceQueryItem].upper())
            poziceQueryItem = poziceQueryItem + 1

            # if self.driver.find_element_by_xpath("//*[@class='f_tileGrid-item']").isDisplayed()==True:
            # if hotelDlazdice != 0:

            try:
                wait.until(EC.visibility_of(self.driver.find_element_by_xpath(fullTextNaseptavacKartaHoteluXpath)))
                try:

                    # hotelDlazdice = self.driver.find_element_by_xpath("//*[@class='f_tileGrid-item']")
                    #wait.until(EC.visibility_of(self.driver.find_element_by_xpath("//*[@class='f_tile f_tile--tour']"))).click()
                    wait.until(EC.visibility_of(
                        self.driver.find_element_by_xpath(fullTextNaseptavacKartaHoteluXpath))).click()

                    # hotelDlazdice.click()
                    currentUrl = self.driver.current_url
                    print("hote dlazdice klik")
                    assert currentUrl != URL
                    testOK_asserted = True
                except NoSuchElementException:
                    print("first no such ele except")
                    testOK_asserted = False
                    pass
            except NoSuchElementException:
                testOK_asserted = False
                pass

            if testOK_asserted == False:
                try:
                    #prvniItem =
                    wait.until(EC.visibility_of(self.driver.find_elements_by_xpath(fullTextNaseptavacTextResultsXpath)[0])).click()
                    # prvniItem[0].click()
                    print("last no such ele except")
                    currentUrl = self.driver.current_url
                    assert currentUrl != URL
                    response = requests.get(currentUrl)
                    assert response.status_code == 200

                except NoSuchElementException:
                    print("first no such ele except")
                    pass
                currentUrl = self.driver.current_url
                assert currentUrl != URL
            else:
                pass

    def test_fulltext_results_status_check(self):
        wait = WebDriverWait(self.driver, 13)
        poziceQueryItem=0
        for _ in queryList:
            driver = self.driver
            driver.get(URL_FT_results+queryList[poziceQueryItem])
            if poziceQueryItem==0:
                acceptConsent(driver)
                self.driver.maximize_window()
            else:
                pass
            print(queryList[poziceQueryItem].upper())
            linksToCheckList = []
            try:
                vysledkyDlazdiceHotelu = driver.find_elements_by_xpath(fullTextResultsKartaHoteluHrefXpath)
               # wait.until(EC.visibility_of(vysledkyDlazdiceHotelu[0]))
                x = 0
                for _ in vysledkyDlazdiceHotelu:
                    linksToCheckList.append(vysledkyDlazdiceHotelu[x].get_attribute("href"))
                    x = x + 1
            except NoSuchElementException:
                pass
            #print(linksToCheckList)
            vysledkyTextItems = driver.find_elements_by_xpath(fullTextResultsTextHrefXpath)
            vysledkyTextItemsSingle = driver.find_element_by_xpath(fullTextResultsTextHrefXpath)
            #wait.until(EC.visibility_of(vysledkyTextItems[0]))
            wait.until(EC.visibility_of(vysledkyTextItemsSingle))
            z = 0
            for _ in vysledkyTextItems:
                    linksToCheckList.append(vysledkyTextItems[0].text)
                    z = z + 1

            #print(linksToCheckList)
            poziceQueryItem=poziceQueryItem+1
            #print(len(linksToCheckList))
            assert len(linksToCheckList) > 0        ## check if there are any result, length > 0
            y = 0
            #for _ in linksToCheckList:
            if len(linksToCheckList) > 5:
                for i in range(5):
                    response = requests.get(linksToCheckList[y])
                    assert response.status_code == 200
                    #print(response.status_code)
                    #print(response.status_code == 200)

                    y = y + 1
            else:
                for _ in linksToCheckList:
                    #print(response.status_code)
                    #print(response.status_code == 200)
                    assert response.status_code == 200
                    y = y + 1