import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CorrectQueriesChecker(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\mbajic\Documents\python\testing\sparql_lab_tests"
                                                       r"\chromedriver.exe")

    def test_load_test_cases(self):
        global url
        global query
        for test_case, url_and_query in self.test_cases_dict.items():
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

    test_cases_dict = {1: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/some-data",
                           'PREFIX qb: <http://purl.org/linked-data/cube#> \n'
                           'DESCRIBE ?dimension \n WHERE { \n   ?dimension a qb:DimensionProperty . \n } '],
                       2: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/one-triple",
                           'SELECT * \n WHERE { \n ?s ?p ?o . \n } LIMIT 1 '],
                       3: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/some-named-graphs",
                           'ASK \n WHERE { \n GRAPH ?g { \n [] ?p [] . \n } \n }'],
                       4: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes",
                           'SELECT DISTINCT ?class \n WHERE { \n [] a ?class . \n }'],
                       5: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-triples",
                           'SELECT (COUNT(*) as ?count) \n WHERE { \n ?s ?p ?o . \n }'],
                       6: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties",
                           'SELECT DISTINCT ?p \n WHERE { \n [] ?p [] . \n } '],
                       7: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/describe-orphan-pension",
                           'DESCRIBE <https://data.cssz.cz/resource/pension-kind/PK_D>'],
                       8: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/one-quad",
                           'SELECT * \n WHERE { \n GRAPH ?g { \n ?s ?p ?o . \n } \n } \n LIMIT 1'],
                       9: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/named-graphs",
                           'SELECT DISTINCT ?g \n WHERE { \n GRAPH ?g { \n ?s ?p ?o . \n } \n }'],
                       10: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes-histogram",
                            'SELECT ?class (COUNT(?s) AS ?count) \n WHERE { \n ?s a ?class . \n } '
                            '\n GROUP BY ?class \n ORDER BY DESC(?count)'],
                       11: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties-histogram",
                            'SELECT ?p (COUNT(*) as ?count) \n WHERE { \n [] ?p [] . \n } \n '
                            'GROUP BY ?p \n ORDER BY DESC( ?count)'],
                       12: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dataset-equals-named-graph",
                            'PREFIX qb: <http://purl.org/linked-data/cube#> \n ASK \n WHERE { \n GRAPH ?d { \n '
                            '?d a qb:DataSet . \n } \n }'],
                       13: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/understanding-from",
                            'SELECT (COUNT(*) AS ?count) \n FROM '
                            '<https://data.cssz.cz/resource/dataset/rocenka/vocabulary> \n'
                            ' WHERE { \n ?s ?p ?o . \n }'],
                       14: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/describe-dimensions",
                            'PREFIX qb: <http://purl.org/linked-data/cube#> \n DESCRIBE ?dimension \n WHERE { \n '
                            '?dimension a qb:DimensionProperty . \n }'],
                       15: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/graph-sizes",
                            'SELECT ?g (COUNT(*) as ?count) \n WHERE { \n GRAPH ?g { \n [] ?p [] . \n } \n } \n'
                            ' GROUP BY ?g \n ORDER BY DESC(?count)'],
                       16: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/understanding-graph",
                            'SELECT (COUNT(*) AS ?COUNT) \n WHERE { \n GRAPH '
                            '<https://data.cssz.cz/resource/dataset/rocenka/vocabulary> { \n [] ?p [] . \n } \n }'],
                       17: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/understanding-from-named",
                            'SELECT (COUNT(*) AS ?count) \n FROM NAMED '
                            '<https://data.cssz.cz/resource/dataset/rocenka/vocabulary> \n WHERE { \n GRAPH ?g { \n ['
                            '] ?p [] . \n } \n } '],
                       18: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-distinct-classes",
                            'SELECT (COUNT(DISTINCT ?class) AS ?count) \n WHERE { \n   GRAPH '
                            '<https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n  '
                            '[] a ?class . \n } \n }'],
                       19: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes-histogram-code-lists",
                            'SELECT ?class (COUNT(?s) AS ?count) \n WHERE { \n GRAPH '
                            '<https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n ?s a ?class . \n } \n } '
                            '\n GROUP BY ?class \n ORDER BY DESC(?count)'],
                       20: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/disjoint-concept-and-concept-scheme",
                            'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n ASK \n WHERE { \n   GRAPH '
                            '<https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n     '
                            '?s a skos:Concept, skos:ConceptScheme . \n } \n }'],
                       21: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties-histogram-code-lists",
                            'SELECT ?property (COUNT(*) AS ?count) \n WHERE { \n   GRAPH '
                            '<https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n     '
                            '[] ?property [] . \n } \n } \n GROUP BY ?property \n ORDER BY DESC(?count)'],
                       22: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes-histogram-data",
                            'SELECT ?class (COUNT(?s) AS ?count) \n WHEE { \n   GRAPH '
                            '<https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { '
                            '\n ?s a ?class . \n } \n } \n GROUP BY ?class \n ORDER BY DESC(?count)'],
                       23: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/most-common-class-data",
                            'SELECT ?class (COUNT(?s) AS ?count) \n WHERE { \n   GRAPH '
                            '<https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n ?s a ?class . '
                            '\n } \n } \n GROUP BY ?class \n ORDER BY DESC(?count) \n LIMIT 1']
                       }

    def tearDown(self):
        # time.sleep(60)
        self.driver.close()


CorrectQueriesChecker()

if __name__ == "__main__":
    unittest.main()
