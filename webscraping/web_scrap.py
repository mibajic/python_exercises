from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path = 'C:/Users/Tomas/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe')
wait = WebDriverWait(driver, 10)
driver.get('http://apps.tga.gov.au/Prod/devices/daen-entry.aspx')

driver.find_element_by_id('disclaimer-accept').click()

wait.until(EC.visibility_of_element_located((By.ID, "medicine-name")))
driver.find_element_by_id('medicine-name').send_keys('124099')

wait.until(EC.visibility_of_element_located((By.ID, "medicines-header-text")))
driver.find_element_by_id('medicines-header-text').click()
driver.find_element_by_id('submit-button').click()

wait.until(EC.visibility_of_element_located((By.ID, "ctl00_body_MedicineSummaryControl_cmbPageSelection")))
driver.find_element_by_id("ctl00_body_MedicineSummaryControl_cmbPageSelection").click()
driver.find_element_by_xpath('//option[@value="all"]').click()

wait.until(EC.visibility_of_element_located((By.ID, "ctl00_body_MedicineSummaryControl_grdSummary")))
tab_data = driver.find_element_by_id("ctl00_body_MedicineSummaryControl_grdSummary")

list_rows = []
for items in tab_data.find_elements_by_xpath('.//tr'):
	list_cells = []
	for item in items.find_elements_by_xpath('.//td[@class="row-odd"]|.//td'):
		list_cells.append(item.text)
	list_rows.append(list_cells)
fdata = open('webdata.xml', 'w')
for data in list_rows:
	fdata.write(data)
fdata.close()
