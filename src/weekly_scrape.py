from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from scraper import Scraper
import argparse

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-y','--year', help='Which season', required=False)
parser.add_argument('-l','--league-id', help='The ESPN ID of your league', required=True)
parser.add_argument('-s','--start-week', help='The first week you want to scrape.', required=True)
parser.add_argument('-e','--end-week', help='The last week you want to scrape.', required=True)
args = vars(parser.parse_args())
league_id = args['league_id']
start_week= int(args['start_week'])
end_week = int(args['end_week'])
year = '2023' if 'year' not in args else args['year']

def weekly_scrape(url: str):
    scraper = Scraper()
    scraper.go_to(url)
    scraper.enter_iframe('#oneid-iframe')

    email_input = scraper.find_by_selector('#InputIdentityFlowValue')
    scraper.enter_text(email_input, open('secrets/email.txt', 'r').read())

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

def assemble_url(season_id: str, week: str):
    fmtStr = 'https://fantasy.espn.com/football/boxscore?leagueId={leagueId}&matchupPeriodId={week}&scoringPeriodId={week}&seasonId={season_id}'
    return fmtStr.format(season_id, week , league_id)

weeks = [assemble_url(year, week) for week in range(start_week, end_week + 1)]

for week in weeks:
    weekly_scrape(week)