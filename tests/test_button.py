from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
#from time import sleep

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    chrome_browser = webdriver.Chrome(options=options)
    return chrome_browser

def test_button_1(browser):
    browser.get("https://www.qa-practice.com/elements/button/simple")
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()
    #sleep(10)

def test_requirements(browser):
    browser.get("https://www.qa-practice.com/elements/button/simple")
    assert browser.find_element(By.ID, 'req_header').is_displayed()
