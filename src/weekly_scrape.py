from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from scraper import Scraper

def weekly_scrape(url: str):
    scraper = Scraper()
    scraper.go_to(url)
    scraper.enter_iframe('#oneid-iframe')

    email_input = scraper.find_by_selector('#InputIdentityFlowValue')
    scraper.enter_text(email_input, 'tourvahsir@yahoo.com')

    scraper.click_selector('#BtnSubmit')

    pw_input = scraper.find_by_selector('#InputPassword')
    scraper.enter_text(pw_input, open('secrets/password.txt', 'r').read())

    scraper.click_selector('#BtnSubmit')

    scraper.driver.switch_to.default_content()
    scraper.driver.find_element(By.CLASS_NAME, 'error-message')
    scraper.go_to(url)
    scraper.driver.refresh()

    nameElements = scraper.driver.find_elements(By.CLASS_NAME, 'ScoreCell__TeamName')
    scoreElements = scraper.driver.find_elements(By.CLASS_NAME, 'ScoreCell__Score')

    names = [nameElement.text for nameElement in nameElements]
    scores = [float(scoreElement.text) for scoreElement in scoreElements]

    scoreboard = {}
    for name, score in zip(names, scores):
        scoreboard[name] = score
        print('{Name}: {Score}'.format(Name = name, Score = score))

    scraper.close()

    return scoreboard


weeks = ['https://fantasy.espn.com/football/boxscore?leagueId=1967724109&matchupPeriodId={week}&scoringPeriodId={week}&seasonId=2023'.format(week = x) for x in range(1, 8)]

for week in weeks:
    weekly_scrape(week)