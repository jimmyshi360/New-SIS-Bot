from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.support.ui import Select 
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains

import datetime
import os 
import sys

#I FUCKING HATE WRITING NEW BOTS. FUCKKKKKKK

usernameStr = 'REPLACE'
passwordStr = 'REPLACE'

try:
	usernameStr = sys.argv[1]
	passwordStr = sys.argv[2]
except BaseException:
	print("\nError: This script should be run with the following (valid) flags:\n python bot.py SIS_Username SIS_Password\n")
	sys.exit(-1)

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get(('https://sis.jhu.edu/sswf/'))
nextButton = browser.find_element_by_id('linkSignIn')
nextButton.click()
WebDriverWait(browser, 10)

username = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.NAME, 'loginfmt')))
username.send_keys(usernameStr)

WebDriverWait(browser, 10)

submit1button = browser.find_element_by_id("idSIButton9")
submit1button.click()


WebDriverWait(browser, 10)
password = browser.find_element_by_name('passwd')
password.send_keys(passwordStr)

WebDriverWait(browser, 10)

#ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
#submit2button = WebDriverWait(browser, 20,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.ID, "idSIButton9")))
#submit2button.click()
'''
def find(driver):
    element = browser.find_elements_by_class_name("button ext-button primary ext-primary")[0]
    if element:
        return element
    else:
        return False
submit2button = WebDriverWait(browser, 20).until(find)
submit2button.click()
'''

staleElement = True; 

while staleElement:
    try:
        submit = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, 'idSIButton9')))
        submit.click()
        staleElement = False

    except StaleElementReferenceException:

        staleElement = True


WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "aspnetForm")))

browser.get("https://sis.jhu.edu/sswf/SSS/EnrollmentCart/SSS_EnrollmentCart.aspx?MyIndex=88199")


WebDriverWait(browser, 10)
selectAll = browser.find_element_by_id('SelectAllCheckBox')
selectAll.click()

WebDriverWait(browser, 10)
register = browser.find_element_by_id("ctl00_contentPlaceHolder_ibEnroll")

# # Wait until its 7 O'clock
while True:
	current_hour = datetime.datetime.now().time().hour
	if current_hour == 7:
		browser.execute_script("arguments[0].click();", register)
		WebDriverWait(browser, 10000)

		while True:
			if (browser.find_element_by_id('ctl00_contentPlaceHolder_rbWaitlistYes')):
				yes = browser.find_element_by_id('ctl00_contentPlaceHolder_rbWaitlistYes')
				cont = browser.find_element_by_id('ctl00_contentPlaceHolder_cmdContinue')
				yes.click()
				WebDriverWait(browser, 10)
				cont.click()
		break



