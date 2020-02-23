import os, sys

try:

	from bokeh.plotting import figure, output_file, show

	from bokeh.layouts import column

	from bokeh.models import ColumnDataSource

except:

	os.system('pip install bokeh')

	from bokeh.plotting import figure, output_file, show

	from bokeh.layouts  import column

	from bokeh.models import ColumnDataSource

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

y = list(df['INTERVAL_START'])
print("y type:", type(y), "\ny:\n", y)

print("x1=list(df['RAW_OBJECT_SIZE_MAX'])", list(df['RAW_OBJECT_SIZE_MAX']))
source = ColumnDataSource(data=dict(
    y=pd.to_datetime(df['INTERVAL_START']),
    x1=list(df['RAW_OBJECT_SIZE_MAX']),
    x2=list(df['RAW_OBJECT_SIZE_AVG']),
))
p = figure(plot_width=400, plot_height=400, y_axis_type = "datetime", y_axis_label = "INTERVAL_START")

p.hbar_stack(['x1', 'x2'], y='y', height=0.8, color=("blue", "red"), source=source, legend=['RAW_OBJECT_SIZE_AVG', 'RAW_OBJECT_SIZE_MAX'],)

p.legend.title = 'EXA_DB_SIZE_MONTHLY'
p.legend.location = 'bottom_right'

show(p)
