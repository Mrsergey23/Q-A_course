from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromService
from webdriver_manager.chrome import ChromeDriverManager


URL = 'https://www.saucedemo.com/'

LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

def get_driver():
  driver = webdriver.Chrome(service=ChromService(ChromeDriverManager().install()))
  return driver

def open_page(driver, url):
  driver.get(url)
    
def get_element_by_id(driver, locator):
  return driver.find_element(value = locator)


def element_click(driver, locator):
  get_element_by_id(driver, locator).click()


def element_send_keys(driver, locator, key):
  get_element_by_id(driver, locator).send_keys(key)

def login(driver, login, password):
  element_send_keys(driver,'user-name', login)
  element_send_keys(driver,'password', password)
  element_click(driver, 'login-button') 

driver = get_driver()
open_page(driver, URL)
login(driver, login = LOGIN, password = PASSWORD )
driver.quit()


