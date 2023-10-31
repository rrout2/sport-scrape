# sport-scrape
### Parse, analyze, and visualize ESPN Fantasy Football data. 
https://rrout2.github.io/sport-scrape/
## Prerequisites
- Python
- todo...

## Usage
1) Clone this repo.
2) Fill out `secrets/email.txt` and `secrets/password.txt` with your ESPN login information.
3) Scrape your data for a range of weeks with `./scripts/range.sh -l $league_id -s $week_number -e $week_number -n $name`

This should output json files of your data to `data/name/`.

4) Create a graph visualization by running `./scripts/generate_weekly_graphs.sh -i data/name -o viz/name`.
