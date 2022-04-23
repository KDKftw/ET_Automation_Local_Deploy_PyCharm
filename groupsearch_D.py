from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from to_import import acceptConsent, URL_groupsearch, setUp, tearDown
import unittest
from selenium.webdriver.support import expected_conditions as EC
emptyImgInTeaserDestinationXpath = """//*[@style='background-image: url("https://cdn.fischer.cz/Images/000000/1200x0.jpg");']"""
empty1 = ''
teaserItemsXpath = "//*[@class='c_tile-category']"
destinationsHighlightXpath = "//*[@class='c_title large center']"

def groupSearch_D(self, driver):
    driver.implicitly_wait(100)
    teaserItems = driver.find_elements_by_xpath(teaserItemsXpath)
    wait = WebDriverWait(self.driver, 150)
    wait.until(EC.visibility_of(teaserItems[0]))
    try:
        for WebElement in teaserItems:
            ##print(len(teaserItems))
            jdouvidet = WebElement.is_displayed()
            ##print(jdouvidet)
            if jdouvidet == True:
                ##print(jdouvidet)
                ##print(WebElement)
                pass

            else:
                pass
                ##print("Else")
                ##emailfunciton



    except NoSuchElementException:
        pass
        ##print("no such")
        ##email fnction

    assert teaserItems[0].is_displayed() == True

    driver.implicitly_wait(100)
    destinationsHL = driver.find_elements_by_xpath(destinationsHighlightXpath)
    try:
        for WebElement in destinationsHL:
            ##print(len(srlItems))
            jdouvidet = WebElement.is_displayed()
            ##print(jdouvidet)
            if jdouvidet == True:
                ##print(jdouvidet)
                ##print(WebElement)
                pass

            else:
                pass
                print("Else")
    except NoSuchElementException:
        pass


    except NoSuchElementException:
        pass
        print("no such")
    assert destinationsHL[0].is_displayed() == True

    emptyImgsList = []
    emptyImgsListCounter = 0
    emptyImgs = driver.find_elements_by_xpath(emptyImgInTeaserDestinationXpath)
    try:
        emptyImgs = driver.find_elements_by_xpath(emptyImgInTeaserDestinationXpath)
        for WebElement in emptyImgs:
            emptyImgsList.append(emptyImgs[emptyImgsListCounter].text)
            print(emptyImgs[emptyImgsListCounter].text)
            emptyImgsListCounter = emptyImgsListCounter + 1

    except NoSuchElementException:
        pass

    print("následující destinace mají prázdný teaser obrazek")
    print(emptyImgsList)


class Test_Groupsearch_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_groupsearch_D(self):
        driver = self.driver
        self.driver.maximize_window()

        self.driver.get(URL_groupsearch)

        acceptConsent(self.driver)

        groupSearch_D(self, driver)