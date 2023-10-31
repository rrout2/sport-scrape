import argparse
import json
import pygal
import os

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-i','--input-path', help='The path to your foler of json data (data/*/', required=True)
parser.add_argument('-o','--output-path', help='The output path of the generated graph. (viz/*.svg)', required=False)
args = vars(parser.parse_args())
input_path = args['input_path']
output_path = '' if args['output_path'] is None else args['output_path']

if not os.path.isdir(input_path):
    exit(1)

line_chart = pygal.Line(height=350)
line_chart.title = 'Weekly Scores for {input}'.format(input = input_path)

# maps from team name to list of scores
chart_data = {}
filenames = sorted(os.listdir(str(input_path)))
num_weeks = len(filenames)
for filename in filenames:
    individual_file = os.path.join(input_path, filename)
    f = open(individual_file, "r")
    json_string = f.read()
    f.close()

    score_data = json.loads(json_string)
    names = list(score_data.keys())
    for name in names:
        if name not in chart_data:
            chart_data[name] = [score_data[name]]
        else:
            chart_data[name].append(score_data[name])

line_chart.x_labels = ['Week {week_num}'.format(week_num = x + 1) for x in range(num_weeks)]
for name in chart_data:
    line_chart.add(name, chart_data[name])

if output_path == '':
    line_chart.render_in_browser()
else:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    line_chart.render_to_file(output_path)

