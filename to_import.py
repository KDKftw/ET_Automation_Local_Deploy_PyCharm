from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import smtplib, ssl
from email.mime.text import MIMEText
from to_import_secret import emailPass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
URL = "https://www.etravel.cz/"
URL_FM = URL+"first-minute"
URL_exotika = URL + "exoticka-dovolena"
URL_LM = URL+"last-minute"
#URL_SRL = URL+"vysledky-vyhledavani?d=63220|63281|63373|63442|63311|63314|63316|63319|63324|63333|63390|63402|63408|63409|63471|63219|63341|63428&tt=0&to=4305|4309|2682|4308|4312&dd=2022-09-01&rd=2022-09-25&nn=7|8|9&ka1=5&kc1=1&ac1=2"
#URL_SRL = URL+"vysledky-vyhledavani?d=64419|64420|64425|64423&tt=0&to=4305|4309|2682|4308|4312&dd=2022-09-01&rd=2022-09-25&nn=7|8|9&ka1=5&kc1=1&ac1=2"
URL_SRL = URL + "vysledky-vyhledavani?d=63213|63241|63360|63267|74459|74460|63284|74464|63350|63354|74465|63216|63226|63242|63244|74462|63313|74461|74463|63349|63455&tt=0&to=4305|4309|2682|4308|4312&dd=2022-07-01&rd=2022-08-31&nn=7|8|9&ka1=6&kc1=1&ac1=2"
URL_detail = URL + "egypt/hurghada/hurghada/mirage-bay-resort-a-aqua-park-hurghada?DS=1024&GIATA=16351&D=64419|64420|64425|64423&HID=5057&MT=5&RT=15&NN=7&DF=2022-07-01|2022-08-31&RD=2022-07-20&DD=2022-07-13&AC1=2&KC1=1&KA1=5&IC1=0&DP=2682&MNN=7&NNM=7|8|9&TT=1&TTM=1&PID=33040&DPR=EXIM%20TOURS"
#URL_detail = URL+"recko/lefkada/nidri/delfini-penzion?ds=1024&giata=538958&hid=141090&nn=7&df=2022-07-01|2022-09-01&rd=2022-09-01&dd=2022-08-25&ac1=2&kc1=1&ka1=5&tt=1&pid=335821&d=63220|63281|63373|63442|63311|63314|63316|63319|63324|63333|63390|63402|63408|63409|63471|63219|63341|63428&mt=2&rt=15&dp=4305&mnn=7&nnm=7|8|9&ttm=1&dpr=EXIM%20TOURS&sortby=Price&sortorder=0"
URL_detail_all_inclusive = URL_detail + "&mmt=5"
URL_detail_airport_praha = URL_detail + "&tom=4312"
URL_FT_results = URL + "hledani-vysledky?q="
URL_groupsearch = URL + "vysledky-vyhledavani?tt=1&dd=2022-08-04&rd=2022-09-30&nn=7|8|9&ka1=5&kc1=1&ac1=2"
def setUp(self):
  self.driver = webdriver.Chrome(ChromeDriverManager().install())
  generalDriverWaitImplicit(self.driver)
  #self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
  #self.driver = webdriver.Opera(executable_path=OperaDriverManager().install())
  #self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

def tearDown(self):
  self.driver.quit()

def generalDriverWaitImplicit(driver):
  driver.implicitly_wait(25)
def acceptConsent(driver):
  driver.maximize_window()
  generalDriverWaitImplicit(driver)
  generalDriverWaitImplicit(driver)
  # time.sleep(5)
  try:
    element = driver.execute_script(
      """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
    print(element)
  except NoSuchElementException:
    print("NOSUCH")
  except TimeoutException:
    pass

  if element != None:
    element.click()

  else:
    print("consent pass")
    pass

def returnLocatorForMealHotelKarty(poziceHotelu):
    string1 = "/ html / body / div[ @ id = 'app'] / div[ @ id = 'c_page-mainSearch'] / div[ @class ='hotel-results-section'] / div[@ class ='hotel-results-content'][1] / div[@ class ='tile-hotel-section'] / div[@ class ='items'] / div[@ class ='flex']["
    stringVariable = poziceHotelu
    stringVariable = str(stringVariable)
    string2 = "] / a[@ class ='c_tile-hotel'] / div[@ class ='inner'] / div[@ class ='section-border'] / div[@ class ='c_row'][2] / span[1]"
    finalString = string1 + stringVariable + string2
    finalString = finalString.replace(" ", "")
    #print(finalString)
    return str(finalString)

def sendEmail(msg):
  fromx = 'alertserverproblem@gmail.com'
  to = 'ooo.kadoun@gmail.com'
  msg = MIMEText(msg)
  msg['Subject'] = "SRWEB1"
  msg['From'] = fromx
  msg['To'] = to

  server = smtplib.SMTP('smtp.gmail.com:587')
  server.starttls()
  server.ehlo()
  server.login("alertserverproblem@gmail.com", emailPass)
  server.sendmail(fromx, to, msg.as_string())
  server.quit()

def acceptConsent5(driver):
  time.sleep(2)
  try:
    element = driver.execute_script(
      """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
  except NoSuchElementException:
    return

  except TimeoutException:
    pass
  try:
    element.click()
  except TimeoutException:
    pass
  except NoSuchElementException:
    return

def closeExponeaBanner(driver):
    time.sleep(1.5)
    wait = WebDriverWait(driver, 150000)
    driver.maximize_window()
    try:
      exponeaBanner = driver.find_element_by_xpath("//*[@class='exponea-popup-banner']")
      if exponeaBanner.is_displayed():
        wait.until(EC.visibility_of(exponeaBanner))
        exponeaCrossAndBanner = driver.find_element_by_xpath(
          "//*[@class='exponea-popup-banner']//*[@class='exponea-close']")
        exponeaCrossAndBanner.click()
        time.sleep(2)

    except NoSuchElementException:
      print("nenasle se exponea banner")

def acceptConsent3(driver):
  time.sleep(2)

  element = driver.execute_script(
      """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
  if element !=0:

      pass

  else:
      element.click()


desired_cap = {
"os" : "Windows",
"os_version" : "11",
"browser" : "Edge",
"browser_version" : "latest",
"browserstack.local" : "false",
"browserstack.selenium_version" : "3.5.2"
}