import time

from selenium.webdriver.common.by import By

def test_govna(browser):

    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button_basket = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    time.sleep(10)
    assert button_basket == True, "Element not found"

