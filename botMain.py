from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os


path = os.getcwd()

jscommand = """
followers = document.querySelector(".isgrP");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;
"""
username = input("Kullanıcı adınızı girin:")
password = input("Şifrenizi girin:")

delay = 5

driver = webdriver.Chrome(executable_path=path+"/chromedriver.exe")
driver.get("https://www.instagram.com/")


while True:
    try:     
        username_box = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.NAME,"username")))
        username_box.send_keys(username)
        password_box = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.NAME,"password")))
        password_box.send_keys(password)
        loginbutton = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(4) > button > div")))
        loginbutton.click()
        not_now = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.CSS_SELECTOR,"body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm")))
        not_now.click()
        break
    except:
        print("Bir hata oluştu lütfen tekrar deneyiniz.\n")
        username_box.send_keys(Keys.CONTROL + "a")
        username_box.send_keys(Keys.DELETE)
        password_box.send_keys(Keys.CONTROL + "a")
        password_box.send_keys(Keys.DELETE)
        username = input("Kullanıcı adınızı girin:")
        password = input("Şifrenizi girin:")

x=0
while (x<=10):
    try:
        profile_button = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(5) > span")))
        profile_button.click()

        followers_button = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#react-root > section > main > div > header > section > ul > li:nth-child(2) > a")))
        followers_button.click()
        break
    except:
        driver.get("https://www.instagram.com/")
        x+=1

time.sleep(1)

while True:
    try:
        lenOfPage = driver.execute_script(jscommand)
        match=False
        while(match==False):
            lastCount = lenOfPage
            time.sleep(0.75)
            lenOfPage = driver.execute_script(jscommand)
            if lastCount == lenOfPage:
                match=True
        time.sleep(1)
        followers_list = []
        followers = driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa ")

        for follower in followers:
            followers_list.append(follower.text)

        driver.back()
        break
    except:
        pass

while True:
    try:
        following_button = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#react-root > section > main > div > header > section > ul > li:nth-child(3) > a")))
        following_button.click()
        break
    except:
        driver.back()

while True:
    try:
        lenOfPage = driver.execute_script(jscommand)
        match=False
        while(match==False):
            lastCount = lenOfPage
            time.sleep(0.75)
            lenOfPage = driver.execute_script(jscommand)
            if lastCount == lenOfPage:
                match=True
        time.sleep(1)
        followings_list = []
        followings = driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa ")

        for following in followings:
            followings_list.append(following.text)

        driver.back()
        break
    except:
        pass


driver.close()

non_members = []
for i in followings_list:
    if i not in followers_list:
        non_members.append(i)

print(".......Geri takip etmeyenler.......\n")

for k in non_members:
    print(k + "\n")
