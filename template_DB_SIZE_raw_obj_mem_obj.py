#! python3
#------------------------------------#
# This section will install python 
# modules needed to run this script
#------------------------------------#
import os, sys

try:

    import bokeh

    from bokeh.plotting import figure, output_file, show

    from bokeh.layouts import column, gridplot

    from bokeh.models import ColumnDataSource, Legend, LabelSet, Label, LegendItem

except:

	os.system('pip install bokeh') 

	from bokeh.plotting import figure, output_file, show

	from bokeh.layouts  import column, gridplot

	from bokeh.models import ColumnDataSource, Legend, LabelSet, Label, LegendItem


try:

    import pyexasol

except:

    os.system('pip install pyexasol')

    import pyexasol

try:

    import csv

except:

    os.system("pip install csv")

    import csv

try:

    import pandas as pd

except:

    os.system('pip install pandas')

    import pandas as pd

try:

    import shutil

except:

    os.system('pip install shutil')

    import shutil

try:

    import numpy as np

except:

    os.system("pip install numpy")


try:

    import datetime as dt

    from datetime import date

    from datetime import time, timedelta

except:

    os.system('pip install datetime')

    import datetime as dt

    from datetime import date

    from datetime import time, timedelta

#######################################
# VARIABLES
#######################################

dailySYSTABLE = ""

N_days = 30                            #DAILY SYS Table over past Month

N_hours = 168                          #HOURLY SYS Table over past week

plotWidth=400

plotHeight=300

INTERVAL_START = []

LIST_RAW_SIZE_MAX = []

LIST_RAW_SIZE_AVG = []

LIST_MEM_SIZE_MAX = []

LIST_MEM_SIZE_AVG = []

IP='demodb.exasol.com'

PORT='8563'

SYS='exasol_joas'

SYS_PW='J0hnsPassw0rdShouldB3Ch4ng3d'

SCHEMA='EXA_STATISTICS' #must be all caps

DB_SIZE_DAILY_TBL   = 'EXA_DB_SIZE_DAILY'

#DB_SIZE_MONTHLY_TBL = 'EXA_DB_SIZE_MONTHLY'

DB_SIZE_HOURLY_TBL  = 'EXA_DB_SIZE_HOURLY'

COLUMN_DATE  = 'INTERVAL_START'
COLUMN_1  = 'RAW_OBJECT_SIZE_AVG' #RECOMMENDED_db_raw_SIZE_AVG' #STORAGE_SIZE_AVG
COLUMN_2  = 'RAW_OBJECT_SIZE_MAX' #RECOMMENDED_db_raw_SIZE_MAX' #STORAGE_SIZE_MAX
COLUMN_3  = 'MEM_OBJECT_SIZE_AVG'
COLUMN_4  = 'MEM_OBJECT_SIZE_MAX'

COLS = [COLUMN_DATE, COLUMN_1, COLUMN_2, COLUMN_3, COLUMN_4]
COLS_TBL1 = [COLUMN_DATE, COLUMN_1, COLUMN_2]
COLS_TBL2 = [COLUMN_DATE, COLUMN_3, COLUMN_4]

#######################################
# Set up directory to use
#######################################

currPath = os.getcwd()              # Directory you are in NOW

now = dt.datetime.now()

savePath =  ("exa_" + now.strftime("%Y%m%d_%H%M%S"))               # We will be creating this new sub-directory

myPath = (currPath + '/' + savePath)# The full path of the new sub-dir

#-----------------------------------#
# Set up place to save spreadsheet
#-----------------------------------#
if not os.path.exists(myPath):      # The directory you are in NOW
   
    os.makedirs(myPath)             # create a new dir below the dir your are in NOW

os.chdir(myPath)                    # move into the newly created sub-dir

print("You are now in dir", os.getcwd())

saveFile=(dailySYSTABLE + '.csv')    # The RESUlTS we are saving on a daily basis

#######################################
# Start the database connection using 
# pyexasol connector
#######################################

try:

    C = pyexasol.connect(dsn=IP+':'+PORT, user=SYS, password=SYS_PW, schema=SCHEMA)
    
    print("INFO: Successfully connected to database using schema", SCHEMA)

except Exception as e:
    
    print("Unable to connect using ", SYS, SYS_PW, "with schema:", SCHEMA)
    
    print(e)
    
    sys.exit(0)

###############################################################################
#   #######   #     ####    #      ######  ##
#      #     #  #   #   #   #      #        #
#      #    ######  ####    #      ###      #
#      #    #    #  #   #   #      #        #
#      #    #    #  ####    #####  ###### #####
###############################################################################

#######################################
# Extract TBL1 Hourly Records
#######################################

try:

    print()

    db_raw_hourlyFile = C.export_to_list(DB_SIZE_HOURLY_TBL, export_params={"columns": COLS_TBL1}) #["INTERVAL_START",COLUMN_1, COLUMN_2]})

    stmt = C.last_statement()

    print(f'EXPORTED Hourly-records: {stmt.rowcount()} rows in {stmt.execution_time}s')

    print("You are currently in", os.getcwd())
    

except Exception as e:

    print("Unable to READ EXA_DB_SIZE_HOURLY, skipping")

    print(e)

    sys.exit(0)


#######################################
# For TBL1 Hourly Table - read past 5 days
#######################################   

date_N_hours_ago = dt.datetime.now() - timedelta(hours= N_hours)

df_raw_hourly = pd.DataFrame(db_raw_hourlyFile, columns = COLS_TBL1) #["INTERVAL_START", COLUMN_1, COLUMN_2])


df_raw_hourly.reset_index(inplace = True, drop = True)

df_raw_hourly[COLUMN_DATE] = pd.to_datetime(df_raw_hourly[COLUMN_DATE])

df_raw_pristine = df_raw_hourly[:]

try:

    df_raw_hourly.set_index(COLUMN_DATE, inplace = True)

    df_raw_hourly.to_csv('db_size_mem_object_hourly_{}'.format(savePath) + '.csv')

except Exception as e:

    print("Unable to Save Hourly extract as csv. Skipping")

    print(e)

finally:

    df_raw_hourly.reset_index(inplace = True)

# #-------------------------------------#
# # Filter out dates beyond 5 days ago
# #-------------------------------------#

row_cnt = 0

col_cnt = 3

for row in db_raw_hourlyFile:
    
    for col in row:
    
        if (col_cnt % 3) == 0:
    
            col = pd.to_datetime(col[:11])
    
            INTERVAL_START.append(col)

        elif (col_cnt % 3) == 1:
    
            LIST_RAW_SIZE_AVG.append(float(col))
    
        elif (col_cnt % 3) == 2:
    
            LIST_RAW_SIZE_MAX.append(float(col))
    
        col_cnt +=1
    
    row_cnt +=1



#######################################
# Extract Daily Records
#######################################

try:

    print()

    dailyFile = C.export_to_list(DB_SIZE_DAILY_TBL)

    stmt = C.last_statement()

    print(f'EXPORTED Daily-records: {stmt.rowcount()} rows in {stmt.execution_time}s')

    print("You are currently in", os.getcwd())
    

except Exception as e:

    print("Unable to READ EXA_DB_SIZE_DAILY, skipping")

    print(e)

    sys.exit(0)  


#######################################
# For Daily Table - read past 5 days
#######################################   

date_N_days_ago = dt.datetime.now() - timedelta(days=N_days)
df_mem_daily = pd.DataFrame(dailyFile, columns = ["INTERVAL_START",
    "RAW_OBJECT_SIZE_AVG", 
    "RAW_OBJECT_SIZE_MAX",
    "MEM_OBJECT_SIZE_AVG",
    "MEM_OBJECT_SIZE_MAX",
    "AUXILIARY_SIZE_AVG",
    "AUXILIARY_SIZE_MAX",
    "STATISTICS_SIZE_AVG",
    "STATISTICS_SIZE_MAX",
    "SNAPSHOT_BACKUP_DATA_AVG",
    "SNAPSHOT_BACKUP_DATA_MAX",
    "RECOMMENDED_db_raw_SIZE_AVG",
    "RECOMMENDED_db_raw_SIZE_MAX",
    "STORAGE_SIZE_AVG",
    "STORAGE_SIZE_MAX",
    "USE_AVG",
    "USE_MAX",
    "OBJECT_COUNT_AVG",
    "OBJECT_COUNT_MAX"])
df_mem_daily.reset_index(inplace = True, drop = True)
df_mem_daily[COLUMN_DATE] = pd.to_datetime(df_mem_daily[COLUMN_DATE])
#-------------------------------------#
# Filter out dates beyond 5 days ago
#-------------------------------------#
mask = (df_mem_daily[COLUMN_DATE] >  date_N_days_ago ) #& (df_mem_daily['date'] <= end_date)
df_mem_daily = df_mem_daily.loc[mask]
try:
    
    df_mem_daily.set_index(COLUMN_DATE, inplace = True)
    
    df_mem_daily.to_csv('db_size_mem_object_daily_{}'.format(savePath) + '.csv')

except Exception as e:

    print("Unable to Save Daily extract as csv. Skipping")

    print(e)

finally:

    df_mem_daily.reset_index(inplace = True)

#######################################
# Set UP Hourly for past 24 hours
#######################################
# #-------------------------------------#
# # Filter out dates beyond 24 hours ago
# #-------------------------------------#
mask = (df_raw_hourly[COLUMN_DATE] >  date_N_hours_ago )

df_tbl1_hourly_day = df_raw_hourly.loc[mask]

cnt = 0

for mem_data_item in df_tbl1_hourly_day[COLUMN_1]:

    df_tbl1_hourly_day[COLUMN_1][cnt] = float(mem_data_item)

    cnt += 1

cnt = 0

for mem_data_item in df_tbl1_hourly_day[COLUMN_2]:

    df_tbl1_hourly_day[COLUMN_2][cnt] = float(mem_data_item)

    cnt += 1


#######################################
# EASTER EGG: FOR DICTIONARY
#######################################
# DICT_db_raw_SIZE_MAX = {}
# DICT_db_raw_SIZE_AVG = {}
# for TIME, AVG, MAX in dailyFile:
#         INTERVAL_START.append(TIME)
#         DICT_db_raw_SIZE_AVG[TIME] = AVG
#         DICT_db_raw_SIZE_MAX[TIME] = MAX
# print("DICT_db_raw_SIZE_AVG:", DICT_db_raw_SIZE_AVG)
# print("DICT_db_raw_SIZE_MAX:", DICT_db_raw_SIZE_MAX)
#######################################


###############################################################################
#   #######   #     ####    #      ######  ###
#      #     #  #   #   #   #      #      #   #
#      #    ######  ####    #      ###       #
#      #    #    #  #   #   #      #        #
#      #    #    #  ####    #####  ######  ####
###############################################################################


#######################################
# Extract  TBL2 Hourly Records
#######################################

try:

    print()

    db_mem_hourlyFile = C.export_to_list(DB_SIZE_HOURLY_TBL, export_params={"columns": COLS_TBL2}) #["INTERVAL_START",COLUMN_3, COLUMN_4]})

    stmt = C.last_statement()

    print(f'EXPORTED Hourly-records: {stmt.rowcount()} rows in {stmt.execution_time}s')

    print("You are currently in", os.getcwd())
    

except Exception as e:

    print("Unable to READ EXA_DB_SIZE_HOURLY, skipping")

    print(e)

    sys.exit(0)



#######################################
# For TBL2 Hourly Table - read past 5 days
#######################################   

date_N_hours_ago = dt.datetime.now() - timedelta(hours= N_hours)

df_mem_hourly = pd.DataFrame(db_mem_hourlyFile, columns = COLS_TBL2) #["INTERVAL_START", COLUMN_3, COLUMN_4])


df_mem_hourly.reset_index(inplace = True, drop = True)

df_mem_hourly[COLUMN_DATE] = pd.to_datetime(df_mem_hourly[COLUMN_DATE])

df_mem_pristine = df_mem_hourly[:]

try:

    df_mem_hourly.set_index(COLUMN_DATE, inplace = True)

    df_mem_hourly.to_csv('db_size_mem_object_hourly_{}'.format(savePath) + '.csv')

except Exception as e:

    print("Unable to Save Hourly extract as csv. Skipping")

    print(e)

finally:

    df_mem_hourly.reset_index(inplace = True)

row_cnt = 0

col_cnt = 3

for row in db_mem_hourlyFile:
    
    for col in row:
    
        if (col_cnt % 3) == 0:
    
            col = pd.to_datetime(col[:11])
    
            INTERVAL_START.append(col)

        elif (col_cnt % 3) == 1:
    
            LIST_MEM_SIZE_AVG.append(float(col))
    
        elif (col_cnt % 3) == 2:
    
            LIST_MEM_SIZE_MAX.append(float(col))
    
        col_cnt +=1
    
    row_cnt +=1

#DEBUG print("Hourly SB RAM extract Rows/Cols:", df_mem_hourly.shape)



#######################################
# Extract TBL2 Daily Records
#######################################

try:

    print()

    dailyFile = C.export_to_list(DB_SIZE_DAILY_TBL)

    stmt = C.last_statement()

    print(f'EXPORTED Daily-records: {stmt.rowcount()} rows in {stmt.execution_time}s')

    print("You are currently in", os.getcwd())
    

except Exception as e:

    print("Unable to READ EXA_DB_SIZE_DAILY, skipping")

    print(e)

    sys.exit(0)  



date_N_days_ago = dt.datetime.now() - timedelta(days=N_days)
df_mem_daily = pd.DataFrame(dailyFile, columns = ["INTERVAL_START",
    "RAW_OBJECT_SIZE_AVG", 
    "RAW_OBJECT_SIZE_MAX",
    "MEM_OBJECT_SIZE_AVG",
    "MEM_OBJECT_SIZE_MAX",
    "AUXILIARY_SIZE_AVG",
    "AUXILIARY_SIZE_MAX",
    "STATISTICS_SIZE_AVG",
    "STATISTICS_SIZE_MAX",
    "SNAPSHOT_BACKUP_DATA_AVG",
    "SNAPSHOT_BACKUP_DATA_MAX",
    "RECOMMENDED_db_mem_SIZE_AVG",
    "RECOMMENDED_db_mem_SIZE_MAX",
    "STORAGE_SIZE_AVG",
    "STORAGE_SIZE_MAX",
    "USE_AVG",
    "USE_MAX",
    "OBJECT_COUNT_AVG",
    "OBJECT_COUNT_MAX"])
df_mem_daily.reset_index(inplace = True, drop = True)
df_mem_daily[COLUMN_DATE] = pd.to_datetime(df_mem_daily[COLUMN_DATE])
#-------------------------------------#
# Filter out dates beyond 5 days ago
#-------------------------------------#
mask = (df_mem_daily[COLUMN_DATE] >  date_N_days_ago ) #& (df_mem_daily['date'] <= end_date)
df_mem_daily = df_mem_daily.loc[mask]

#######################################
# Set UP Hourly for past 24 hours
#######################################
# #-------------------------------------#
# # Filter out dates beyond 24 hours ago
# #-------------------------------------#
mask = (df_mem_hourly[COLUMN_DATE] >  date_N_hours_ago )

df_tbl2_hourly_day = df_mem_hourly.loc[mask]

cnt = 0

for mem_data_item in df_tbl2_hourly_day[COLUMN_3]:

    df_tbl2_hourly_day[COLUMN_3][cnt] = float(mem_data_item)

    cnt += 1

cnt = 0

for mem_data_item in df_tbl2_hourly_day[COLUMN_4]:

    df_tbl2_hourly_day[COLUMN_4][cnt] = float(mem_data_item)

    cnt += 1


###############################################################################
# #         # #########  #######
#  #       #      #     #
#   #     #       #       #
#    #   #        #         #
#     # #         #           #
#      #      ########## ####### ual
###############################################################################    

output_file("raw_obj_mem.html", title = "RAW & MEM")

###############################################################################
#   #######   #     ####    #      ######  ##
#      #     #  #   #   #   #      #        #
#      #    ######  ####    #      ###      #
#      #    #    #  #   #   #      #        #
#      #    #    #  ####    #####  ###### #####
###############################################################################


#######################################
# Visualize Hourly Past Day Data
#######################################



line_tbl1_hourly = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

line_tbl1_hourly.title.text = ("Past Week " +  DB_SIZE_HOURLY_TBL)

line_tbl1_hourly.title.align = "center"

line_tbl1_hourly.title.text_color = "white"

line_tbl1_hourly.title.text_font_size = "15px"

line_tbl1_hourly.title.background_fill_color = "darkblue"##aaaaee"

line_tbl1_hourly.line( x=COLUMN_DATE, y = COLUMN_2 , color=("red"),  source=df_tbl1_hourly_day, legend = ('DAILY ' + COLUMN_2))

line_tbl1_hourly.line( x=COLUMN_DATE, y = COLUMN_1 , color=("blue"), source=df_tbl1_hourly_day, legend = ("DAILY"  + COLUMN_1))

line_tbl1_hourly.legend.location = 'bottom_left'

#######################################
# Visualize Daily Data
#######################################


line_tbl1_daily = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

line_tbl1_daily.title.text = ("Past Month " + DB_SIZE_DAILY_TBL)

line_tbl1_daily.title.align = "center"

line_tbl1_daily.title.text_color = "white"

line_tbl1_daily.title.text_font_size = "15px"

line_tbl1_daily.title.background_fill_color = "darkblue"##aaaaee"

line_tbl1_daily.line( x=COLUMN_DATE, y =   COLUMN_2 , color=("red"),  source=df_mem_daily, legend = ('DAILY ' + COLUMN_2))#, legend = "db_raw_SIZE_MAX")#, hatch_weight = 5, legend_label="Sunrise")

line_tbl1_daily.line( x=COLUMN_DATE, y = COLUMN_1 , color=("blue"), source=df_mem_daily, legend = ("DAILY " + COLUMN_1))#, legend = ["db_raw_SIZE_AVG","db_raw_SIZE_MAX"])#, hatch_weight = 5, legend_label="Sunrise")

line_tbl1_daily.legend.location = 'bottom_left'

#######################################
# Visualize Monthly Data
#######################################

vbar_tbl1_source = ColumnDataSource(data=dict(x = INTERVAL_START, 
                                   y1 = LIST_RAW_SIZE_AVG, 
                                   y2 = LIST_RAW_SIZE_MAX, 
                                   label = [COLUMN_1, COLUMN_2]))


vbar_tbl1_tot_col1 = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

vbar_tbl1_tot_col1.title.text = ("TOT. " + DB_SIZE_HOURLY_TBL)

vbar_tbl1_tot_col1.title.align = "center"

vbar_tbl1_tot_col1.title.text_color = "white"

vbar_tbl1_tot_col1.title.text_font_size = "15px"

vbar_tbl1_tot_col1.title.background_fill_color = "darkblue"

vbar_tbl1_tot_col1.vbar(x = 'x', top = 'y1', color= "blue",  width = 3, source=vbar_tbl1_source, legend = COLUMN_1)

vbar_tbl1_tot_col1.legend.location = 'bottom_left'


varea_tbl1_stack_source = ColumnDataSource(data=dict(x = INTERVAL_START, 
                                   y1 = LIST_RAW_SIZE_AVG, 
                                   y2 = LIST_RAW_SIZE_MAX, 
                                   label = [COLUMN_1, COLUMN_2]))


vbar_tbl1_tot_col2 = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

vbar_tbl1_tot_col2.title.text = ("TOT. " + DB_SIZE_HOURLY_TBL)

vbar_tbl1_tot_col2.title.align = "center"

vbar_tbl1_tot_col2.title.text_color = "white"

vbar_tbl1_tot_col2.title.text_font_size = "15px"

vbar_tbl1_tot_col2.title.background_fill_color = "darkblue"

vbar_tbl1_tot_col2.vbar(x = 'x', top = 'y2', color= "red",  width = 3, source=varea_tbl1_stack_source, legend = COLUMN_2)




# MEM_OBJECT_GRIDPLOT = gridplot([[vbar_tbl1_tot_col1, vbar_tbl1_tot_col2, line_tbl1_daily, line_tbl1_hourly]], toolbar_location='right')

###############################################################################
#   #######   #     ####    #      ######  ###
#      #     #  #   #   #   #      #      #   #
#      #    ######  ####    #      ###       #
#      #    #    #  #   #   #      #        #
#      #    #    #  ####    #####  ######  ####
###############################################################################

#######################################
# Visualize Daily Data
#######################################

line_tbl2_hourly = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

line_tbl2_hourly.title.text = ("Past Week " +  DB_SIZE_HOURLY_TBL)

line_tbl2_hourly.title.align = "center"

line_tbl2_hourly.title.text_color = "white"

line_tbl2_hourly.title.text_font_size = "15px"

line_tbl2_hourly.title.background_fill_color = "darkblue"##aaaaee"

line_tbl2_hourly.line( x=COLUMN_DATE, y = COLUMN_4 , color=("red"),  source=df_tbl2_hourly_day, legend = ('DAILY ' + COLUMN_4))

line_tbl2_hourly.line( x=COLUMN_DATE, y = COLUMN_3 , color=("blue"), source=df_tbl2_hourly_day, legend = ("DAILY"  + COLUMN_3))

line_tbl2_hourly.legend.location = 'bottom_left'



line_tbl2_daily = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

line_tbl2_daily.title.text = ("Past Month " + DB_SIZE_DAILY_TBL)

line_tbl2_daily.title.align = "center"

line_tbl2_daily.title.text_color = "white"

line_tbl2_daily.title.text_font_size = "15px"

line_tbl2_daily.title.background_fill_color = "darkblue"##aaaaee"

line_tbl2_daily.line( x=COLUMN_DATE, y =   COLUMN_4 , color=("red"),  source=df_mem_daily, legend = ('DAILY ' + COLUMN_4))#, legend = "db_mem_SIZE_MAX")#, hatch_weight = 5, legend_label="Sunrise")

line_tbl2_daily.line( x=COLUMN_DATE, y = COLUMN_3 , color=("blue"), source=df_mem_daily, legend = ("DAILY " + COLUMN_3))#, legend = ["db_mem_SIZE_AVG","db_mem_SIZE_MAX"])#, hatch_weight = 5, legend_label="Sunrise")

line_tbl2_daily.legend.location = 'bottom_left'

#######################################
# Visualize Monthly Data
#######################################

vbar_tbl2_source = ColumnDataSource(data=dict(x = INTERVAL_START, 
                                   y1 = LIST_MEM_SIZE_AVG, 
                                   y2 = LIST_MEM_SIZE_MAX, 
                                   label = [COLUMN_3, COLUMN_4]))


vbar_tbl2_tot_col1 = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

vbar_tbl2_tot_col1.title.text = ("TOT. " + DB_SIZE_HOURLY_TBL)

vbar_tbl2_tot_col1.title.align = "center"

vbar_tbl2_tot_col1.title.text_color = "white"

vbar_tbl2_tot_col1.title.text_font_size = "15px"

vbar_tbl2_tot_col1.title.background_fill_color = "darkblue"

vbar_tbl2_tot_col1.vbar(x = 'x', top = 'y1', color= "blue",  width = 3, source=vbar_tbl2_source, legend = COLUMN_3)

vbar_tbl2_tot_col1.legend.location = 'bottom_left'


varea_tbl2_stack_source = ColumnDataSource(data=dict(x = INTERVAL_START, 
                                   y1 = LIST_MEM_SIZE_AVG, 
                                   y2 = LIST_MEM_SIZE_MAX, 
                                   label = [COLUMN_3, COLUMN_4]))


vbar_tbl2_tot_col2 = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

vbar_tbl2_tot_col2.title.text = ("TOT. " + DB_SIZE_HOURLY_TBL)

vbar_tbl2_tot_col2.title.align = "center"

vbar_tbl2_tot_col2.title.text_color = "white"

vbar_tbl2_tot_col2.title.text_font_size = "15px"

vbar_tbl2_tot_col2.title.background_fill_color = "darkblue"

vbar_tbl2_tot_col2.vbar(x = 'x', top = 'y2', color= "red",  width = 3, source=varea_tbl2_stack_source, legend = COLUMN_4)














MEM_OBJECT_GRIDPLOT = gridplot([[vbar_tbl1_tot_col1, vbar_tbl1_tot_col2, line_tbl1_daily, line_tbl1_hourly], [vbar_tbl2_tot_col1, vbar_tbl2_tot_col2, line_tbl2_daily, line_tbl2_hourly]], toolbar_location='right')

show(MEM_OBJECT_GRIDPLOT)

output_file("RAW_MEM_ALT.html", title = "RAW ALT")

x = INTERVAL_START

y = LIST_RAW_SIZE_MAX

t = figure(plot_width = (int(plotWidth *.8 )), plot_height = int(int((plotHeight * .8))), x_axis_type = 'datetime')

t.line(x, y, color = 'green')

t.circle(x, y, color = 'red', legend_label = COLUMN_2)

p = figure(plot_width=int((plotWidth * .8)), plot_height=int((plotHeight * .8)))

q = figure(plot_width = int((plotWidth * .8)), plot_height = int((plotHeight * .8)), x_axis_type = 'datetime')

r = figure(plot_width = int((plotWidth * .8)), plot_height = int((plotHeight * .8)), x_axis_type = 'datetime')

s = figure(plot_width = int((plotWidth * .8)), plot_height = int((plotHeight * .8)), x_axis_type = 'datetime')

vbar_tbl1_source = ColumnDataSource(data=dict(
        x=list(INTERVAL_START),
        y1 = LIST_RAW_SIZE_AVG,
        y2= LIST_RAW_SIZE_MAX))
p.varea_stack(['y1', 'y2'], x='x', color=("blue", "red"), source=vbar_tbl1_source, legend_label = [COLUMN_1, COLUMN_2])

q.line(INTERVAL_START, LIST_RAW_SIZE_AVG, color = 'navy', alpha = 0.9, line_width = 2, legend_label = COLUMN_1)

q.line(INTERVAL_START, LIST_RAW_SIZE_MAX, color = 'red', alpha = 0.2, line_width = 4, legend_label = COLUMN_2)

r.line(INTERVAL_START, LIST_RAW_SIZE_AVG, color = 'navy', alpha = 0.5 , legend_label = COLUMN_1)

s.line(INTERVAL_START, LIST_RAW_SIZE_MAX, color = 'red', alpha = 0.5,  legend_label = COLUMN_2)

show(gridplot([[p, q, r, s, t]], toolbar_location = 'left'))




#show(t)