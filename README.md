# sport-scrape
### Parse, analyze, and visualize ESPN Fantasy Football data. 

## Prerequisites
- Python
- todo...

## Usage
1) Clone this repo.
2) Fill out `secrets/email.txt` and `secrets/password.txt` with your ESPN login information.
3) Scrape your data for a range of weeks with `./scripts/week.sh -l $league_id -s $week_number -e $week_number -n $name`

This should output json files of your data to `data/name/`.

4) Create a graph visualization by running `./scripts/generate_week.sh -i data/name/week_1.json`.
