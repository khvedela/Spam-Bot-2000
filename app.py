print(
    """
    
░██████╗██████╗░░█████╗░███╗░░░███╗░░░██╗░██╗░██████╗░░█████╗░████████╗░░░██╗░██╗░██████╗░░█████╗░░█████╗░░█████╗░
██╔════╝██╔══██╗██╔══██╗████╗░████║██████████╗██╔══██╗██╔══██╗╚══██╔══╝██████████╗╚════██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░██████╔╝███████║██╔████╔██║╚═██╔═██╔═╝██████╦╝██║░░██║░░░██║░░░╚═██╔═██╔═╝░░███╔═╝██║░░██║██║░░██║██║░░██║
░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██████████╗██╔══██╗██║░░██║░░░██║░░░██████████╗██╔══╝░░██║░░██║██║░░██║██║░░██║
██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║╚██╔═██╔══╝██████╦╝╚█████╔╝░░░██║░░░╚██╔═██╔══╝███████╗╚█████╔╝╚█████╔╝╚█████╔╝
╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚═╝░╚═╝░░░╚═════╝░░╚════╝░░░░╚═╝░░░░╚═╝░╚═╝░░░╚══════╝░╚════╝░░╚════╝░░╚════╝░
    """
)

print(
    """    
█▄▄ █▄█   █▄▀ █░█ █░█ █▀▀ █▀▄ █▀▀ █░░ ▄▀█
█▄█ ░█░   █░█ █▀█ ▀▄▀ ██▄ █▄▀ ██▄ █▄▄ █▀█
    """
)



from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from credentials import username, password, profile_link, count, word
from itertools import repeat


#CHROMEDRIVER PATH
driver = webdriver.Chrome(executable_path=r'C:\Users\David\Documents\chromedriver.exe')

#Target website
driver.get('https://instagram.com/accounts/login/')

time.sleep(5)

#Yousername input
driver.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input').send_keys(username)
#Password input
driver.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input').send_keys(password)

#Log in button
driver.find_element_by_css_selector('button[type=submit]').click()

time.sleep(5)

#Target persons page
driver.get(profile_link)

time.sleep(5)

#Press message button
driver.find_element_by_css_selector('button[type=button]').click()

time.sleep(5)

#press not now to remove notification pop-up
driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()




#SPAMMING
for unused in repeat(None, count):
    del unused
    print(word)
    driver.find_element_by_xpath(
        '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(word)
    driver.find_element_by_xpath(
        '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(Keys.ENTER)
