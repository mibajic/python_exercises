import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys


class WebChecker(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\mbajic\Documents\python\testing\sparql_lab_tests\chromedriver.exe')

    # functions checks if page is running
    def test_page_running(self):
        driver = self.driver
        driver.get("https://doc.lmcloud.vse.cz/sparqlab")
        title = driver.find_element_by_tag_name("h1")
        assert 'Exercises by difficulty' in title.text
        # self.assertIn("Exercises by difficulty", title.text)

    # function checks if there are correct elements in the navigation bar
    def test_navigation_bar(self):
        driver = self.driver
        driver.get("https://doc.lmcloud.vse.cz/sparqlab")
        nav_bar = driver.find_element_by_id("collapsing-navbar")
        assert "SPARQLabβ" in nav_bar.text
        assert "Exercises" in nav_bar.text
        assert "SPARQL endpoint" in nav_bar.text
        assert "Data" in nav_bar.text
        assert "About" in nav_bar.text

    # exercise 'show some data' given correct query
    def test_show_data(self):
        driver = self.driver
        driver.get("https://doc.lmcloud.vse.cz/sparqlab/exercise/show/some-data")
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "CodeMirror-scroll")))
        editor = driver.find_element_by_css_selector('.CodeMirror  textarea')
        editor.send_keys('ASK { \n [] ?p [] . \n }')
        send_button = driver.find_element_by_xpath('//button[text()="Submit"]')
        send_button.click()
        driver.implicitly_wait(20)
        checkmark = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/h2/i')
        assert checkmark.is_displayed()

    def tearDown(self):
        time.sleep(4)
        # self.driver.close()


if __name__ == "__main__":
    unittest.main()
