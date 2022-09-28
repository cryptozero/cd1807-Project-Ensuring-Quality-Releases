# #!/usr/bin/env python
from re import sub
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By


# Start the browser and login with standard_user
def login(user: str, password: str) -> webdriver:
    print('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    # options = ChromeOptions()
    # options.add_argument("--headless")
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    print('Browser started successfully. Navigating to the demo page to login.')

    driver.implicitly_wait(0.5)

    driver.get('https://www.saucedemo.com/')

    print(f"Login with user: {user}")

    text_box_user = driver.find_element(
        by=By.CSS_SELECTOR, value=".form_group input[id='user-name']")
    text_box_user.send_keys(user)

    text_box_password = driver.find_element(
        by=By.CSS_SELECTOR, value=".form_group input[id='password']")
    text_box_password.send_keys(password)

    submit_button = driver.find_element(
        by=By.CSS_SELECTOR, value="input#login-button.submit-button.btn_action")

    submit_button.click()

    print("Login Success")

    return driver


def add_items(driver: webdriver) -> int:
    items = driver.find_elements(
        by=By.CSS_SELECTOR, value=".btn_inventory[id|=add-to-cart]")
    for i in items:
        print(f"Adding to cart item: {i.get_property('id')}")
        i.click()

    cart_items = driver.find_element(
        by=By.CSS_SELECTOR, value=".shopping_cart_link > span").text

    assert len(items) == int(cart_items)

    print(f"the cart has {cart_items} items after adding {len(items)}")

    return len(items)

def remove_items(driver: webdriver) -> None:
    items = driver.find_elements(
        by=By.CSS_SELECTOR, value=".cart_button[id|=remove]")
    for i in items:
        print(f"Removing from cart item: {i.get_property('id')}")
        i.click()
        sleep(1)

    cart_items = driver.find_element(
        by=By.CSS_SELECTOR, value=".shopping_cart_link").text

    print(f"Removed cart items, items left: {cart_items}")

    assert cart_items == ""


def go_cart(driver: webdriver) -> None:
    cart = driver.find_element(
        by=By.CSS_SELECTOR, value="#shopping_cart_container > a")
    cart.click()
    print(f"Clicked shopping cart")


driver = login('standard_user', 'secret_sauce')
nitems = 6
added_items = add_items(driver)
assert nitems == added_items
go_cart(driver)
remove_items(driver)

driver-quit()
