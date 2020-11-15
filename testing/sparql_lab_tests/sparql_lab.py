import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WebChecker(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\mbajic\Documents\python\testing\sparql_lab_tests\chromedriver.exe')

    # functions checks if page is running
    def test1_page_running(self):
        driver = self.driver
        driver.get("https://doc.lmcloud.vse.cz/sparqlab")
        title = driver.find_element_by_tag_name("h1")
        assert 'Exercises by difficulty' in title.text

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
