from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from fantasy_football_data import FantasyFootballData
from team import Team

from scraper import Scraper
import argparse
import json
import os

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-y','--year',       help='Which season',                       required=False)
parser.add_argument('-n','--name',       help='name of the league',                 required=False)
parser.add_argument('-l','--league-id',  help='The ESPN ID of your league',         required=True)
parser.add_argument('-s','--start-week', help='The first week you want to scrape.', required=True)
parser.add_argument('-e','--end-week',   help='The last week you want to scrape.',  required=True)

def scrape_scoreboard(url: str, scraper: Scraper):
    scraper.go_to(url)

    nameElements = scraper.driver.find_elements(By.CLASS_NAME, 'ScoreCell__TeamName')
    scoreElements = scraper.driver.find_elements(By.CLASS_NAME, 'ScoreCell__Score')

    names = [nameElement.text for nameElement in nameElements]
    scores = [float(scoreElement.text) for scoreElement in scoreElements]

    scoreboard = {}
    for name, score in zip(names, scores):
        scoreboard[name] = score

    return scoreboard

# WIP
def scrape_standings(league_id: str, scraper: Scraper):
    scraper.go_to('https://fantasy.espn.com/football/league/standings?leagueId={league_id}&seasonId=2023'.format(league_id = league_id))
    ranks = scraper.driver.find_elements(By.CSS_SELECTOR, '.table--cell.rank:not(.header)')
    ranks = ranks[len(ranks) // 2:]
    ranks = [int(rank.text) for rank in ranks]
    names = scraper.driver.find_elements(By.CSS_SELECTOR, '.v-mid.team--link')
    names = names[len(names) // 2:]
    names = [name.text for name in names]

    points_for = scraper.driver.find_elements(By.CSS_SELECTOR, '.table--cell.points-for:not(.header)')
    points_for = [float(pf.text) for pf in points_for]

    data = [Team(name, rank, pf) for name, rank, pf in zip(names, ranks, points_for)]

    return data


def assemble_url(season_id, league_id, week_num: str):
    fmtStr = 'https://fantasy.espn.com/football/boxscore?leagueId={league_id}&matchupPeriodId={week_num}&scoringPeriodId={week_num}&seasonId={season_id}'
    return fmtStr.format(season_id = season_id, week_num = week_num, league_id = league_id)

args = vars(parser.parse_args())
league_id = args['league_id']
start_week= int(args['start_week'])
end_week = int(args['end_week'])
year = '2023' if 'year' not in args else args['year']
league_name = league_id if 'name' not in args else args['name']

urls = [assemble_url(year, league_id, week_num) for week_num in range(start_week, end_week + 1)]
scraper = Scraper()

data = FantasyFootballData(scrape_standings(league_id, scraper))
print(data.__dict__)
filename = 'test.json'
# os.makedirs(os.path.dirname(filename), exist_ok=True)
f = open(filename, 'w')
f.write(json.dumps(data.__dict__))
f.close()
for i, url in enumerate(urls):
    scoreboard = scrape_scoreboard(url, scraper)
    filename = 'data/{league_name}/week_{week_num}.json'.format(league_name = league_name, week_num = start_week + i)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    f = open(filename, 'w')
    f.write(json.dumps(scoreboard))
    f.close()

scraper.close()
