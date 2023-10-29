import argparse
import json
import pygal

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-i','--input-path', help='The path to your json data (data/*/week_*.json)', required=True)
args = vars(parser.parse_args())

input_path = args['input_path']

f = open(input_path, "r")
json_string = f.read()
f.close()

score_data = json.loads(json_string)
names = list(score_data.keys())
bar_chart = pygal.Bar(title=input_path, height=350)

for name in names:
    bar_chart.add(name, score_data[name])
bar_chart.render_in_browser()