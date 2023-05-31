from selenium import webdriver
from time import sleep


def url_should_have(browser: webdriver.Chrome, current_url: str, timeout: int= 5):
    time_spend = 0
    for i in range(timeout):
        if current_url in browser.current_url:
            return True
        else:
            if time_spend <= timeout:
                time_spend += 0.5
                sleep(0.5)
            else:
                return False
