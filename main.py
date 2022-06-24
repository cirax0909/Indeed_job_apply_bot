from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

job_title = input("Please insert key word for job position: ")
location = input("Please insert location you want to find a job: ")
email = "tichpham1@gmail.com"
password = "6688thien!!tich"

s = Service('C:\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=s)
url = 'https://ca.indeed.com/'
driver.maximize_window()
driver.get(url)

# login
driver.find_element(By.LINK_TEXT, "Sign in").click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="ifl-InputFormField-3"]').send_keys(email)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="emailform"]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="auth-page-google-password-fallback"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="ifl-InputFormField-106"]').send_keys(password)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="loginform"]/button').click()

# searching
driver.find_element(By.XPATH, '//*[@id="text-input-what"]').send_keys(job_title)
driver.find_element(By.XPATH, '//*[@id="text-input-where"]').send_keys(Keys.CONTROL + "a")
driver.find_element(By.XPATH, '//*[@id="text-input-where"]').send_keys(location)
driver.find_element(By.XPATH, '//*[@id="jobsearch"]/button').click()


# Saving jobs
def job_save(enough):
    while enough <= 2:
        job_listings = driver.find_elements(By.CSS_SELECTOR, '.resultWithShelf')
        for job in job_listings:
            driver.execute_script("arguments[0].scrollIntoView(true);", job)
            time.sleep(2)
            try:
                wait = WebDriverWait(driver, 20)
                wait.until(EC.element_to_be_clickable(job)).click()
            except StaleElementReferenceException:
                print(f'Cannot click number {job_listings.index(job)} job')

            try:
                wait = WebDriverWait(driver, 10)
                wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='vjs-container-iframe']")))
                wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='icl-Button icl-Button--secondary icl"
                                                                 "-Button--lg icl-Button--block css-u42zq4 e8ju0x51'])[1]"
                                                                 ""))).click()
                driver.switch_to.default_content()
            except ElementNotInteractableException:
                print(f'Cannot save number {job_listings.index(job)} job')
        try:
            driver.find_element(By.XPATH, f"//span[normalize-space()='{enough + 1}']").click()
        except NoSuchElementException:
            print("Cannot click the page number")
        enough += 1

        try:
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, '//*[@id="popover-x"]/button').click()
        except ElementNotInteractableException:
            print("No popup")
        finally:
            pass

job_save(1)
