import argparse
import json
import pygal
import os

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-i','--input-path', help='The path to your json data. (data/*/week_*.json)', required=True)
parser.add_argument('-o','--output-path', help='The output path of the generated graph. (viz/*.svg)', required=False)
args = vars(parser.parse_args())

input_path = args['input_path']
output_path = args['output_path'] if 'output_path' in args else ''

def generate_graph(input_path, output_path: str):
    f = open(input_path, "r")
    json_string = f.read()
    f.close()

    score_data = json.loads(json_string)
    names = list(score_data.keys())
    bar_chart = pygal.Bar(title=input_path, height=350)

    for name in names:
        bar_chart.add(name, score_data[name])
    if output_path == '':
        bar_chart.render_in_browser()
    else:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        bar_chart.render_to_file(output_path)

if os.path.isdir(input_path):
    for filename in os.listdir(input_path):
        generate_graph(os.path.join(input_path, filename), os.path.splitext(os.path.join(output_path, filename))[0] + '.svg')
else:
    generate_graph(input_path, output_path)
