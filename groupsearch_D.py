from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from to_import import acceptConsent, URL_groupsearch, setUp, tearDown
import unittest
from selenium.webdriver.support import expected_conditions as EC
emptyImgInTeaserDestinationXpath = "background-image: url('https://cdn.fischer.cz/Images/000000/1200x0.jpg');"
teaserItemsXpath = "//*[@class='c_tile-category']"
destinationsHighlightXpath = "//*[@class='c_title large center']"
class Test_Groupsearch_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_groupsearch_D(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 150000)
        self.driver.get(URL_groupsearch)
        self.driver.maximize_window()
        acceptConsent(self.driver)
        teaserItems = driver.find_elements_by_xpath(teaserItemsXpath)
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
            print("no such")
        assert destinationsHL[0].is_displayed() == True