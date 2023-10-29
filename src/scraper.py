from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class Scraper:
    def __init__(self):
        driver = webdriver.Chrome()
        FIVE_SECONDS = 5
        driver.implicitly_wait(FIVE_SECONDS)
        self.driver = driver
    
    def go_to(self, url: str):
        self.driver.get(url)

    def find_by_selector(self, identifer: str):
        return self.driver.find_element(By.CSS_SELECTOR, identifer)

    def enter_iframe(self, identifer: str):
        iframe = self.find_by_selector(identifer)
        self.driver.switch_to.frame(iframe)
    
    def enter_text(self, input: WebElement, text: str):
        value = ''
        while value != text:
            input.clear()
            input.send_keys(text)
            value = input.get_attribute('value')
    
    def selector_exists(self, selector: str):
        return len(self.driver.find_elements(By.CSS_SELECTOR, selector)) > 0

    def click_selector(self, selector: str):
        self.driver.find_element(By.CSS_SELECTOR, selector).click()
    
    def close(self):
        self.driver.close()