'''
Made by Arpit.

Python bot to attend google meets.


What it does?
1. Joins Meet.
2. Mutes Mic and Disables camera.
3.Sends a message that "Pls mark me Present."
3. Include voice recognition to check if name called and then response.
4.You tell what more to add ¯\_ʘ‿ʘ_/¯


Packages required:

'''
#from webserver import keep_alive
#keep_alive()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://youtube.com")