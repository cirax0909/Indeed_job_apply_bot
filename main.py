from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.common.exceptions import NoSuchElementException

# job_title = input("Please insert key word for job position: ")
# location = input("Please insert location you want to find a job: ")
email = "tichpham1@gmail.com"
password = "6688thien!!tich"

s = Service('C:\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=s)
url = 'https://ca.indeed.com/'
driver.maximize_window()
driver.get(url)

#login
driver.find_element(By.LINK_TEXT, "Sign in").click()
driver.find_element(By.XPATH, '//*[@id="ifl-InputFormField-3"]').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="emailform"]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="auth-page-google-password-fallback"]').click()
driver.find_element(By.XPATH, '//*[@id="ifl-InputFormField-106"]').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="loginform"]/button').click()




