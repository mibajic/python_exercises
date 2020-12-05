import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data_correct_queries_checker import test_cases_dict


class CorrectQueriesChecker(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/mbajic/Documents/python/'
                                                                        r'testing/sparql_lab_tests/chromedriver.exe')

    def test_load_test_cases(self):
        global url
        global query
        driver = self.driver
        for test_case, url_and_query in test_cases_dict.items():
            with self.subTest(test_case=test_case, url_and_query=url_and_query):
                url = url_and_query[0]
                query = url_and_query[1]
                driver.get(url)
                WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'CodeMirror-scroll'))) 
                editor = driver.find_element_by_css_selector('.CodeMirror  textarea')
                editor.send_keys(Keys.CONTROL + "a")
                editor.send_keys(Keys.DELETE)
                editor.send_keys(query)
                send_button = driver.find_element_by_xpath('//button[text()="Submit""]')
                send_button.click()
                driver.implicitly_wait(20)
                checkmark = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/h2/i')
                assert checkmark.is_displayed()

    def tearDown(self):
        # time.sleep(60)
        self.driver.close()


CorrectQueriesChecker()


class UiElementsChecker(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/mbajic/Documents/python/testing/sparql_lab_tests'
                                                       r'/chromedriver.exe')

    def test_page_running(self):
        driver = self.driver
        driver.get("https://doc.lmcloud.vse.cz/sparqlab")
        title = driver.find_element_by_tag_name("h1")
        assert 'Exercises by difficulty' in title.text
        # self.assertIn("Exercises by difficulty", title.text)

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
