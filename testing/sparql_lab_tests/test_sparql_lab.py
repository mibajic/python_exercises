import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys


class CorrectQueriesChecker(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\mbajic\Documents\python\testing\sparql_lab_tests\chromedriver.exe')

    def test_load_test_cases(self):
        global url
        global query
        for test_case, url_and_query in self.test_cases_dict.items():
            # print("Test case: {}, URL:{}, query: {}".format(test_case, url_and_query[0], url_and_query[1]))
            url = url_and_query[0]
            query = url_and_query[1]
            # print("url is: ", url)
            # print("query is: ", query)
            self.query_checker_helper(url, query)

    test_cases_dict = {1: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/describe-dimensions",
                           'PREFIX qb: <http://purl.org/linked-data/cube#> \n'
                           'DESCRIBE ?dimension \n WHERE { \n   ?dimension a qb:DimensionProperty . \n } '],
                       2: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes-histogram",
                           'SELECT ?class (COUNT(?s) AS ?count) \n WHERE { \n ?s a ?class . \n } '
                           '\n GROUP BY ?class \n ORDER BY DESC(?count)']}

    def query_checker_helper(self, url, query):
        self.driver.get(url)
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "CodeMirror-scroll")))
        editor = self.driver.find_element_by_css_selector('.CodeMirror  textarea')
        editor.send_keys(Keys.CONTROL + "a")
        editor.send_keys(Keys.DELETE)
        editor.send_keys(query)
        send_button = self.driver.find_element_by_xpath('//button[text()="Submit"]')
        send_button.click()
        self.driver.implicitly_wait(20)
        checkmark = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/h2/i')
        assert checkmark.is_displayed()

    def tearDown(self):
        time.sleep(60)
        # self.driver.close()


CorrectQueriesChecker()

if __name__ == "__main__":
    unittest.main()
