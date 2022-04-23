from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from to_import import acceptConsent, URL, setUp, tearDown, generalDriverWaitImplicit
import unittest
from selenium.webdriver.support import expected_conditions as EC
from groupsearch_D import groupSearch_D
import time
from SRL_D import SRL_D
from SDO_D import SDO_D
HPvyhledatZajezdyButtonXpath = "//*[@class='f_filterMainSearch'] //*[contains(text(), 'Vyhledat dovolenou')]"
HPkamPojedeteButtonXpath = "//*[contains(text(), 'Kam se chystáte?')]"
HPzlutakEgyptDestinaceXpath = "//*[@class='f_filterMainSearch']//*[@class='flex flex-row overflow-hidden']//*[@class='flex flex-col pb-2']//*[contains(text(), 'Egypt')]"
#HPzlutakReckoDestinaceXpath = "/html/body[@id='homepage']/header[@class='f_pageHeader js_header f_set--filterOpened']/div[@class='f_pageHeader-content']/div[@class='f_pageHeader-item f_pageHeader-item--holder']/div/div[@class='f_filterMainSearch']/div/div[2]/span/div[@class='f_filterHolder f_set--active']/div[@class='f_filterHolder-content']/div[@class='f_filter f_filter--destination']/div[@class='f_customScroll js_destinationsContent']/div[1]/div[@class='f_column']/div[@class='f_column-item'][1]/div[@class='f_list']/div[@class='f_list-item'][1]/div[@class='f_input-wrapper']/label[@class='f_input f_input--checkbox']/span[@class='f_input-content']"
HPzlutakPokracovatButtonXpath = "//*[contains(text(), 'Pokračovat')]"
#HPzlutakPokracovatButtonXpathStep2 = "/html/body[@id='homepage']/header[@class='f_pageHeader js_header f_set--filterOpened']/div[@class='f_pageHeader-content']/div[@class='f_pageHeader-item f_pageHeader-item--holder']/div/div[@class='f_filterMainSearch']/div/div[2]/span/div[@class='f_filterHolder f_set--active']/div[@class='f_filterHolder-footer js_filter-footer']/div[@class='f_filterHolder-footer-item'][2]/a[@class='f_button f_button--common']/span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right']"
HPzlutakPokracovatButtonXpathStep2 = "//*[@class='f_filterHolder js_filterHolder f_set--active']//*[@class='c_btn blue-dark']"
HPzlutakLetniPrazdninyXpath = "//*[@class='f_filterHolder js_filterHolder f_set--active']//*[@class='flex flex-col gap-2']//*[contains(text(), 'Letní prázdniny 2022')]"
#HPzlutakPokracovatButtonXpathStep3 = "/html/body[@id='homepage']/header[@class='f_pageHeader js_header f_set--filterOpened']/div[@class='f_pageHeader-content']/div[@class='f_pageHeader-item f_pageHeader-item--holder']/div/div[@class='f_filterMainSearch']/div/div[2]/span/div[@class='f_filterHolder f_set--active']/div[@class='f_filterHolder-footer js_filter-footer']/div[@class='f_filterHolder-footer-item'][2]/a[@class='f_button f_button--common']/span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right']"
HPzlutakPridatPokojXpath = "//*[contains(text(), 'přidat pokoj')]"
HPzlutakObsazenost2plus1Xpath = "//*[contains(text(), 'Rodina')]"
HPzlutakPotvrditAvyhledatXpath = "//*[@class='f_filterHolder js_filterHolder f_set--active']//*[contains(text(), 'Potvrdit a vyhledat')]"
HPnejlepsiZajezdySwitchButtonXpath = "//*[@class='f_switch-button']"
HPnejlepsiZajezdyVypisXpath = "//*[@class='f_tourTable-tour']"
HPstatyKartyXpath = "//*[@class='content']"

class Test_HP_C(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_HP_zlutak_to_groupsearch(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)

        acceptConsent(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)     ##time sleep not the best not pog but it works =)
        groupSearch_D(self, self.driver)

    def test_HP_zlutak_to_SRL(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)

        acceptConsent(self.driver)
        time.sleep(1)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPkamPojedeteButtonXpath))).click()
        time.sleep(0.3)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakEgyptDestinaceXpath))).click()

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpath))).click()
        time.sleep(1.5)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpathStep2))).click()

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakLetniPrazdninyXpath))).click()
        time.sleep(0.5)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpathStep2))).click()

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakObsazenost2plus1Xpath))).click()

        time.sleep(1)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPotvrditAvyhledatXpath))).click()
        SRL_D(self, self.driver)

    def test_HP_banner_destination_to_SDO(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)

        acceptConsent(self.driver)
        time.sleep(1)
        HPstatyKartyElement=self.driver.find_element_by_xpath(HPstatyKartyXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", HPstatyKartyElement)

        time.sleep(0.666)
        HPstatyKartyElement.click()
        time.sleep(6.666)
        SDO_D(self, self.driver)