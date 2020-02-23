import os, sys

try:

	from bokeh.plotting import figure, output_file, show

	from bokeh.layouts import column

except:

	os.system('pip install bokeh')

	from bokeh.plotting import figure, output_file, show

	from bokeh.layouts  import column

try:

	import pandas as pd

except:

	os.system('pip install pandas')

	import pandas as pd

try:
	import csv

except:

	os.system('pip install csv')

	import csv

df_raw = pd.read_csv('exa_db_size_monthly.csv',  parse_dates=['INTERVAL_START'])

df_raw['INTERVAL_START'] = pd.to_datetime(df_raw['INTERVAL_START']) 

print(df_raw.head(10))

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="RAW_OBJECT_SIZE_AVG over time", x_axis_type = "datetime", x_axis_label='INTERVAL_START', y_axis_label='RAW_OBJECT_SIZE_AVG', plot_height = 200)

p.vbar(df_raw['INTERVAL_START'], top = df_raw['RAW_OBJECT_SIZE_AVG'], width = 750, line_width=2)

# add a line renderer with legend and line thickness
df_raw.reset_index(inplace  = True)

q = figure(title="RAW_OBJECT_SIZE_MAX over time", x_axis_type = "datetime", x_axis_label='INTERVAL_START', y_axis_label='RAW_OBJECT_SIZE_MAX', plot_height = 300,x_range=p.x_range)

q.line(df_raw['INTERVAL_START'], df_raw['RAW_OBJECT_SIZE_MAX'], legend="Temp.", line_width=2)

# show the results
show(column([q, p]))
