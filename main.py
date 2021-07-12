import wget
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os



driver= webdriver.Chrome()
driver.get("http://www.instagram.com/")
accept_all = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[class='aOOlW  bIiDR  ']"))).click()
username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']")))
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))

username.clear()
password.clear()

username.send_keys("yourusername")
password.send_keys("yourpassword")

login = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()
Not_now1 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Not now')]"))).click()
Not_now2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Not Now')]"))).click()
searchbox = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder = 'Search']")))
searchbox.clear()
keyword = "#dogs"
searchbox.send_keys(keyword)
time.sleep(2)
searchbox.send_keys(Keys.ENTER)
searchbox.send_keys(Keys.ENTER)
time.sleep(2)
#scroll down to scrape more images
driver.execute_script("window.scrollTo(0, 4000);")

#target all images on the page
images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]
images = images[:-2]

print('Number of scraped images: ', len(images))
time.sleep(2)
path = os.getcwd()
path = os.path.join(path, keyword[1:] + "s")

#create the directory
os.mkdir(path)

path
time.sleep(2)
#download images
counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1



















# scroll to the bottom of the page
#lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
#match=False
#while(match==False):
#    lastCount = lenOfPage
#    time.sleep(3)
#    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
#    if lastCount==lenOfPage:
#        match=True

