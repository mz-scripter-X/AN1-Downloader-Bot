#The numbers in the time.sleep() is to wait for the page to load
#You can remove/reduce depending on the speed of your connection
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

LINK = "https://an1.com/"
game = input("Which modded app would you like to download? ")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(LINK)
time.sleep(5)

search_btn = driver.find_element(By.ID, "qsearch_btn")
search_btn.click()
time.sleep(3)

input_query = driver.find_element(By.ID, "searchinput")
input_query.send_keys(game)
input_query.send_keys(Keys.ENTER)
time.sleep(3)
first_game = driver.find_element(By.CLASS_NAME, "item")
first_game.click()
time.sleep(3)

download_btn = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-lg.btn-green")
download_btn.click()
time.sleep(10)

time.sleep(3)
download_btn2 = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-lg.btn-green")
download_btn2.click()
driver.quit() 
