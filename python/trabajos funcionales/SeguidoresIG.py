from selenium import webdriver
import time

web = webdriver.Chrome()
web.get("https://www.instagram.com/")
time.sleep(5)

def login():
    user = "sthefano_153"
    passed = "45140930yt"
    
    inputUser = web.find_element("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
    inputUser.send_keys(user)
    inputPass = web.find_element("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
    inputPass.send_keys(passed)
    loginButton = web.find_element("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]").click()
