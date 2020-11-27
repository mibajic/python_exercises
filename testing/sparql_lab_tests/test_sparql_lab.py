import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data_test_suite_1 import test_cases_dict


class CorrectQueriesChecker(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\mbajic\Documents\python\testing\sparql_lab_tests"
                                                       r"\chromedriver.exe")

    def test_load_test_cases(self):
        global url
        global query
        for test_case, url_and_query in test_cases_dict.items():
            with self.subTest(test_case=test_case, url_and_query=url_and_query):
                url = url_and_query[0]
                query = url_and_query[1]
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
        # time.sleep(60)
        self.driver.close()


CorrectQueriesChecker()

if __name__ == "__main__":
    unittest.main()