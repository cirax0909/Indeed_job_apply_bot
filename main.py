from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.common.exceptions import NoSuchElementException

s = Service('C:\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=s)
url = 'https://www.linkedin.com/jobs/search/?keywords=backend%20developer'
driver.minimize_window()
driver.get(url)