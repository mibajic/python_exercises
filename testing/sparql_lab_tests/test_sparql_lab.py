import unittest

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_cases_data import test_cases_dict_correct_queries_checker
from test_cases_data import test_cases_dict_wrong_queries_checker


class CorrectQueriesChecker(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/mbajic/Documents/python/'
                                                                        r'testing/sparql_lab_tests/chromedriver.exe')

    def test_load_test_cases(self):
        global url
        global query
        for test_case, url_and_query in test_cases_dict_correct_queries_checker.items():
            with self.subTest(test_case=test_case, url_and_query=url_and_query):
                url = url_and_query[0]
                query = url_and_query[1]
                self.driver.get(url)
                WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "CodeMirror-scroll")))
                editor = self.driver.find_element_by_css_selector('.CodeMirror  textarea')
                editor.send_keys(Keys.CONTROL + "a")
                editor.send_keys(Keys.DELETE)
                editor.send_keys(query)
                self.driver.find_element_by_xpath('//button[text()="Submit"]').click()
                check_mark = self.driver.find_element_by_css_selector("i.fa.fa-check.correct")
                assert check_mark.is_displayed()

    def tearDown(self):
        time.sleep(60)
    #   self.driver.close()


CorrectQueriesChecker()


class WrongQueriesChecker(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/mbajic/Documents/python/'
                                                                        r'testing/sparql_lab_tests/chromedriver.exe')

    def test_load_test_cases(self):
        global url
        global query
        for test_case, url_and_query in test_cases_dict_wrong_queries_checker.items():
            with self.subTest(test_case=test_case, url_and_query=url_and_query):
                url = url_and_query[0]
                query = url_and_query[1]
                self.driver.get(url)
                WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "CodeMirror-scroll")))
                editor = self.driver.find_element_by_css_selector('.CodeMirror  textarea')
                editor.send_keys(Keys.CONTROL + "a")
                editor.send_keys(Keys.DELETE)
                editor.send_keys(query)
                self.driver.find_element_by_xpath('//button[text()="Submit"]').click()
                self.driver.implicitly_wait(20)
                x_mark = self.driver.find_element_by_css_selector("i.fa.fa-times.incorrect")
                assert x_mark.is_displayed()

    def tearDown(self):
        # time.sleep(60)
        self.driver.close()


WrongQueriesChecker()


class UiElementsChecker(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/mbajic/Documents/python/'
                                                                        r'testing/sparql_lab_tests/chromedriver.exe')

    def test_page_running(self):
        driver = self.driver
        driver.get("https://doc.lmcloud.vse.cz/sparqlab")
        assert 'Exercises by difficulty' in driver.find_element_by_tag_name("h1").text

    def test_navigation_bar(self):
        driver = self.driver
        driver.get("https://doc.lmcloud.vse.cz/sparqlab")
        nav_bar = driver.find_element_by_id("collapsing-navbar")
        assert "SPARQLabβ" in nav_bar.text
        assert "Exercises" in nav_bar.text
        assert "SPARQL endpoint" in nav_bar.text
        assert "Data" in nav_bar.text
        assert "About" in nav_bar.text

    def test_search_function(self):
        driver = self.driver
        driver.get("https://doc.lmcloud.vse.cz/sparqlab")
        search = driver.find_element_by_xpath('//*[@id="search-term"]')
        search.click()
        search.send_keys("datatype")
        driver.find_element_by_xpath('//*[@id="collapsing-navbar"]/form/div/div/div/ul/li/mark').click()
        assert "Datové typy" in driver.find_element_by_xpath('/html/body/div/ul').text

    def test_about_option(self):
        driver = self.driver
        driver.get("https://doc.lmcloud.vse.cz/sparqlab")
        driver.find_element_by_xpath('//*[@id="collapsing-navbar"]/ul/li[4]/a').click()
        assert "SPARQLab serves for exercising the SPARQL query language." in driver.find_element_by_xpath(
            "/html/body/div/div/div/p[1]").text

    def test_exercises_menu(self):
        driver = self.driver
        driver.get("https://doc.lmcloud.vse.cz/sparqlab")
        driver.find_element_by_xpath('//*[@id="collapsing-navbar"]/ul/li[1]/a').click()
        assert "By language constructs" in driver.find_element_by_xpath(
            '//*[@id="collapsing-navbar"]/ul/li[1]/div/a[3]').text

    def tearDown(self):
        # time.sleep(60)
        self.driver.close()


UiElementsChecker()


class NumbersTestResult(unittest.TextTestResult):
    def addSubTest(self, test, subtest, outcome):
        super(NumbersTestResult, self).addSubTest(test, subtest, outcome)
        self.testsRun += 1


if __name__ == "__main__":
    unittest.main(testRunner=unittest.TextTestRunner(resultclass=NumbersTestResult))
