# #!/usr/bin/env python
from re import sub
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By


# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    # options = ChromeOptions()
    # options.add_argument("--headless") 
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')

    text_box_user = driver.find_element(by=By.CSS_SELECTOR, value=".form_group input[id='user-name']")
    text_box_user.send_keys(user)
    
    text_box_password = driver.find_element(by=By.CSS_SELECTOR, value=".form_group input[id='password']")
    text_box_password.send_keys(password)

    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="input#login-button.submit-button.btn_action")

    submit_button.click()

    print("Login Success")

    sleep(3)

def add_items():
    pass

def remove_items():
    pass

login('standard_user', 'secret_sauce')

