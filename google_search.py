from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pathlib

PATH = pathlib.Path("G:\Code\Selenium_drivers\geckodriver\geckodriver-v0.31.0-win64")

driver = webdriver.Firefox(PATH)
driver.implicitly_wait(0.5)
driver.get("http://www.google.com")

#identify search box
m = driver.find_element_by_name("q")
#enter search text
m.send_keys("today's date")
time.sleep(0.2)
#perform Google search with Keys.ENTER
m.send_keys(Keys.ENTER)
