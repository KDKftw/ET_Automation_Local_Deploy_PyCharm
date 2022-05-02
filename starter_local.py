#from Detail_D import *
from Detail_C import *
from FM_Exotika_D import *
from fulltext_C import *
from groupsearch_D import *
from HP_D import *
from LM_D import *

from SDO_D import *
from SRL_C import *
from SRL_D import *
from HP_C import *
import HtmlTestRunner

def suite():
    suite = unittest.TestSuite()
    #suite.addTest(TestDetailHotelu_D("test_detail_D"))
    suite.addTest(TestDetailHotelu_C("test_detail_fotka"))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal"))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_airport"))
    suite.addTest(Test_FM_Exotika_D("test_FM_D"))
    suite.addTest(Test_FM_Exotika_D("test_Exotika_D"))
    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac"))
    suite.addTest(Test_Fulltext_C("test_fulltext_results_status_check"))
    suite.addTest(Test_Groupsearch_D("test_groupsearch_D"))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch'))
    suite.addTest(Test_HP_C('test_HP_banner_destination_to_SDO'))
    suite.addTest(Test_HP_D("test_HP_D"))
    suite.addTest(Test_LM_D("test_LM_D"))
    suite.addTest(TestSDO_D('test_SDO_D'))
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest'))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive'))
    suite.addTest(Test_SRL_C('test_SRL_map'))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava'))
    suite.addTest(Test_SRL_C('test_srl_C'))
    suite.addTest(TestSRL_D('test_SRL_D'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch'))
    suite.addTest(Test_HP_C('test_HP_banner_destination_to_SDO'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    #outfile = open("C:\Users\KDK\Desktop\HTML_TEST_REPORTS\sest_results.html", "w")
    outfile = open("results.html", "w")
    #runner = HTMLTestRunner.HTMLTestRunner(
     #   stream=outfile,
      #  title='Test Report',
       # description='This demonstrates the report output by Prasanna.Yelsangikar.')

    #runner = HtmlTestRunner(title='My unit test', open_in_browser=True)
    #runner = HtmlTestRunner.HTMLTestRunner(output='example_dir')        ## this is ??
    runner = HtmlTestRunner.HTMLTestRunner(log=True, verbosity=2, output='ETRAVEL-Web Suite test', title='ETRAVEL-Web Suite test'+URL, report_name='ETRAVEL-Web Suite test',
                            open_in_browser=True, description="ETRAVEL-Web Suite test")

    runner.run(suite())