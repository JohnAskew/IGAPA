import os, sys

try:

	from bokeh.plotting import figure, output_file, show

except:

	os.system('pip install bokeh')

	from bokeh.plotting import figure, output_file, show

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

df = pd.read_csv('exa_db_size_monthly.csv',  parse_dates=['INTERVAL_START'])

df['INTERVAL_START'] = pd.to_datetime(df['INTERVAL_START']) 

print(df.head(10))

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="RAW_OBJECT_SIZE_MAX over time", x_axis_type = "datetime", x_axis_label='INTERVAL_START', y_axis_label='RAW_OBJECT_SIZE_MAX')

# add a line renderer with legend and line thickness
df.reset_index(inplace  = True)

p.vbar(df['INTERVAL_START'], top = df['RAW_OBJECT_SIZE_MAX'], width = 1000, line_width=2)

# show the results
show(p)