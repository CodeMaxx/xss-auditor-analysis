import json
from pychart import *

JS_STATS_FILE = 'js_stats.json'
X_XSS_STATS_FILE = 'x_xss_stats.json'
RANK_FILE = 'rank.json'

X_XSS_STATS_IMAGE_FILE = 'x_xss_stats.png'

with open(X_XSS_STATS_FILE, 'r') as infile:
  x_xss_stats = json.load(infile)

with open(RANK_FILE, 'r') as infile:
  ranks = json.load(infile)

def generate_x_xss_chart():
  count_default = 0
  count_zero = 0
  count_one = 0
  count_block = 0

  for website, header in x_xss_stats.items():
    if header == "default":
      count_default += 1
    elif header == "0":
      count_zero += 1
    elif header == "1":
      count_one += 1
    elif ("1; mode=block" in header) or ("1;mode=block" in header):
      count_block += 1
    else:
      print(header)

  print(count_default)
  print(count_zero)
  print(count_one)
  print(count_block)

  theme.get_options()
  theme.scale_factor = 3
  theme.output_format = "png"
  theme.output_file = X_XSS_STATS_IMAGE_FILE

  data = []
  data.append(["default", count_default])
  data.append(["0", count_zero])
  data.append(["1; mode=block", count_block])
  data.append(["1", count_one])

  ar = area.T(size=(300,300), legend=legend.T(),
              x_grid_style=None, y_grid_style=None)
  plot = pie_plot.T(data=data, arc_offsets=[0,0,0,0],
                    fill_styles=[fill_style.black,
                                 fill_style.gray70,
                                 fill_style.diag,
                                 fill_style.lines],
                    label_offset=10)
  ar.add_plot(plot)
  ar.draw()

generate_x_xss_chart()
