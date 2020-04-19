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

try:
    
    import configparser

except:
    
    os.system('pip install configparser')
    
    import configparser

try:

    from tools_parse_config import ParseConfig

except:
    
    msg = "Unable to find tools_parse_config.py"

    print("#######################################")

    print("# ERROR in", os.path.basename(__file__))
    
    print(msg)

    print("#", os.path.basename(__file__), "aborting with no action taken.")

    print("#######################################")

    sys.exit(0)
    
    
#######################################
# Set up processinging logic
#######################################

if __name__ == "__main__":

    if len(sys.argv) > 1:

        in_ticket = sys.argv[1]

    else:
       
        in_ticket = 28615

    if len(sys.argv) > 2:

        class_chart = sys.argv[2]

    else:

        class_chart = 'DB_SIZE'
else:
   
    in_ticket = sys.argv[1]

    class_chart = sys.argv[2]



in_dir = str("EXA-" + str(in_ticket))

if not os.path.exists(in_dir):

    print("#######################################")

    print("# FATAL ERROR")

    print("#")

    print("# Needed path", in_dir)

    print("# is NOT available for", os.path.basename(__file__))

    print("# --> was directory", in_dir, "created?")

    print("# --> it is created but not a directory?")

    print("# --> Is it a directory and read-only?")

    print("#")

    print("# *** See subr_jira_download.py for creating needed directory")

    print("#")

    print("# Aborting with no action taken")

    print("#######################################")

    sys.exit(0)


#######################################
# C H A N G E    D I R E C T O R Y
#######################################

os.chdir(in_dir) 

#######################################
# VARIABLES
#######################################

dailySYSTABLE = ""

N_days = 30                            #DAILY SYS Table over past Month

N_hours = 168                          #HOURLY SYS Table over past week

N_hourly_days = 7                      #Needs to match N_hours 

plotWidth=400

plotHeight=300

b = ParseConfig(class_chart)

config_sections = b.read_config_sections()

#######################################
# LOOP for duration of the program
#
# #      # # #   # # #   #  #
# #      #   #   #   #   #    #
# #      #   #   #   #   #  #
# #      #   #   #   #   #
# # # #  # # #   # # #   #
# 
########################################

for config_section in config_sections:

    process_section = ParseConfig(config_section)

    CONFIG_HOURLY_TBL,CONFIG_DAILY_TBL,CONFIG_ROW1_COL_X_AXIS,CONFIG_ROW1_COL_Y_AXIS_1,CONFIG_ROW1_COL_Y_AXIS_2,CONFIG_ROW2_COL_X_AXIS,CONFIG_ROW2_COL_Y_AXIS_1,CONFIG_ROW2_COL_Y_AXIS_2,CONFIG_ROW3_COL_X_AXIS,CONFIG_ROW3_COL_Y_AXIS_1,CONFIG_ROW3_COL_Y_AXIS_2,CONFIG_ROW4_COL_X_AXIS,CONFIG_ROW4_COL_Y_AXIS_1,CONFIG_ROW4_COL_Y_AXIS_2 = process_section.run()

    DAILY_TBL   =  CONFIG_DAILY_TBL

    HOURLY_TBL  =  CONFIG_HOURLY_TBL

    COLUMN_DATE  = CONFIG_ROW1_COL_X_AXIS
    COLUMN_1     = CONFIG_ROW1_COL_Y_AXIS_1 
    COLUMN_2     = CONFIG_ROW1_COL_Y_AXIS_2
    COLUMN_3     = CONFIG_ROW2_COL_Y_AXIS_1
    COLUMN_4     = CONFIG_ROW2_COL_Y_AXIS_2
    COLUMN_5     = CONFIG_ROW3_COL_Y_AXIS_1
    COLUMN_6     = CONFIG_ROW3_COL_Y_AXIS_2
    COLUMN_7     = CONFIG_ROW4_COL_Y_AXIS_1
    COLUMN_8     = CONFIG_ROW4_COL_Y_AXIS_2

    COLS_TBL1 = [COLUMN_DATE, COLUMN_1, COLUMN_2]
    COLS_TBL2 = [COLUMN_DATE, COLUMN_3, COLUMN_4]
    COLS_TBL3 = [COLUMN_DATE, COLUMN_5, COLUMN_6]
    COLS_TBL4 = [COLUMN_DATE, COLUMN_7, COLUMN_8]

    print("#######################################")

    print("# INFO:", os.path.basename(__file__))

    print("# Config section:\t", config_section)

    print("# with HOURLY_TBL:\t", HOURLY_TBL)

    print("# and DAILY_TBL:\t",  DAILY_TBL)

    print("#######################################")

    print()

#######################################
# Set up directory to use
#######################################

    currPath = os.getcwd()              # Directory you are in NOW

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

        df_hourly_full_tbl_1 = pd.read_csv(HOURLY_TBL + '.csv')#, columns = ["INTERVAL_START", "RAW_OBJECT_SIZE_AVG", "RAW_OBJECT_SIZE_MAX", "MEM_OBJECT_SIZE_AVG","MEM_OBJECT_SIZE_MAX","AUXILIARY_SIZE_AVG","AUXILIARY_SIZE_MAX", "STATISTICS_SIZE_AVG","STATISTICS_SIZE_MAX","SNAPSHOT_BACKUP_DATA_AVG","SNAPSHOT_BACKUP_DATA_MAX","RECOMMENDED_DB_RAM_SIZE_AVG","RECOMMENDED_DB_RAM_SIZE_MAX","STORAGE_SIZE_AVG","STORAGE_SIZE_MAX","USE_AVG","USE_MAX","OBJECT_COUNT_AVG", "OBJECT_COUNT_MAX"])

    except Exception as e:

        print("#######################################")

        print("# FATAL ERROR in", os.path.basename(__file__))

        print("# ---> File is NOT FOUND!")

        print("#")

        print("# config.ini section:\t", config_section)

        print("# which specified:\t", HOURLY_TBL)

        print("# Needs CSV file:\t", str(HOURLY_TBL + '.csv'))

        print("# in directory:\t\t", in_dir + ".")

        print("# Aborting with no action taken.")

        print("#######################################")

        print(e)

        sys.exit(0)

    try:

        df_hourly_full_tbl_1 = df_hourly_full_tbl_1[COLS_TBL1]

        df_hourly_full_tbl_1_extracted = df_hourly_full_tbl_1.shape[0]


    except Exception as e:

        print("Unable to READ", HOURLY_TBL, "skipping")

        print(e)

        sys.exit(0)

    #######################################
    # Extract TBL1 Daily Records
    #######################################

    try:

        df_daily_full_tbl_1 = pd.read_csv(DAILY_TBL + '.csv', usecols = COLS_TBL1)

    except Exception as e:

        print("#######################################")

        print("# FATAL ERROR in", os.path.basename(__file__))

        print("# ---> File is NOT FOUND!")

        print("#")

        print("# config.ini section:\t", config_section)

        print("# which specified:\t", DAILY_TBL)

        print("# Needs CSV file:\t", str(DAILY_TBL + '.csv'))

        print("# in directory:\t\t", in_dir + ".")

        print("# Aborting with no action taken.")

        print("#######################################")

        print(e)

        sys.exit(0)


    try:

        df_daily_full_tbl_1 = df_daily_full_tbl_1[COLS_TBL1]

        df_daily_full_tbl_1_extracted =  df_daily_full_tbl_1.shape[0]

    except Exception as e:

        print("Unable to read", DAILY_TBL, "skipping")

        print(e)

        sys.exit(0)

    #######################################
    # Read the max df_hourly_full_tbl_1 timestamp
    #######################################

    try:

        df_hourly_full_tbl_1['INTERVAL_START'] = pd.to_datetime(df_hourly_full_tbl_1['INTERVAL_START'])

    except Exception as e:

        print("#######################################")

        print("#Error in ", os.path.basename(__file__))

        print("#")

        print("#")

        print("#")

        print(e)

        print("#######################################")

        sys.exit(0)

    date_max_hourly = df_hourly_full_tbl_1[COLUMN_DATE].max()

    print("# INFO:", os.path.basename(__file__), " read", HOURLY_TBL, "date_max_hourly:", date_max_hourly)

    #######################################
    # Read the max df_daily_full_tbl_1 timestamp
    #######################################

    df_daily_full_tbl_1[COLUMN_DATE] = pd.to_datetime(df_daily_full_tbl_1[COLUMN_DATE])

    date_max_daily = df_daily_full_tbl_1[COLUMN_DATE].max()

    print("# INFO:", os.path.basename(__file__), " read", DAILY_TBL, "date_max_daily:", date_max_daily)

    #######################################
    # For TBL1 Hourly Table - read past 5 days
    #######################################   

    date_N_hours_ago = date_max_hourly - timedelta(hours= N_hours)

    df_hourly_work_tbl_1 = pd.DataFrame(df_hourly_full_tbl_1, columns = COLS_TBL1).copy(deep = True) #["INTERVAL_START", COLUMN_1, COLUMN_2])

    df_hourly_work_tbl_1.reset_index(inplace = True, drop = True)

    df_hourly_work_tbl_1[COLUMN_DATE] = pd.to_datetime(df_hourly_work_tbl_1[COLUMN_DATE])

    mask = (df_hourly_work_tbl_1[COLUMN_DATE] >  date_N_hours_ago )

    df_hourly_7_day_tbl_1 = df_hourly_work_tbl_1.loc[mask].copy(deep = True)

    #######################################
    # For TBL1 Daily Table - read past 30 days
    #######################################   

    date_N_days_ago = date_max_daily - timedelta(days = N_days)

    df_daily_work_tbl_1 = pd.DataFrame(df_daily_full_tbl_1, columns = COLS_TBL1).copy(deep = True) #["INTERVAL_START", COLUMN_1, COLUMN_2])

    df_daily_work_tbl_1.reset_index(inplace = True, drop = True)

    df_daily_work_tbl_1[COLUMN_DATE] = pd.to_datetime(df_daily_work_tbl_1[COLUMN_DATE])

    mask = (df_daily_work_tbl_1[COLUMN_DATE] >  date_N_days_ago )

    df_daily_30_day_tbl_1 = df_daily_work_tbl_1.loc[mask].copy(deep = True)




    ###############################################################################
    #   #######   #     ####    #      ######  ###
    #      #     #  #   #   #   #      #      #   #
    #      #    ######  ####    #      ###       #
    #      #    #    #  #   #   #      #        #
    #      #    #    #  ####    #####  ######  ####
    ###############################################################################


    #######################################bbb
    # Extract TBL2 Hourly Records
    #######################################

    try:

        df_hourly_full_tbl_2 = pd.read_csv(HOURLY_TBL + '.csv', usecols = COLS_TBL2)#  export_params={"columns": COLS_TBL2}) #["INTERVAL_START",COLUMN_1, COLUMN_2]})

        df_hourly_full_tbl_2_extracted = df_hourly_full_tbl_2.shape[0]


    except Exception as e:

        print("Unable to READ", HOURLY_TBL + "...Aborting with no action taken.")

        print(e)

        sys.exit(0)

    #######################################
    # Extract TBL2 Daily Records
    #######################################

    try:

        df_daily_full_tbl_2 = pd.read_csv(DAILY_TBL + '.csv', usecols = COLS_TBL2)#  export_params={"columns": COLS_TBL2}) #["INTERVAL_START",COLUMN_1, COLUMN_2]})

        df_daily_full_tbl_2_extracted =  df_daily_full_tbl_2.shape[0]


    except Exception as e:

        print("Unable to READ EXA_DB_SIZE_DAILY, skipping")

        print(e)

        sys.exit(0)

    #######################################
    #  Set COLUMN_DATE as timestamp for Hourly full tbl 2
    #######################################

    df_hourly_full_tbl_2[COLUMN_DATE] = pd.to_datetime(df_hourly_full_tbl_2[COLUMN_DATE])

    #######################################
    # For TBL2 Hourly Table - read past 5 days
    #######################################   

    date_N_hours_ago = date_max_hourly - timedelta(hours= N_hours)

    df_hourly_work_tbl_2 = pd.DataFrame(df_hourly_full_tbl_2, columns = COLS_TBL2).copy(deep = True) #["INTERVAL_START", COLUMN_1, COLUMN_2])



    df_hourly_work_tbl_2.reset_index(inplace = True, drop = True)

    df_hourly_work_tbl_2[COLUMN_DATE] = pd.to_datetime(df_hourly_work_tbl_2[COLUMN_DATE])

    mask = (df_hourly_work_tbl_2[COLUMN_DATE] >  date_N_hours_ago )

    df_hourly_7_day_tbl_2 = df_hourly_work_tbl_2.loc[mask].copy(deep = True) 

    #######################################
    # For TBL2 Daily Table - read past 30 days
    #######################################   

    date_N_days_ago = date_max_daily - timedelta(days = N_days)

    df_daily_work_tbl_2 = pd.DataFrame(df_daily_full_tbl_2, columns = COLS_TBL2).copy(deep = True)  #["INTERVAL_START", COLUMN_1, COLUMN_2])

    df_daily_work_tbl_2.reset_index(inplace = True, drop = True)

    df_daily_work_tbl_2[COLUMN_DATE] = pd.to_datetime(df_daily_work_tbl_2[COLUMN_DATE])

    mask = (df_daily_work_tbl_2[COLUMN_DATE] >  date_N_days_ago )

    df_daily_30_day_tbl_2 = df_daily_work_tbl_2.loc[mask].copy(deep = True)

    ###############################################################################
    #   #######   #     ####    #      ######  ####
    #      #     #  #   #   #   #      #         #
    #      #    ######  ####    #      ###      ####
    #      #    #    #  #   #   #      #           #
    #      #    #    #  ####    #####  ###### #####
    ###############################################################################

    #######################################
    # Extract TBL3 Hourly Records
    #######################################

    try:

        df_hourly_full_tbl_3 = pd.read_csv(HOURLY_TBL + '.csv', usecols = COLS_TBL3)

        df_hourly_full_tbl_3_extracted = df_hourly_full_tbl_3.shape[0]


    except Exception as e:

        print("Unable to READ EXA_DB_SIZE_HOURLY, skipping")

        print(e)

        sys.exit(0)

    #######################################
    # Extract TBL3 Daily Records
    #######################################

    try:

        df_daily_full_tbl_3 = pd.read_csv(DAILY_TBL + '.csv', usecols = COLS_TBL3)#  export_params={"columns": COLS_TBL3}) #["INTERVAL_START",COLUMN_5, COLUMN_6]})

        df_daily_full_tbl_3_extracted = df_daily_full_tbl_3.shape[0]


    except Exception as e:

        print("Unable to READ EXA_DB_SIZE_DAILY, skipping")

        print(e)

        sys.exit(0)

    #######################################
    # Read the max df_hourly_full_tbl_3 timestamp
    #######################################

    df_hourly_full_tbl_3[COLUMN_DATE] = pd.to_datetime(df_hourly_full_tbl_3[COLUMN_DATE])

    date_max_hourly = df_hourly_full_tbl_3[COLUMN_DATE].max()

    #######################################
    # Read the max df_daily_full_tbl_3 timestamp
    #######################################

    df_daily_full_tbl_3[COLUMN_DATE] = pd.to_datetime(df_daily_full_tbl_3[COLUMN_DATE])

    date_max_daily = df_daily_full_tbl_3[COLUMN_DATE].max()

    #######################################
    # For TBL3 Hourly Table - read past 5 days
    #######################################   

    date_N_hours_ago = date_max_hourly - timedelta(hours= N_hours)

    df_hourly_work_tbl_3 = pd.DataFrame(df_hourly_full_tbl_3, columns = COLS_TBL3).copy(deep = True) #["INTERVAL_START", COLUMN_5, COLUMN_6])

    df_hourly_work_tbl_3.reset_index(inplace = True, drop = True)

    df_hourly_work_tbl_3[COLUMN_DATE] = pd.to_datetime(df_hourly_work_tbl_3[COLUMN_DATE])

    mask = (df_hourly_work_tbl_3[COLUMN_DATE] >  date_N_hours_ago )

    df_hourly_7_day_tbl_3 = df_hourly_work_tbl_3.loc[mask].copy(deep = True)

    #######################################
    # For TBL3 Daily Table - read past 30 days
    #######################################   

    date_N_days_ago = date_max_daily - timedelta(days = N_days)

    df_daily_work_tbl_3 = pd.DataFrame(df_daily_full_tbl_3, columns = COLS_TBL3).copy(deep = True) #["INTERVAL_START", COLUMN_5, COLUMN_6])

    df_daily_work_tbl_3.reset_index(inplace = True, drop = True)

    df_daily_work_tbl_3[COLUMN_DATE] = pd.to_datetime(df_daily_work_tbl_3[COLUMN_DATE])

    mask = (df_daily_work_tbl_3[COLUMN_DATE] >  date_N_days_ago )

    df_daily_30_day_tbl_3 = df_daily_work_tbl_3.loc[mask].copy(deep = True)

    ###############################################################################
    #   #######   #     ####    #      ######    #
    #      #     #  #   #   #   #      #       # #
    #      #    ######  ####    #      ###    ######
    #      #    #    #  #   #   #      #         #
    #      #    #    #  ####    #####  ######  ####
    ###############################################################################


    #######################################
    # Extract TBL4 Hourly Records
    #######################################

    try:

        df_hourly_full_tbl_4 = pd.read_csv(HOURLY_TBL + '.csv', usecols = COLS_TBL4)#  export_params={"columns": COLS_TBL4}) #["INTERVAL_START",COLUMN_5, COLUMN_6]})

        df_hourly_full_tbl_4_extracted = df_hourly_full_tbl_4.shape[0]


    except Exception as e:

        print("Unable to READ EXA_DB_SIZE_HOURLY, skipping")

        print(e)

        sys.exit(0)

    #######################################
    # Extract TBL4 Daily Records
    #######################################

    try:

        df_daily_full_tbl_4 = pd.read_csv(DAILY_TBL + '.csv', usecols = COLS_TBL4)#  export_params={"columns": COLS_TBL4}) #["INTERVAL_START",COLUMN_5, COLUMN_6]})

        df_daily_full_tbl_4_extracted = df_daily_full_tbl_4.shape[0]


    except Exception as e:

        print("Unable to READ EXA_DB_SIZE_DAILY, skipping")

        print(e)

        sys.exit(0)

    #######################################
    #  Set COLUMN_DATE as timestamp for Hourly full tbl 2
    #######################################

    df_hourly_full_tbl_4[COLUMN_DATE] = pd.to_datetime(df_hourly_full_tbl_4[COLUMN_DATE])

    #######################################
    # For TBL4 Hourly Table - read past 5 days
    #######################################   

    date_N_hours_ago = date_max_hourly - timedelta(hours= N_hours)

    df_hourly_work_tbl_4 = pd.DataFrame(df_hourly_full_tbl_4, columns = COLS_TBL4).copy(deep = True) #["INTERVAL_START", COLUMN_5, COLUMN_6])


    df_hourly_work_tbl_4.reset_index(inplace = True, drop = True)

    df_hourly_work_tbl_4[COLUMN_DATE] = pd.to_datetime(df_hourly_work_tbl_4[COLUMN_DATE])

    mask = (df_hourly_work_tbl_4[COLUMN_DATE] >  date_N_hours_ago )

    df_hourly_7_day_tbl_4 = df_hourly_work_tbl_4.loc[mask].copy(deep = True) 

    #######################################
    # For TBL4 Daily Table - read past 30 days
    #######################################   

    date_N_days_ago = date_max_daily - timedelta(days = N_days)

    df_daily_work_tbl_4 = pd.DataFrame(df_daily_full_tbl_4, columns = COLS_TBL4).copy(deep = True)

    df_daily_work_tbl_4.reset_index(inplace = True, drop = True)

    df_daily_work_tbl_4[COLUMN_DATE] = pd.to_datetime(df_daily_work_tbl_4[COLUMN_DATE])

    mask = (df_daily_work_tbl_4[COLUMN_DATE] >  date_N_days_ago )

    df_daily_30_day_tbl_4 = df_daily_work_tbl_4.loc[mask].copy(deep = True)

    ###############################################################################
    # Convert Hourly full TBL1 COLUMN_1 / _2 to float
    ###############################################################################

    df_hourly_full_tbl_1[COLUMN_1] = df_hourly_full_tbl_1[COLUMN_1].astype(float)

    df_hourly_full_tbl_1[COLUMN_2] = df_hourly_full_tbl_1[COLUMN_2].astype(float)

    ###############################################################################
    # Convert Hourly 5 day TBL1 COLUMN_1 / _2 to float
    ###############################################################################

    df_hourly_7_day_tbl_1[COLUMN_1] = df_hourly_7_day_tbl_1[COLUMN_1].astype(float)

    df_hourly_7_day_tbl_1[COLUMN_2] = df_hourly_7_day_tbl_1[COLUMN_2].astype(float)

    ###############################################################################
    # Convert Daily full TBL1 COLUMN_1 / _2 to float
    ###############################################################################

    df_daily_full_tbl_1[COLUMN_1] = df_daily_full_tbl_1[COLUMN_1].astype(float)

    df_daily_full_tbl_1[COLUMN_2] = df_daily_full_tbl_1[COLUMN_2].astype(float)

    ###############################################################################
    # Convert Daily 30 day TBL1 COLUMN_1 / _2 to float
    ###############################################################################

    df_daily_30_day_tbl_1[COLUMN_1] = df_daily_30_day_tbl_1[COLUMN_1].astype(float)

    df_daily_30_day_tbl_1[COLUMN_2] = df_daily_30_day_tbl_1[COLUMN_2].astype(float)

    ###############################################################################
    # Convert Hourly full TBL2 COLUMN_3 / _2 to float
    ###############################################################################

    df_hourly_full_tbl_2[COLUMN_3] = df_hourly_full_tbl_2[COLUMN_3].astype(float)

    df_hourly_full_tbl_2[COLUMN_4] = df_hourly_full_tbl_2[COLUMN_4].astype(float)

    ###############################################################################
    # Convert Hourly 5 day TBL2 COLUMN_3 / _2 to float
    ###############################################################################

    df_hourly_7_day_tbl_2[COLUMN_3] = df_hourly_7_day_tbl_2[COLUMN_3].astype(float)

    df_hourly_7_day_tbl_2[COLUMN_4] = df_hourly_7_day_tbl_2[COLUMN_4].astype(float)

    ###############################################################################
    # Convert Daily full TBL2 COLUMN_3 / _2 to float
    ###############################################################################

    df_daily_full_tbl_2[COLUMN_3] = df_daily_full_tbl_2[COLUMN_3].astype(float)

    df_daily_full_tbl_2[COLUMN_4] = df_daily_full_tbl_2[COLUMN_4].astype(float)

    ###############################################################################
    # Convert Daily 30 day TBL2 COLUMN_3 / _2 to float
    ###############################################################################

    df_daily_30_day_tbl_2[COLUMN_3] = df_daily_30_day_tbl_2[COLUMN_3].astype(float)

    df_daily_30_day_tbl_2[COLUMN_4] = df_daily_30_day_tbl_2[COLUMN_4].astype(float)

    ###############################################################################
    # Convert Hourly full TBL3 COLUMN_5 / _2 to float
    ###############################################################################

    df_hourly_full_tbl_3[COLUMN_5] = df_hourly_full_tbl_3[COLUMN_5].astype(float)

    df_hourly_full_tbl_3[COLUMN_6] = df_hourly_full_tbl_3[COLUMN_6].astype(float)

    ###############################################################################
    # Convert Hourly 5 day TBL3 COLUMN_5 / _2 to float
    ###############################################################################

    df_hourly_7_day_tbl_3[COLUMN_5] = df_hourly_7_day_tbl_3[COLUMN_5].astype(float)

    df_hourly_7_day_tbl_3[COLUMN_6] = df_hourly_7_day_tbl_3[COLUMN_6].astype(float)

    ###############################################################################
    # Convert Daily full TBL3 COLUMN_5 / _2 to float
    ###############################################################################

    df_daily_full_tbl_3[COLUMN_5] = df_daily_full_tbl_3[COLUMN_5].astype(float)

    df_daily_full_tbl_3[COLUMN_6] = df_daily_full_tbl_3[COLUMN_6].astype(float)

    ###############################################################################
    # Convert Daily 30 day TBL3 COLUMN_5 / _2 to float
    ###############################################################################

    df_daily_30_day_tbl_3[COLUMN_5] = df_daily_30_day_tbl_3[COLUMN_5].astype(float)

    df_daily_30_day_tbl_3[COLUMN_6] = df_daily_30_day_tbl_3[COLUMN_6].astype(float)

    ###############################################################################
    # Convert Hourly full TBL4 COLUMN_7 / _2 to float
    ###############################################################################

    df_hourly_full_tbl_4[COLUMN_7] = df_hourly_full_tbl_4[COLUMN_7].astype(float)

    df_hourly_full_tbl_4[COLUMN_8] = df_hourly_full_tbl_4[COLUMN_8].astype(float)

    ###############################################################################
    # Convert Hourly 5 day TBL4 COLUMN_7 / _2 to float
    ###############################################################################

    df_hourly_7_day_tbl_4[COLUMN_7] = df_hourly_7_day_tbl_4[COLUMN_7].astype(float)

    df_hourly_7_day_tbl_4[COLUMN_8] = df_hourly_7_day_tbl_4[COLUMN_8].astype(float)

    ###############################################################################
    # Convert Daily full TBL4 COLUMN_7 / _2 to float
    ###############################################################################

    df_daily_full_tbl_4[COLUMN_7] = df_daily_full_tbl_4[COLUMN_7].astype(float)

    df_daily_full_tbl_4[COLUMN_8] = df_daily_full_tbl_4[COLUMN_8].astype(float)

    ###############################################################################
    # Convert Daily 30 day TBL4 COLUMN_7 / _2 to float
    ###############################################################################

    df_daily_30_day_tbl_4[COLUMN_7] = df_daily_30_day_tbl_4[COLUMN_7].astype(float)

    df_daily_30_day_tbl_4[COLUMN_8] = df_daily_30_day_tbl_4[COLUMN_8].astype(float)

    ###############################################################################
    # #         # #########  ####### #       # 
    #  #       #      #     #        #       #
    #   #     #       #       #      #       #
    #    #   #        #         #    #       #
    #     # #         #           #  #       #
    #      #      ########## ####### ######### als   (fine, you type it out)
    ###############################################################################   


    output_title = str(config_section + '.html')

    output_file(output_title, title = config_section)

    ###############################################################################
    #   #######   #     ####    #      ######  ##
    #      #     #  #   #   #   #      #        #
    #      #    ######  ####    #      ###      #
    #      #    #    #  #   #   #      #        #
    #      #    #    #  ####    #####  ###### #####
    ###############################################################################

    #######################################
    # Visualize Hourly Past  5 Day Data
    #######################################

    line1_tbl1_hourly_7_day = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

    line1_tbl1_hourly_7_day.title.text = (str(N_hourly_days) + " Day " +  HOURLY_TBL)

    line1_tbl1_hourly_7_day.title.align = "center"

    line1_tbl1_hourly_7_day.title.text_color = "white"

    line1_tbl1_hourly_7_day.title.text_font_size = "15px"

    line1_tbl1_hourly_7_day.title.background_fill_color = "darkblue"##aaaaee"

    line1_tbl1_hourly_7_day.line( x=COLUMN_DATE, y = COLUMN_2 , color=("red"),  source=df_hourly_7_day_tbl_1, legend_label = ('DAILY ' + COLUMN_2))

    line1_tbl1_hourly_7_day.line( x=COLUMN_DATE, y = COLUMN_1 , color=("blue"), source=df_hourly_7_day_tbl_1, legend_label = ("DAILY"  + COLUMN_1))

    line1_tbl1_hourly_7_day.legend.location = 'bottom_left'


    #######################################
    # Visualized
    #######################################

    #######################################
    # Visualize Daily Data
    #######################################


    line1_tbl1_daily = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

    line1_tbl1_daily.title.text = ("Past Month " + DAILY_TBL)

    line1_tbl1_daily.title.align = "center"

    line1_tbl1_daily.title.text_color = "white"

    line1_tbl1_daily.title.text_font_size = "15px"

    line1_tbl1_daily.title.background_fill_color = "darkblue"##aaaaee"

    line1_tbl1_daily.line( x=COLUMN_DATE, y =   COLUMN_2 , color=("red"),  source=df_daily_30_day_tbl_1, legend_label = ('DAILY ' + COLUMN_2))#, legend = "db_raw_SIZE_MAX")#, hatch_weight = 5, legend_label="Sunrise")

    line1_tbl1_daily.line( x=COLUMN_DATE, y = COLUMN_1 , color=("blue"), source=df_daily_30_day_tbl_1, legend_label = ("DAILY " + COLUMN_1))#, legend = ["db_raw_SIZE_AVG","db_raw_SIZE_MAX"])#, hatch_weight = 5, legend_label="Sunrise")

    line1_tbl1_daily.legend.location = 'bottom_left'


    #######################################
    # Visualize Entire Data
    #######################################

    vbar_tbl1_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_1[COLUMN_DATE], #INTERVAL_START, 
                                       y1 = df_hourly_full_tbl_1[COLUMN_1], #LIST_RAW_SIZE_AVG, 
                                       y2 = df_hourly_full_tbl_1[COLUMN_2], #LIST_RAW_SIZE_MAX, 
                                       ))


    vbar_tbl1_tot_col1 = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

    vbar_tbl1_tot_col1.title.text = (HOURLY_TBL)

    vbar_tbl1_tot_col1.title.align = "center"

    vbar_tbl1_tot_col1.title.text_color = "yellow"

    vbar_tbl1_tot_col1.title.text_font_size = "15px"

    vbar_tbl1_tot_col1.title.background_fill_color = "darkblue"

    vbar_tbl1_tot_col1.vbar(x = 'x', top = 'y1', color= "blue",  width = 3, source=vbar_tbl1_source, legend_label = COLUMN_1)

    vbar_tbl1_tot_col1.legend.location = 'bottom_left'

    varea_tbl1_stack_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_1[COLUMN_DATE], 
                                       y1 = df_hourly_full_tbl_1[COLUMN_1],
                                       y2 = df_hourly_full_tbl_1[COLUMN_2],
                                       ))

    vbar_tbl1_tot_col2 = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

    vbar_tbl1_tot_col2.title.text = (HOURLY_TBL)

    vbar_tbl1_tot_col2.title.align = "center"

    vbar_tbl1_tot_col2.title.text_color = "yellow"

    vbar_tbl1_tot_col2.title.text_font_size = "15px"

    vbar_tbl1_tot_col2.title.background_fill_color = "darkblue"

    vbar_tbl1_tot_col2.vbar(x = 'x', top = 'y2', color= "red",  width = 3, source=varea_tbl1_stack_source, legend_label = COLUMN_2)

    ###############################################################################
    #   #######   #     ####    #      ######  ###
    #      #     #  #   #   #   #      #      #  #
    #      #    ######  ####    #      ###      #
    #      #    #    #  #   #   #      #       #
    #      #    #    #  ####    #####  ###### #####
    ###############################################################################

    #######################################
    # Visualize Hourly Past  5 Day Data
    #######################################

    line2_tbl2_hourly_7_day = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

    line2_tbl2_hourly_7_day.title.text = (str(N_hourly_days) + " Day " +  HOURLY_TBL)

    line2_tbl2_hourly_7_day.title.align = "center"

    line2_tbl2_hourly_7_day.title.text_color = "white"

    line2_tbl2_hourly_7_day.title.text_font_size = "15px"

    line2_tbl2_hourly_7_day.title.background_fill_color = "darkblue"##aaaaee"

    line2_tbl2_hourly_7_day.line( x=COLUMN_DATE, y = COLUMN_4 , color=("red"),  source=df_hourly_7_day_tbl_2, legend_label = ('DAILY ' + COLUMN_4))

    line2_tbl2_hourly_7_day.line( x=COLUMN_DATE, y = COLUMN_3 , color=("blue"), source=df_hourly_7_day_tbl_2, legend_label = ("DAILY"  + COLUMN_3))

    line2_tbl2_hourly_7_day.legend.location = 'bottom_left'


    #######################################
    # Visualized
    #######################################

    #######################################
    # Visualize Daily Data
    #######################################


    line2_tbl2_daily = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

    line2_tbl2_daily.title.text = ("Past Month " + DAILY_TBL)

    line2_tbl2_daily.title.align = "center"

    line2_tbl2_daily.title.text_color = "white"

    line2_tbl2_daily.title.text_font_size = "15px"

    line2_tbl2_daily.title.background_fill_color = "darkblue"##aaaaee"

    line2_tbl2_daily.line( x=COLUMN_DATE, y =   COLUMN_4 , color=("red"),  source=df_daily_30_day_tbl_2, legend_label = ('DAILY ' + COLUMN_4))#, legend = "db_tbl_2_SIZE_MAX")#, hatch_weight = 5, legend_label="Sunrise")

    line2_tbl2_daily.line( x=COLUMN_DATE, y = COLUMN_3 , color=("blue"), source=df_daily_30_day_tbl_2, legend_label = ("DAILY " + COLUMN_3))#, legend = ["db_tbl_2_SIZE_AVG","db_tbl_2_SIZE_MAX"])#, hatch_weight = 5, legend_label="Sunrise")

    line2_tbl2_daily.legend.location = 'bottom_left'


    #######################################
    # Visualize Entire Data
    #######################################

    vbar_tbl2_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_1[COLUMN_DATE], #INTERVAL_START, 
                                       y1 = df_hourly_full_tbl_2[COLUMN_3], #LIST_RAW_SIZE_AVG, 
                                       y2 = df_hourly_full_tbl_2[COLUMN_4])) #, #LIST_RAW_SIZE_MAX, 
                                       #label = [COLUMN_3, COLUMN_4]))


    vbar_tbl2_tot_col1 = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

    vbar_tbl2_tot_col1.title.text = (HOURLY_TBL)

    vbar_tbl2_tot_col1.title.align = "center"

    vbar_tbl2_tot_col1.title.text_color = "yellow"

    vbar_tbl2_tot_col1.title.text_font_size = "15px"

    vbar_tbl2_tot_col1.title.background_fill_color = "darkblue"

    vbar_tbl2_tot_col1.vbar(x = 'x', top = 'y1', color= "blue",  width = 3, source=vbar_tbl2_source, legend_label = COLUMN_3)

    vbar_tbl2_tot_col1.legend.location = 'bottom_left'


    varea_tbl2_stack_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_2[COLUMN_DATE], #INTERVAL_START, 
                                       y1 = df_hourly_full_tbl_2[COLUMN_3], #LIST_RAW_SIZE_AVG, 
                                       y2 = df_hourly_full_tbl_2[COLUMN_4], #LIST_RAW_SIZE_MAX, 
                                       ))

    vbar_tbl2_tot_col2 = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

    vbar_tbl2_tot_col2.title.text = (HOURLY_TBL)

    vbar_tbl2_tot_col2.title.align = "center"

    vbar_tbl2_tot_col2.title.text_color = "yellow"

    vbar_tbl2_tot_col2.title.text_font_size = "15px"

    vbar_tbl2_tot_col2.title.background_fill_color = "darkblue"

    vbar_tbl2_tot_col2.vbar(x = 'x', top = 'y2', color= "red",  width = 3, source=varea_tbl2_stack_source, legend_label = COLUMN_4)

    ###############################################################################
    #   #######   #     ####    #      ######  ####
    #      #     #  #   #   #   #      #         #
    #      #    ######  ####    #      ###      ####
    #      #    #    #  #   #   #      #           #
    #      #    #    #  ####    #####  ###### #####
    ###############################################################################


    #######################################
    # Visualize Hourly Past  5 Day Data
    #######################################

    line3_tbl3_hourly_7_day = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

    line3_tbl3_hourly_7_day.title.text = (str(N_hourly_days) + " Day " +  HOURLY_TBL)

    line3_tbl3_hourly_7_day.title.align = "center"

    line3_tbl3_hourly_7_day.title.text_color = "white"

    line3_tbl3_hourly_7_day.title.text_font_size = "15px"

    line3_tbl3_hourly_7_day.title.background_fill_color = "darkblue"##aaaaee"

    line3_tbl3_hourly_7_day.line( x=COLUMN_DATE, y = COLUMN_6 , color=("red"),  source=df_hourly_7_day_tbl_3, legend_label = ('DAILY ' + COLUMN_6))

    line3_tbl3_hourly_7_day.line( x=COLUMN_DATE, y = COLUMN_5 , color=("blue"), source=df_hourly_7_day_tbl_3, legend_label = ("DAILY"  + COLUMN_5))

    line3_tbl3_hourly_7_day.legend.location = 'bottom_left'


    #######################################
    # Visualized
    #######################################

    #######################################
    # Visualize Daily Data
    #######################################


    line3_tbl3_daily = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

    line3_tbl3_daily.title.text = ("Past Month " + DAILY_TBL)

    line3_tbl3_daily.title.align = "center"

    line3_tbl3_daily.title.text_color = "white"

    line3_tbl3_daily.title.text_font_size = "15px"

    line3_tbl3_daily.title.background_fill_color = "darkblue"##aaaaee"

    line3_tbl3_daily.line( x=COLUMN_DATE, y =   COLUMN_6 , color=("red"),  source=df_daily_30_day_tbl_3, legend_label = ('DAILY ' + COLUMN_6))#, legend = "db_raw_SIZE_MAX")#, hatch_weight = 5, legend_label="Sunrise")

    line3_tbl3_daily.line( x=COLUMN_DATE, y = COLUMN_5 , color=("blue"), source=df_daily_30_day_tbl_3, legend_label = ("DAILY " + COLUMN_5))#, legend = ["db_raw_SIZE_AVG","db_raw_SIZE_MAX"])#, hatch_weight = 5, legend_label="Sunrise")

    line3_tbl3_daily.legend.location = 'bottom_left'


    #######################################
    # Visualize Entire Data
    #######################################

    vbar_tbl3_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_3[COLUMN_DATE], #INTERVAL_START, 
                                       y1 = df_hourly_full_tbl_3[COLUMN_5], #LIST_RAW_SIZE_AVG, 
                                       y2 = df_hourly_full_tbl_3[COLUMN_6], #LIST_RAW_SIZE_MAX, 
                                       ))


    vbar_tbl3_tot_col1 = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

    vbar_tbl3_tot_col1.title.text = (HOURLY_TBL)

    vbar_tbl3_tot_col1.title.align = "center"

    vbar_tbl3_tot_col1.title.text_color = "yellow"

    vbar_tbl3_tot_col1.title.text_font_size = "15px"

    vbar_tbl3_tot_col1.title.background_fill_color = "darkblue"

    vbar_tbl3_tot_col1.vbar(x = 'x', top = 'y1', color= "blue",  width = 3, source=vbar_tbl3_source, legend_label = COLUMN_5)

    vbar_tbl3_tot_col1.legend.location = 'bottom_left'

    varea_tbl3_stack_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_3[COLUMN_DATE], 
                                       y1 = df_hourly_full_tbl_3[COLUMN_5],
                                       y2 = df_hourly_full_tbl_3[COLUMN_6],
                                       ))

    vbar_tbl3_tot_col2 = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

    vbar_tbl3_tot_col2.title.text = (HOURLY_TBL)

    vbar_tbl3_tot_col2.title.align = "center"

    vbar_tbl3_tot_col2.title.text_color = "yellow"

    vbar_tbl3_tot_col2.title.text_font_size = "15px"

    vbar_tbl3_tot_col2.title.background_fill_color = "darkblue"

    vbar_tbl3_tot_col2.vbar(x = 'x', top = 'y2', color= "red",  width = 3, source=varea_tbl3_stack_source, legend_label = COLUMN_6)



    ###############################################################################
    #   #######   #     ####    #      ######    #
    #      #     #  #   #   #   #      #       # #
    #      #    ######  ####    #      ###    ######
    #      #    #    #  #   #   #      #         #
    #      #    #    #  ####    #####  ######  ####
    ###############################################################################


    #######################################
    # Visualize Hourly Past  5 Day Data
    #######################################

    line4_tbl4_hourly_7_day = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

    line4_tbl4_hourly_7_day.title.text = (str(N_hourly_days) + " Day " +  HOURLY_TBL)

    line4_tbl4_hourly_7_day.title.align = "center"

    line4_tbl4_hourly_7_day.title.text_color = "white"

    line4_tbl4_hourly_7_day.title.text_font_size = "15px"

    line4_tbl4_hourly_7_day.title.background_fill_color = "darkblue"##aaaaee"

    line4_tbl4_hourly_7_day.line( x=COLUMN_DATE, y = COLUMN_8 , color=("red"),  source=df_hourly_7_day_tbl_4, legend_label = ('DAILY ' + COLUMN_8))

    line4_tbl4_hourly_7_day.line( x=COLUMN_DATE, y = COLUMN_7 , color=("blue"), source=df_hourly_7_day_tbl_4, legend_label = ("DAILY"  + COLUMN_7))

    line4_tbl4_hourly_7_day.legend.location = 'bottom_left'


    #######################################
    # Visualized
    #######################################

    #######################################
    # Visualize Daily Data
    #######################################


    line4_tbl4_daily = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

    line4_tbl4_daily.title.text = ("Past Month " + DAILY_TBL)

    line4_tbl4_daily.title.align = "center"

    line4_tbl4_daily.title.text_color = "white"

    line4_tbl4_daily.title.text_font_size = "15px"

    line4_tbl4_daily.title.background_fill_color = "darkblue"##aaaaee"

    line4_tbl4_daily.line( x=COLUMN_DATE, y =   COLUMN_8 , color=("red"),  source=df_daily_30_day_tbl_4, legend_label = ('DAILY ' + COLUMN_8))#, legend = "db_tbl_4_SIZE_MAX")#, hatch_weight = 5, legend_label="Sunrise")

    line4_tbl4_daily.line( x=COLUMN_DATE, y = COLUMN_7 , color=("blue"), source=df_daily_30_day_tbl_4, legend_label = ("DAILY " + COLUMN_7))#, legend = ["db_tbl_4_SIZE_AVG","db_tbl_4_SIZE_MAX"])#, hatch_weight = 5, legend_label="Sunrise")

    line4_tbl4_daily.legend.location = 'bottom_left'


    #######################################
    # Visualize Entire Data
    #######################################

    vbar_tbl4_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_3[COLUMN_DATE], #INTERVAL_START, 
                                       y1 = df_hourly_full_tbl_4[COLUMN_7], #LIST_RAW_SIZE_AVG, 
                                       y2 = df_hourly_full_tbl_4[COLUMN_8])) #, #LIST_RAW_SIZE_MAX, 
                                       #label = [COLUMN_7, COLUMN_8]))


    vbar_tbl4_tot_col1 = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

    vbar_tbl4_tot_col1.title.text = (HOURLY_TBL)

    vbar_tbl4_tot_col1.title.align = "center"

    vbar_tbl4_tot_col1.title.text_color = "yellow"

    vbar_tbl4_tot_col1.title.text_font_size = "15px"

    vbar_tbl4_tot_col1.title.background_fill_color = "darkblue"

    vbar_tbl4_tot_col1.vbar(x = 'x', top = 'y1', color= "blue",  width = 3, source=vbar_tbl4_source, legend_label = COLUMN_7)

    vbar_tbl4_tot_col1.legend.location = 'bottom_left'


    varea_tbl4_stack_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_4[COLUMN_DATE], #INTERVAL_START, 
                                       y1 = df_hourly_full_tbl_4[COLUMN_7], #LIST_RAW_SIZE_AVG, 
                                       y2 = df_hourly_full_tbl_4[COLUMN_8], #LIST_RAW_SIZE_MAX, 
                                       ))

    vbar_tbl4_tot_col2 = figure(plot_width=plotWidth, plot_height=plotHeight,  x_axis_type="datetime")

    vbar_tbl4_tot_col2.title.text = (HOURLY_TBL)

    vbar_tbl4_tot_col2.title.align = "center"

    vbar_tbl4_tot_col2.title.text_color = "yellow"

    vbar_tbl4_tot_col2.title.text_font_size = "15px"

    vbar_tbl4_tot_col2.title.background_fill_color = "darkblue"

    vbar_tbl4_tot_col2.vbar(x = 'x', top = 'y2', color= "red",  width = 3, source=varea_tbl4_stack_source, legend_label = COLUMN_8)

    #MEM_OBJECT_GRIDPLOT = gridplot([[vbar_tbl1_tot_col1, vbar_tbl1_tot_col2, line1_tbl1_daily, line1_tbl1_hourly_7_day], [vbar_tbl2_tot_col1, vbar_tbl2_tot_col2, line2_tbl2_daily, line2_tbl2_hourly_7_day]], toolbar_location='right')
    MEM_OBJECT_GRIDPLOT = gridplot([[vbar_tbl1_tot_col1, 
        vbar_tbl1_tot_col2, 
        line1_tbl1_daily, 
        line1_tbl1_hourly_7_day], 
        [vbar_tbl2_tot_col1, 
        vbar_tbl2_tot_col2, 
        line2_tbl2_daily,
        line2_tbl2_hourly_7_day],
        [vbar_tbl3_tot_col1,
        vbar_tbl3_tot_col2,
        line3_tbl3_daily,
        line3_tbl3_hourly_7_day],
        [vbar_tbl4_tot_col1,
        vbar_tbl4_tot_col2,
        line4_tbl4_daily,
        line4_tbl4_hourly_7_day]], toolbar_location='right')

    show(MEM_OBJECT_GRIDPLOT)
