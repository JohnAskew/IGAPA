#! python3
#------------------------------------#
# This section will install python 
# modules needed to run this script
#------------------------------------#
import os, sys

try:

    from statistics import mean

except:

    os.system('pip install statistics')

    from statistics import mean

try:

    import numpy as np

    from numpy.polynomial import Polynomial

except:

    os.system('pip install numpy')

    import numpy as np

    from numpy.polynomial import Polynomial

try:

    import bokeh

    from bokeh.plotting import figure, output_file, show

    from bokeh.layouts import column, gridplot

    from bokeh.models import ColumnDataSource, Legend, LabelSet, Label, LegendItem, Div, HoverTool

except:

    os.system('pip install bokeh')

    from bokeh.plotting import figure, output_file, show

    from bokeh.layouts  import column, gridplot

    from bokeh.models import ColumnDataSource, Legend, LabelSet, Label, LegendItem, Div

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

    sys.exit(13)

try:

    import logging

except:

    os.system('pip install logging')

    import logging

try:

    from datetime import datetime as dt

except:

    os.system('pip install datetime')

    from datetime import datetime as dt

try:

    import time

except:

    os.system("pip install time")

    import time

now = dt.today().strftime('%Y-%m-%d-%H:%M:%S')

logging_filename = "igapa_master.py.log"

logging.basicConfig(filename = logging_filename, level=logging.INFO, filemode = 'a', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')
  
#######################################
# FUNCTTIONS BEFORE MAIN CODE
#######################################

#-------------------------------------#
def best_fit(xs, ys):
#-------------------------------------#
    m = (  ( (mean(xs) * mean(ys)) - mean(xs * ys) )  /
           ( (mean(xs) * mean(xs)) - mean(xs * xs))
        )
    b = mean(ys) - m * mean(xs)
    return m, b

#-------------------------------------#
def date_to_seconds(timestamp):
#-------------------------------------#

    d = dt.strptime(str(timestamp), "%Y-%m-%d %H:%M:%S")

    secs = time.mktime(d.timetuple())

    #print("secs: " + str(secs))
    
    return int(secs)

#-------------------------------------#
def my_logger(orig_func):
#-------------------------------------#
    import logging

    mylogr = logging.getLogger(orig_func.__name__)

    mylogr.setLevel(logging.INFO)

    mylogr_fh = logging.FileHandler('{}.log'.format(orig_func.__name__))

    mylogr_fmt = ('%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

    formatter = logging.Formatter(mylogr_fmt)

    mylogr_fh.setFormatter(formatter)

    mylogr.addHandler(mylogr_fh)

    def wrapper(*args, **kwargs):

        mylogr.info(

            'Function {} Ran with arg: {} and kwargs {}'.format(orig_func.__name__, args, kwargs))

        return orig_func(*args, **kwargs)

    return wrapper

#-------------------------------------#
def log_and_print_debug(msg):
#-------------------------------------#

    logging.debug(msg)

    print(msg)


#-------------------------------------#
#@my_logger
def log_and_print_info(msg):
#-------------------------------------#

    logging.info(msg)

    print(msg)

#-------------------------------------#
def log_and_print_warning(msg):
#-------------------------------------#

    logging.warning(msg)

    print(msg)

#-------------------------------------#
def log_and_print_error(msg):
#-------------------------------------#

    logging.error(msg)

    print(msg)

#######################################
# Set up processinging logic
#######################################

save_dir = os.getcwd()

if __name__ == "__main__":

    log_and_print_info("#--------------------------------------#")

    log_and_print_info("# Entering " +  os.path.basename(__file__))

    log_and_print_info("#--------------------------------------#")

    if len(sys.argv) > 1:

        in_ticket = sys.argv[1]

    else:
       
        in_ticket = 28727

    if len(sys.argv) > 2:

        class_chart = 'DB_SIZE'

        config_in   = sys.argv[2]

        log_and_print_info("# " + os.path.basename(__file__) + " received these arguments: in_ticket " + str(in_ticket) + " config_in: " + config_in)

    else:

        class_chart = 'DB_SIZE'

        config_in = 'config_reports.ini'

    log_and_print_info("# " + os.path.basename(__file__) + " received these arguments: in_ticket " + str(in_ticket) + " config_in: " + config_in)

else:
   
    in_ticket = sys.argv[1]

    config_in = sys.argv[2]

    log_and_print_info("#------------------------------------#")
  
    log_and_print_info("# Entering " +  os.path.basename(__file__))

    log_and_print_info("#------------------------------------#")

    log_and_print_info("# received these arguments: in_ticket " + str(in_ticket) + " config_in: " + config_in)


in_dir = str("EXA-" + str(in_ticket))

if not os.path.exists(in_dir):

    log_and_print_error("#######################################")

    log_and_print_error("# " + os.path.basename(__file__) + " FATAL ERROR " )

    log_and_print_error("#  " + os.path.basename(__file__) + " Needed path " + in_dir)

    log_and_print_error("# is NOT available for " + os.path.basename(__file__))

    log_and_print_error("# --> was directory " + in_dir + " created?")

    log_and_print_error("# --> it is created but not a directory?")

    log_and_print_error("# --> Is it a directory and read-only?")

    log_and_print_error("# *** See subr_jira_download.py for creating needed directory")

    log_and_print_error("#")

    log_and_print_error("#  " + os.path.basename(__file__) + " Aborting with no action taken.")

    log_and_print_error("#######################################")

    sys.exit(13)


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

try:

    b = ParseConfig(class_chart, config_in)

except Exception as e:

    log_and_print_error("#######################################")

    log_and_print_error("FATAL: " + os.path.basename(__file__))

    log_and_print_error("# " + os.path.basename(__file__) + " Unable to reference ParseConfig using:")

    log_and_print_error("# b = ParseConfig(class_chart)")

    log_and_print_error("# Does pgm tools_parse_config.py exist in " + os.getcwd(),"?" )

    log_and_print_error("# " + os.path.basename(__file__) + " Aborting with no action taken.")

    logging.error(e, exc_info = True)

    print(e)

    log_and_print_error("#######################################")

    sys.exit(13)

config_sections = b.read_config_sections(save_dir)

if len(config_sections) == 0:

    log_and_print_error("FATAL: " + os.path.basename(__file__))

    log_and_print_error("# " + os.path.basename(__file__) + " unable to reference ParseConfig using:")

    log_and_print_error("# config_sections = b.read_config_sections()")

    log_and_print_error("# Does pgm tools_parse_config.py exist in " + os.getcwd(),"?" )

    log_and_print_error("# " + os.path.basename(__file__) + " Aborting with no action taken.")

    sys.exit(13)

for item in config_sections:

    log_and_print_info("# " + os.path.basename(__file__) + " received this section from tool_parse_config: " + item)


legend_font_size, legend_location, plotWidth, plotHeight, smallplotWidth, smallplotHeight, largeplotWidth, largeplotHeight = b.read_config_admin_layout(save_dir, 'config_admin.ini')

plotWidth       = int(plotWidth)

plotHeight      = int(plotHeight)

smallplotWidth  = int(smallplotWidth)

smallplotHeight = int(smallplotHeight)

largeplotWidth  = int(largeplotWidth)

largeplotHeight = int(largeplotHeight)


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

    process_section = ParseConfig(config_section, config_in)

    CONFIG_HOURLY_TBL,CONFIG_DAILY_TBL,CONFIG_ROW1_COL_X_AXIS,CONFIG_ROW1_COL_Y_AXIS_1,CONFIG_ROW1_COL_Y_AXIS_2,CONFIG_ROW2_COL_X_AXIS,CONFIG_ROW2_COL_Y_AXIS_1,CONFIG_ROW2_COL_Y_AXIS_2,CONFIG_ROW3_COL_X_AXIS,CONFIG_ROW3_COL_Y_AXIS_1,CONFIG_ROW3_COL_Y_AXIS_2,CONFIG_ROW4_COL_X_AXIS,CONFIG_ROW4_COL_Y_AXIS_1,CONFIG_ROW4_COL_Y_AXIS_2 = process_section.run(save_dir)

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

    log_and_print_info("# " + os.path.basename(__file__) + " Processing\tConfig section:\t " + config_section)

    log_and_print_info("# " + os.path.basename(__file__) + " Processing\tHOURLY_TBL:\t " + HOURLY_TBL)

    log_and_print_info("# " + os.path.basename(__file__) + " Processing\tDAILY_TBL:\t " +  DAILY_TBL)

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

        log_and_print_error("# FATAL ERROR in " + os.path.basename(__file__))

        log_and_print_error("# ---> File is NOT FOUND!")

        log_and_print_error("# " + os.path.basename(__file__) + " config.ini section:\t " + config_section)

        log_and_print_error("# which specified:\t " + HOURLY_TBL)

        log_and_print_error("# Needs CSV file:\t " + str(HOURLY_TBL + '.csv'))

        log_and_print_error("# in directory:\t\t " + in_dir + ".")

        log_and_print_error("#  " + os.path.basename(__file__) + " Aborting with no action taken.")

        logging.error(e, exc_info = True)

        print(e)

        sys.exit(13)

    try:

        df_hourly_full_tbl_1 = df_hourly_full_tbl_1[COLS_TBL1]

        df_hourly_full_tbl_1_extracted = df_hourly_full_tbl_1.shape[0]


    except Exception as e:

        log_and_print_error("# " + os.path.basename(__file__) + " unable to read " + HOURLY_TBL + " skipping!")

        log_and_print_error("# " + os.path.basename(__file__) + " Aborting with no action taken.")

        logging.error(e, exc_info = True)

        print(e)

        sys.exit(13)

    #######################################
    # Extract TBL1 Daily Records
    #######################################

    try:

        df_daily_full_tbl_1 = pd.read_csv(DAILY_TBL + '.csv', usecols = COLS_TBL1)

    except Exception as e:

        log_and_print_error("# FATAL ERROR in " + os.path.basename(__file__))

        log_and_print_error("# ---> File is NOT FOUND!")

        for item in config_sections:

            log_and_print_error("# " + os.path.basename(__file__) + " config.ini section has this item:\t " + item)

        log_and_print_error("# which specified:\t " + DAILY_TBL)

        log_and_print_error("# Needs CSV file:\t " + str(DAILY_TBL + '.csv'))

        log_and_print_error("# in directory:\t\t " + in_dir + ".")

        logging.error(e, exc_info = True)

        print(e)

        log_and_print_error("#-------------------------------------#")

        log_and_print_error("# " + os.path.basename(__file__) + " Aborting with no action taken.")

        log_and_print_error("#-------------------------------------#")
        
        sys.exit(13)


    try:

        df_daily_full_tbl_1 = df_daily_full_tbl_1[COLS_TBL1]

        df_daily_full_tbl_1_extracted =  df_daily_full_tbl_1.shape[0]

    except Exception as e:

        log_and_print_error("# " + os.path.basename(__file__) + " unable to read " + DAILY_TBL + " skipping!")

        logging.error(e, exc_info = True)

        print(e)

        log_and_print_error("#-------------------------------------#")

        log_and_print_error("# " + os.path.basename(__file__) + " Aborting with no action taken.")

        log_and_print_error("#-------------------------------------#")



        sys.exit(13)

    #######################################
    # Read the max df_hourly_full_tbl_1 timestamp
    #######################################

    try:

        df_hourly_full_tbl_1['INTERVAL_START'] = pd.to_datetime(df_hourly_full_tbl_1['INTERVAL_START'])

    except Exception as e:

        log_and_print_error("#Error in " +  os.path.basename(__file__))

        log_and_print_error("# "+ os.path.basename(__file__) + " Unable to parse INTERVAL_START")

        log_and_print_error("# " + os.path.basename(__file__) + " when trying to set datetime using pd.to_datetime." )

        logging.error(e, exc_info = True)

        print(e)

        log_and_print_error("#-------------------------------------#")

        log_and_print_error("# " + os.path.basename(__file__) + " Aborting with no action taken.")

        log_and_print_error("#-------------------------------------#")

        sys.exit(13)

    date_max_hourly = df_hourly_full_tbl_1[COLUMN_DATE].max()

    print("# INFO:", os.path.basename(__file__), " read", HOURLY_TBL, "date_max_hourly:", date_max_hourly)

    #######################################
    # Read the max df_daily_full_tbl_1 timestamp
    #######################################
    try:

        df_daily_full_tbl_1[COLUMN_DATE] = pd.to_datetime(df_daily_full_tbl_1[COLUMN_DATE])

    except Exception as e:

        log_and_print_error("#Error in " +  os.path.basename(__file__))

        log_and_print_error("# "+ os.path.basename(__file__) + " Unable to parse COLUMN_DATE on df_daily_full_tbl_1")

        log_and_print_error("# " + os.path.basename(__file__) + " when trying to set datetime using pd.to_datetime." )

        logging.error(e, exc_info = True)

        print(e)

        log_and_print_error("#-------------------------------------#")

        log_and_print_error("# " + os.path.basename(__file__) + " Aborting with no action taken.")

        log_and_print_error("#-------------------------------------#")

        sys.exit(13)

    date_max_daily = df_daily_full_tbl_1[COLUMN_DATE].max()

    log_and_print_info("# INFO: " + os.path.basename(__file__) + " read " + DAILY_TBL + " date_max_daily: " + str(date_max_daily))

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

        log_and_print_error("Unable to READ " + HOURLY_TBL + "...Aborting with no action taken.")

        logging.error(e, exc_info = True)

        print(e)

        sys.exit(13)

    #######################################
    # Extract TBL2 Daily Records
    #######################################

    try:

        df_daily_full_tbl_2 = pd.read_csv(DAILY_TBL + '.csv', usecols = COLS_TBL2)#  export_params={"columns": COLS_TBL2}) #["INTERVAL_START",COLUMN_1, COLUMN_2]})

        df_daily_full_tbl_2_extracted =  df_daily_full_tbl_2.shape[0]


    except Exception as e:

        log_and_print_error("Unable to READ " + DAILY_TBL + " ...Aborting with no action taken.")

        logging.error(3)

        print(e)

        sys.exit(13)

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

        log_and_print_error("Unable to READ " + HOURLY_TBL + " ...Aborting with no action taken.")

        logging.error(e, exc_info = True)

        print(e)

        sys.exit(13)

    #######################################
    # Extract TBL3 Daily Records
    #######################################

    try:

        df_daily_full_tbl_3 = pd.read_csv(DAILY_TBL + '.csv', usecols = COLS_TBL3)#  export_params={"columns": COLS_TBL3}) #["INTERVAL_START",COLUMN_5, COLUMN_6]})

        df_daily_full_tbl_3_extracted = df_daily_full_tbl_3.shape[0]


    except Exception as e:

        log_and_print_error("Unable to READ " + DAILY_TBL + " ...Aborting with no action taken.")

        logging.error(e, exc_info = True)

        print(e)

        sys.exit(13)

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

        log_and_print_error("Unable to READ " + HOURLY_TBL + " ...Aborting with no action taken.")

        logging.error(e, exc_info = True)

        print(e)

        sys.exit(13)

    #######################################
    # Extract TBL4 Daily Records
    #######################################

    try:

        df_daily_full_tbl_4 = pd.read_csv(DAILY_TBL + '.csv', usecols = COLS_TBL4)#  export_params={"columns": COLS_TBL4}) #["INTERVAL_START",COLUMN_5, COLUMN_6]})

        df_daily_full_tbl_4_extracted = df_daily_full_tbl_4.shape[0]


    except Exception as e:

        log_and_print_error("Unable to READ " + DAILY_TBL + " ...Aborting with no action taken.")

        logging.error(e, exc_info = True)

        print(e)

        sys.exit(13)

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

#######################################
# DATA CLEAN UP  - Charts Row 1 Set NULLS To 0.
#######################################

    df_hourly_full_tbl_1[COLUMN_1].fillna(0, inplace = True)

    df_hourly_full_tbl_1[COLUMN_2].fillna(0, inplace = True)

    df_hourly_7_day_tbl_1[COLUMN_1].fillna(0, inplace = True)

    df_hourly_7_day_tbl_1[COLUMN_2].fillna(0, inplace = True)

    df_daily_full_tbl_1[COLUMN_1].fillna(0, inplace = True)

    df_daily_full_tbl_1[COLUMN_2].fillna(0, inplace = True)

    df_daily_30_day_tbl_1[COLUMN_1].fillna(0, inplace = True)

    df_daily_30_day_tbl_1[COLUMN_2].fillna(0, inplace = True)

#######################################
# DATA CLEAN UP  - Charts Row 2 Set NULLS To 0.
#######################################

    df_hourly_full_tbl_2[COLUMN_3].fillna(0, inplace = True)

    df_hourly_full_tbl_2[COLUMN_4].fillna(0, inplace = True)

    df_hourly_7_day_tbl_2[COLUMN_3].fillna(0, inplace = True)

    df_hourly_7_day_tbl_2[COLUMN_4].fillna(0, inplace = True)

    df_daily_full_tbl_2[COLUMN_3].fillna(0, inplace = True)

    df_daily_full_tbl_2[COLUMN_4].fillna(0, inplace = True)

    df_daily_30_day_tbl_2[COLUMN_3].fillna(0, inplace = True)

    df_daily_30_day_tbl_2[COLUMN_4].fillna(0, inplace = True)

#######################################
# DATA CLEAN UP  - Charts Row 3 Set NULLS To 0.
#######################################

    df_hourly_full_tbl_3[COLUMN_5].fillna(0, inplace = True)

    df_hourly_full_tbl_3[COLUMN_6].fillna(0, inplace = True)

    df_hourly_7_day_tbl_3[COLUMN_5].fillna(0, inplace = True)

    df_hourly_7_day_tbl_3[COLUMN_6].fillna(0, inplace = True)

    df_daily_full_tbl_3[COLUMN_5].fillna(0, inplace = True)

    df_daily_full_tbl_3[COLUMN_6].fillna(0, inplace = True)

    df_daily_30_day_tbl_3[COLUMN_5].fillna(0, inplace = True)

    df_daily_30_day_tbl_3[COLUMN_6].fillna(0, inplace = True)

#######################################
# DATA CLEAN UP  - Charts Row 4 Set NULLS To 0.
#######################################

    df_hourly_full_tbl_4[COLUMN_7].fillna(0, inplace = True)

    df_hourly_full_tbl_4[COLUMN_8].fillna(0, inplace = True)

    df_hourly_7_day_tbl_4[COLUMN_7].fillna(0, inplace = True)

    df_hourly_7_day_tbl_4[COLUMN_8].fillna(0, inplace = True)

    df_daily_full_tbl_4[COLUMN_7].fillna(0, inplace = True)

    df_daily_full_tbl_4[COLUMN_8].fillna(0, inplace = True)

    df_daily_30_day_tbl_4[COLUMN_7].fillna(0, inplace = True)

    df_daily_30_day_tbl_4[COLUMN_8].fillna(0, inplace = True)



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

    line1_tbl1_hourly_7_day = figure(plot_width=largeplotWidth, plot_height=largeplotHeight,  x_axis_type="datetime")

    line1_tbl1_hourly_7_day.title.text = (str(N_hourly_days) + " Day " +  HOURLY_TBL)

    line1_tbl1_hourly_7_day.title.align = "center"

    line1_tbl1_hourly_7_day.title.text_color = "white"

    line1_tbl1_hourly_7_day.title.text_font_size = "15px"

    line1_tbl1_hourly_7_day.title.background_fill_color = "darkblue"

    line1_tbl1_hourly_7_day.diamond( x=COLUMN_DATE, y = COLUMN_2 , line_width = 3, alpha = 0.5, color=("red"),  source=df_hourly_7_day_tbl_1, legend_label = ('HOURLY ' + COLUMN_2) )

    line1_tbl1_hourly_7_day.circle( x=COLUMN_DATE, y = COLUMN_1 , line_width = 2, alpha = 0.5, color=("blue"), source=df_hourly_7_day_tbl_1, legend_label = ("HOURLY"  + COLUMN_1))

    line1_tbl1_hourly_7_day.legend.location = legend_location #legend_location

    line1_tbl1_hourly_7_day.legend.label_text_font_size = legend_font_size

#######################################
# Calculate the BEST_FIT line against _MAX
#######################################

    int_list = []

    for mydate in df_hourly_7_day_tbl_1[COLUMN_DATE]:

        int_list.append(date_to_seconds(mydate))

        int_list = sorted(int_list)

    xs = np.array(int_list, dtype = float)

    ys = np.array(df_hourly_7_day_tbl_1[COLUMN_2], dtype = float)

    m, b = best_fit(xs, ys)

    regression_line = [ (m * x) + b  for x in xs]

    line1_tbl1_hourly_7_day.line(df_hourly_7_day_tbl_1[COLUMN_DATE], regression_line, color = 'yellow', alpha = 0.3, line_width = 6, legend_label = 'BEST_FIT of ' + COLUMN_2)

#######################################
# Calculate the OUTLIERS
#######################################

    threshold = 3

    my_mean = np.mean(df_hourly_7_day_tbl_1[COLUMN_2])

    my_std  = np.std(df_hourly_7_day_tbl_1[COLUMN_2])

    for count, i in enumerate(df_hourly_7_day_tbl_1[COLUMN_2]):

        if ( ( i - my_mean ) / my_std ) > threshold:

            line1_tbl1_hourly_7_day.circle( x=df_hourly_7_day_tbl_1.iloc[count:count+1,0], y = df_hourly_7_day_tbl_1.iloc[count:count+1,2] , line_width = 7, alpha = 0.5, color=("green"), legend_label = COLUMN_2 + " Outlier")

   

    #######################################
    # Visualized
    #######################################

    #######################################
    # Visualize Daily Data
    #######################################


    line1_tbl1_daily = figure(plot_width=largeplotWidth, plot_height=largeplotHeight,  x_axis_type="datetime")

    line1_tbl1_daily.title.text = ("Past Month " + DAILY_TBL)

    line1_tbl1_daily.title.align = "center"

    line1_tbl1_daily.title.text_color = "white"

    line1_tbl1_daily.title.text_font_size = "15px"

    line1_tbl1_daily.title.background_fill_color = "darkblue"##aaaaee"

    line1_tbl1_daily.line( x=COLUMN_DATE, y =   COLUMN_2 , alpha = 0.5, color=("red"),  source=df_daily_30_day_tbl_1, legend_label = ('DAILY ' + COLUMN_2))#, legend = "db_raw_SIZE_MAX")#, hatch_weight = 5, legend_label="Sunrise")

    line1_tbl1_daily.line( x=COLUMN_DATE, y = COLUMN_1 , alpha = 0.5, color=("blue"), source=df_daily_30_day_tbl_1, legend_label = ("DAILY " + COLUMN_1))#, legend = ["db_raw_SIZE_AVG","db_raw_SIZE_MAX"])#, hatch_weight = 5, legend_label="Sunrise")

    line1_tbl1_daily.legend.location = legend_location

    line1_tbl1_daily.legend.label_text_font_size = legend_font_size


#######################################
# Calculate the BEST_FIT line against _MAX
# Left in for purposes of using at a later date
# so do not delete out the this commented section
# of code.
#######################################

    # int_list = []

    # for mydate in df_daily_30_day_tbl_1[COLUMN_DATE]:

    #     int_list.append(date_to_seconds(mydate))

    #     int_list = sorted(int_list)

    # xs = np.array(int_list, dtype = float)

    # ys = np.array(df_daily_30_day_tbl_1[COLUMN_2], dtype = float)

    # m, b = best_fit(xs, ys)

    # regression_line = [ (m * x) + b  for x in xs]

    # line1_tbl1_daily.line(df_daily_30_day_tbl_1[COLUMN_DATE], regression_line, color = 'yellow', alpha = 0.3, line_width = 6, legend_label = "BEST_FIT of " + COLUMN_2)

#######################################
# Calculate the OUTLIERS
#######################################

    # threshold = 3

    # my_mean = np.mean(df_daily_30_day_tbl_1[COLUMN_2])

    # my_std  = np.std(df_daily_30_day_tbl_1[COLUMN_2])

    # for count, i in enumerate(df_daily_30_day_tbl_1[COLUMN_2]):

    #     if ( ( i - my_mean ) / my_std ) > threshold:
            
    #         print("Outlier :" + str(i) + " count: " + str(count))
    #         line1_tbl1_daily.circle( x=df_daily_30_day_tbl_1.iloc[count:count+1,0], y = df_daily_30_day_tbl_1.iloc[count:count+1,2] , line_width = 7, alpha = 0.5, color=("green"))




    #######################################
    # Visualize Entire Data
    #######################################

    vbar_tbl1_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_1[COLUMN_DATE], #INTERVAL_START, 
                                       y1 = df_hourly_full_tbl_1[COLUMN_1], #LIST_RAW_SIZE_AVG, 
                                       y2 = df_hourly_full_tbl_1[COLUMN_2], #LIST_RAW_SIZE_MAX, 
                                       ))


    vbar_tbl1_tot_col1 = figure(plot_width=smallplotWidth, plot_height=smallplotHeight,  x_axis_type="datetime")

    vbar_tbl1_tot_col1.title.text = (HOURLY_TBL)

    vbar_tbl1_tot_col1.title.align = "center"

    vbar_tbl1_tot_col1.title.text_color = "yellow"

    vbar_tbl1_tot_col1.title.text_font_size = "15px"

    vbar_tbl1_tot_col1.title.background_fill_color = "darkblue"

    vbar_tbl1_tot_col1.vbar(x = 'x', top = 'y1', color= "blue",  width = 3, source=vbar_tbl1_source, legend_label = COLUMN_1)

    vbar_tbl1_tot_col1.legend.location = legend_location

    vbar_tbl1_tot_col1.legend.label_text_font_size = legend_font_size

    varea_tbl1_stack_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_1[COLUMN_DATE], 
                                       y1 = df_hourly_full_tbl_1[COLUMN_1],
                                       y2 = df_hourly_full_tbl_1[COLUMN_2],
                                       ))

    vbar_tbl1_tot_col2 = figure(plot_width=smallplotWidth, plot_height=smallplotHeight,  x_axis_type="datetime")

    vbar_tbl1_tot_col2.title.text = (HOURLY_TBL)

    vbar_tbl1_tot_col2.title.align = "center"

    vbar_tbl1_tot_col2.title.text_color = "yellow"

    vbar_tbl1_tot_col2.title.text_font_size = "15px"

    vbar_tbl1_tot_col2.title.background_fill_color = "darkblue"

    vbar_tbl1_tot_col2.vbar(x = 'x', top = 'y2', color= "red",  width = 3, source=varea_tbl1_stack_source, legend_label = COLUMN_2)

    vbar_tbl1_tot_col2.legend.location = legend_location

    vbar_tbl1_tot_col2.legend.label_text_font_size = legend_font_size

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

    line2_tbl2_hourly_7_day = figure(plot_width=largeplotWidth, plot_height=largeplotHeight,  x_axis_type="datetime")

    line2_tbl2_hourly_7_day.title.text = (str(N_hourly_days) + " Day " +  HOURLY_TBL)

    line2_tbl2_hourly_7_day.title.align = "center"

    line2_tbl2_hourly_7_day.title.text_color = "white"

    line2_tbl2_hourly_7_day.title.text_font_size = "15px"

    line2_tbl2_hourly_7_day.title.background_fill_color = "darkblue"##aaaaee"

    line2_tbl2_hourly_7_day.diamond( x=COLUMN_DATE, y = COLUMN_4 , line_width = 3, alpha = 0.5, color=("red"),  source=df_hourly_7_day_tbl_2, legend_label = ('HOURLY ' + COLUMN_4) )

    line2_tbl2_hourly_7_day.circle( x=COLUMN_DATE, y = COLUMN_3 , line_width = 2, alpha = 0.5, color=("blue"), source=df_hourly_7_day_tbl_2, legend_label = ("HOURLY"  + COLUMN_3))
    
    line2_tbl2_hourly_7_day.legend.location = legend_location

    line2_tbl2_hourly_7_day.legend.label_text_font_size = legend_font_size

#######################################
# Calculate the BEST_FIT line against _MAX
#######################################

    int_list = []

    for mydate in df_hourly_7_day_tbl_2[COLUMN_DATE]:

        int_list.append(date_to_seconds(mydate))

        int_list = sorted(int_list)

    xs = np.array(int_list, dtype = float)

    ys = np.array(df_hourly_7_day_tbl_2[COLUMN_4], dtype = float)

    m, b = best_fit(xs, ys)

    regression_line = [ (m * x) + b  for x in xs]

    line2_tbl2_hourly_7_day.line(df_hourly_7_day_tbl_2[COLUMN_DATE], regression_line, color = 'yellow', alpha = 0.3, line_width = 6, legend_label = 'BEST_FIT of ' + COLUMN_4)

#######################################
# Calculate the OUTLIERS
#######################################

    threshold = 3

    my_mean = np.mean(df_hourly_7_day_tbl_2[COLUMN_4])

    my_std  = np.std(df_hourly_7_day_tbl_2[COLUMN_4])

    for count, i in enumerate(df_hourly_7_day_tbl_2[COLUMN_4]):

        if ( ( i - my_mean ) / my_std ) > threshold:

            line2_tbl2_hourly_7_day.circle( x=df_hourly_7_day_tbl_2.iloc[count:count+1,0], y = df_hourly_7_day_tbl_2.iloc[count:count+1,2] , line_width = 7, alpha = 0.5, color=("green"), legend_label = COLUMN_4 + " Outlier")

   


    #######################################
    # Visualized
    #######################################

    #######################################
    # Visualize Daily Data
    #######################################


    line2_tbl2_daily = figure(plot_width=largeplotWidth, plot_height=largeplotHeight,  x_axis_type="datetime")

    line2_tbl2_daily.title.text = ("Past Month " + DAILY_TBL)

    line2_tbl2_daily.title.align = "center"

    line2_tbl2_daily.title.text_color = "white"

    line2_tbl2_daily.title.text_font_size = "15px"

    line2_tbl2_daily.title.background_fill_color = "darkblue"##aaaaee"

    line2_tbl2_daily.line( x=COLUMN_DATE, y =   COLUMN_4 , alpha = 0.5, color=("red"),  source=df_daily_30_day_tbl_2, legend_label = ('DAILY ' + COLUMN_4))#, legend = "db_tbl_2_SIZE_MAX")#, hatch_weight = 5, legend_label="Sunrise")

    line2_tbl2_daily.line( x=COLUMN_DATE, y = COLUMN_3 , alpha = 0.5, color=("blue"), source=df_daily_30_day_tbl_2, legend_label = ("DAILY " + COLUMN_3))#, legend = ["db_tbl_2_SIZE_AVG","db_tbl_2_SIZE_MAX"])#, hatch_weight = 5, legend_label="Sunrise")

    line2_tbl2_daily.legend.location = legend_location

    line2_tbl2_daily.legend.label_text_font_size = legend_font_size


    #######################################
    # Visualize Entire Data
    #######################################

    vbar_tbl2_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_1[COLUMN_DATE], #INTERVAL_START, 
                                       y1 = df_hourly_full_tbl_2[COLUMN_3], #LIST_RAW_SIZE_AVG, 
                                       y2 = df_hourly_full_tbl_2[COLUMN_4])) #, #LIST_RAW_SIZE_MAX, 
                                       #label = [COLUMN_3, COLUMN_4]))


    vbar_tbl2_tot_col1 = figure(plot_width=smallplotWidth, plot_height=smallplotHeight,  x_axis_type="datetime")

    vbar_tbl2_tot_col1.title.text = (HOURLY_TBL)

    vbar_tbl2_tot_col1.title.align = "center"

    vbar_tbl2_tot_col1.title.text_color = "yellow"

    vbar_tbl2_tot_col1.title.text_font_size = "15px"

    vbar_tbl2_tot_col1.title.background_fill_color = "darkblue"

    vbar_tbl2_tot_col1.vbar(x = 'x', top = 'y1', color= "blue",  width = 3, source=vbar_tbl2_source, legend_label = COLUMN_3)

    vbar_tbl2_tot_col1.legend.location = legend_location

    vbar_tbl2_tot_col1.legend.label_text_font_size = legend_font_size


    varea_tbl2_stack_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_2[COLUMN_DATE], #INTERVAL_START, 
                                       y1 = df_hourly_full_tbl_2[COLUMN_3], #LIST_RAW_SIZE_AVG, 
                                       y2 = df_hourly_full_tbl_2[COLUMN_4], #LIST_RAW_SIZE_MAX, 
                                       ))

    vbar_tbl2_tot_col2 = figure(plot_width=smallplotWidth, plot_height=smallplotHeight,  x_axis_type="datetime")

    vbar_tbl2_tot_col2.title.text = (HOURLY_TBL)

    vbar_tbl2_tot_col2.title.align = "center"

    vbar_tbl2_tot_col2.title.text_color = "yellow"

    vbar_tbl2_tot_col2.title.text_font_size = "15px"

    vbar_tbl2_tot_col2.title.background_fill_color = "darkblue"

    vbar_tbl2_tot_col2.vbar(x = 'x', top = 'y2', color= "red",  width = 3, source=varea_tbl2_stack_source, legend_label = COLUMN_4)

    vbar_tbl2_tot_col2.legend.location = legend_location

    vbar_tbl2_tot_col2.legend.label_text_font_size = legend_font_size


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

    line3_tbl3_hourly_7_day = figure(plot_width=largeplotWidth, plot_height=largeplotHeight,  x_axis_type="datetime")

    line3_tbl3_hourly_7_day.title.text = (str(N_hourly_days) + " Day " +  HOURLY_TBL)

    line3_tbl3_hourly_7_day.title.align = "center"

    line3_tbl3_hourly_7_day.title.text_color = "white"

    line3_tbl3_hourly_7_day.title.text_font_size = "15px"

    line3_tbl3_hourly_7_day.title.background_fill_color = "darkblue"##aaaaee"

    line3_tbl3_hourly_7_day.diamond( x=COLUMN_DATE, y = COLUMN_6 , line_width = 3, alpha = 0.5, color=("red"),  source=df_hourly_7_day_tbl_3, legend_label = ('HOURLY ' + COLUMN_6) )

    line3_tbl3_hourly_7_day.circle( x=COLUMN_DATE, y = COLUMN_5 , line_width = 2, alpha = 0.5, color=("blue"), source=df_hourly_7_day_tbl_3, legend_label = ("HOURLY"  + COLUMN_5))
    
    line3_tbl3_hourly_7_day.legend.location = legend_location

    line3_tbl3_hourly_7_day.legend.label_text_font_size = legend_font_size

#######################################
# Calculate the BEST_FIT line against _MAX
#######################################

    int_list = []

    for mydate in df_hourly_7_day_tbl_3[COLUMN_DATE]:

        int_list.append(date_to_seconds(mydate))

        int_list = sorted(int_list)

    xs = np.array(int_list, dtype = float)

    ys = np.array(df_hourly_7_day_tbl_3[COLUMN_6], dtype = float)

    m, b = best_fit(xs, ys)

    regression_line = [ (m * x) + b  for x in xs]

    line3_tbl3_hourly_7_day.line(df_hourly_7_day_tbl_3[COLUMN_DATE], regression_line, color = 'yellow', alpha = 0.3, line_width = 6, legend_label = 'BEST_FIT of ' + COLUMN_6)

#######################################
# Calculate the OUTLIERS
#######################################

    threshold = 3

    my_mean = np.mean(df_hourly_7_day_tbl_3[COLUMN_6])

    my_std  = np.std(df_hourly_7_day_tbl_3[COLUMN_6])

    for count, i in enumerate(df_hourly_7_day_tbl_3[COLUMN_6]):

        if ( ( i - my_mean ) / my_std ) > threshold:

            line3_tbl3_hourly_7_day.circle( x=df_hourly_7_day_tbl_3.iloc[count:count+1,0], y = df_hourly_7_day_tbl_3.iloc[count:count+1,2] , line_width = 7, alpha = 0.5, color=("green"), legend_label = COLUMN_6 + " Outlier")

   


    #######################################
    # Visualized
    #######################################

    #######################################
    # Visualize Daily Data
    #######################################


    line3_tbl3_daily = figure(plot_width=largeplotWidth, plot_height=largeplotHeight,  x_axis_type="datetime")

    line3_tbl3_daily.title.text = ("Past Month " + DAILY_TBL)

    line3_tbl3_daily.title.align = "center"

    line3_tbl3_daily.title.text_color = "white"

    line3_tbl3_daily.title.text_font_size = "15px"

    line3_tbl3_daily.title.background_fill_color = "darkblue"##aaaaee"

    line3_tbl3_daily.line( x=COLUMN_DATE, y =   COLUMN_6 , alpha = 0.5, color=("red"),  source=df_daily_30_day_tbl_3, legend_label = ('DAILY ' + COLUMN_6))#, legend = "db_raw_SIZE_MAX")#, hatch_weight = 5, legend_label="Sunrise")

    line3_tbl3_daily.line( x=COLUMN_DATE, y = COLUMN_5 , alpha = 0.5, color=("blue"), source=df_daily_30_day_tbl_3, legend_label = ("DAILY " + COLUMN_5))#, legend = ["db_raw_SIZE_AVG","db_raw_SIZE_MAX"])#, hatch_weight = 5, legend_label="Sunrise")

    line3_tbl3_daily.legend.location = legend_location

    line3_tbl3_daily.legend.label_text_font_size = legend_font_size


    #######################################
    # Visualize Entire Data
    #######################################

    vbar_tbl3_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_3[COLUMN_DATE], #INTERVAL_START, 
                                       y1 = df_hourly_full_tbl_3[COLUMN_5], #LIST_RAW_SIZE_AVG, 
                                       y2 = df_hourly_full_tbl_3[COLUMN_6], #LIST_RAW_SIZE_MAX, 
                                       ))


    vbar_tbl3_tot_col1 = figure(plot_width=smallplotWidth, plot_height=smallplotHeight,  x_axis_type="datetime")

    vbar_tbl3_tot_col1.title.text = (HOURLY_TBL)

    vbar_tbl3_tot_col1.title.align = "center"

    vbar_tbl3_tot_col1.title.text_color = "yellow"

    vbar_tbl3_tot_col1.title.text_font_size = "15px"

    vbar_tbl3_tot_col1.title.background_fill_color = "darkblue"

    vbar_tbl3_tot_col1.vbar(x = 'x', top = 'y1', color= "blue",  width = 3, source=vbar_tbl3_source, legend_label = COLUMN_5)

    vbar_tbl3_tot_col1.legend.location = legend_location

    vbar_tbl3_tot_col1.legend.label_text_font_size = legend_font_size

    varea_tbl3_stack_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_3[COLUMN_DATE], 
                                       y1 = df_hourly_full_tbl_3[COLUMN_5],
                                       y2 = df_hourly_full_tbl_3[COLUMN_6],
                                       ))

    vbar_tbl3_tot_col2 = figure(plot_width=smallplotWidth, plot_height=smallplotHeight,  x_axis_type="datetime")

    vbar_tbl3_tot_col2.title.text = (HOURLY_TBL)

    vbar_tbl3_tot_col2.title.align = "center"

    vbar_tbl3_tot_col2.title.text_color = "yellow"

    vbar_tbl3_tot_col2.title.text_font_size = "15px"

    vbar_tbl3_tot_col2.title.background_fill_color = "darkblue"

    vbar_tbl3_tot_col2.vbar(x = 'x', top = 'y2', color= "red",  width = 3, source=varea_tbl3_stack_source, legend_label = COLUMN_6)

    vbar_tbl3_tot_col2.legend.location = legend_location

    vbar_tbl3_tot_col2.legend.label_text_font_size = legend_font_size



    ###############################################################################
    #   #######   #     ####    #      ######    #
    #      #     #  #   #   #   #      #       # #
    #      #    ######  ####    #      ###    ######
    #      #    #    #  #   #   #      #         #
    #      #    #    #  ####    #####  ######  ####
    ###############################################################################


    #######################################
    # Visualize Hourly Past  7 Day Data
    #######################################

    line4_tbl4_hourly_7_day = figure(plot_width=largeplotWidth, plot_height=largeplotHeight,  x_axis_type="datetime")

    line4_tbl4_hourly_7_day.title.text = (str(N_hourly_days) + " Day " +  HOURLY_TBL)

    line4_tbl4_hourly_7_day.title.align = "center"

    line4_tbl4_hourly_7_day.title.text_color = "white"

    line4_tbl4_hourly_7_day.title.text_font_size = "15px"

    line4_tbl4_hourly_7_day.title.background_fill_color = "darkblue"##aaaaee"

    line4_tbl4_hourly_7_day.diamond( x=COLUMN_DATE, y = COLUMN_8 , line_width = 3, alpha = 0.5, color=("red"),  source=df_hourly_7_day_tbl_4, legend_label = ('HOURLY ' + COLUMN_8) )

    line4_tbl4_hourly_7_day.circle( x=COLUMN_DATE, y = COLUMN_7 , line_width = 2, alpha = 0.5, color=("blue"), source=df_hourly_7_day_tbl_4, legend_label = ("HOURLY"  + COLUMN_7))

    line4_tbl4_hourly_7_day.legend.location = legend_location

    line4_tbl4_hourly_7_day.legend.label_text_font_size = legend_font_size

#######################################
# Calculate the BEST_FIT line against _MAX
#######################################

    int_list = []

    for mydate in df_hourly_7_day_tbl_4[COLUMN_DATE]:

        int_list.append(date_to_seconds(mydate))

        int_list = sorted(int_list)

    xs = np.array(int_list, dtype = float)

    ys = np.array(df_hourly_7_day_tbl_4[COLUMN_8], dtype = float)

    m, b = best_fit(xs, ys)

    regression_line = [ (m * x) + b  for x in xs]

    line4_tbl4_hourly_7_day.line(df_hourly_7_day_tbl_4[COLUMN_DATE], regression_line, color = 'yellow', alpha = 0.3, line_width = 6, legend_label = 'BEST_FIT of ' + COLUMN_8)

#######################################
# Calculate the OUTLIERS
#######################################

    threshold = 3

    my_mean = np.mean(df_hourly_7_day_tbl_4[COLUMN_8])

    my_std  = np.std(df_hourly_7_day_tbl_4[COLUMN_8])

    for count, i in enumerate(df_hourly_7_day_tbl_4[COLUMN_8]):

        if ( ( i - my_mean ) / my_std ) > threshold:

            line4_tbl4_hourly_7_day.circle( x=df_hourly_7_day_tbl_4.iloc[count:count+1,0], y = df_hourly_7_day_tbl_4.iloc[count:count+1,2] , line_width = 7, alpha = 0.5, color=("green"), legend_label = COLUMN_8 + " Outlier")

   


    #######################################
    # Visualized
    #######################################

    #######################################
    # Visualize Daily Data
    #######################################


    line4_tbl4_daily = figure(plot_width=largeplotWidth, plot_height=largeplotHeight,  x_axis_type="datetime")

    line4_tbl4_daily.title.text = ("Past Month " + DAILY_TBL)

    line4_tbl4_daily.title.align = "center"

    line4_tbl4_daily.title.text_color = "white"

    line4_tbl4_daily.title.text_font_size = "15px"

    line4_tbl4_daily.title.background_fill_color = "darkblue"##aaaaee"

    line4_tbl4_daily.line( x=COLUMN_DATE, y =   COLUMN_8 , color=("red"),  source=df_daily_30_day_tbl_4, legend_label = ('DAILY ' + COLUMN_8))#, legend = "db_tbl_4_SIZE_MAX")#, hatch_weight = 5, legend_label="Sunrise")

    line4_tbl4_daily.line( x=COLUMN_DATE, y = COLUMN_7 , color=("blue"), source=df_daily_30_day_tbl_4, legend_label = ("DAILY " + COLUMN_7))#, legend = ["db_tbl_4_SIZE_AVG","db_tbl_4_SIZE_MAX"])#, hatch_weight = 5, legend_label="Sunrise")

    line4_tbl4_daily.legend.location = legend_location

    line4_tbl4_daily.legend.label_text_font_size = legend_font_size


    #######################################
    # Visualize Entire Data
    #######################################

    vbar_tbl4_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_4[COLUMN_DATE], #INTERVAL_START, 
                                       y1 = df_hourly_full_tbl_4[COLUMN_7], #LIST_RAW_SIZE_AVG, 
                                       y2 = df_hourly_full_tbl_4[COLUMN_8])) #, #LIST_RAW_SIZE_MAX, 
                                       #label = [COLUMN_7, COLUMN_8]))


    vbar_tbl4_tot_col1 = figure(plot_width=smallplotWidth, plot_height=smallplotHeight,  x_axis_type="datetime")

    vbar_tbl4_tot_col1.title.text = (HOURLY_TBL)

    vbar_tbl4_tot_col1.title.align = "center"

    vbar_tbl4_tot_col1.title.text_color = "yellow"

    vbar_tbl4_tot_col1.title.text_font_size = "15px"

    vbar_tbl4_tot_col1.title.background_fill_color = "darkblue"

    vbar_tbl4_tot_col1.vbar(x = 'x', top = 'y1', color= "blue",  width = 3, source=vbar_tbl4_source, legend_label = COLUMN_7)

    vbar_tbl4_tot_col1.legend.location = legend_location

    vbar_tbl4_tot_col1.legend.label_text_font_size = legend_font_size


    varea_tbl4_stack_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_4[COLUMN_DATE], #INTERVAL_START, 
                                       y1 = df_hourly_full_tbl_4[COLUMN_7], #LIST_RAW_SIZE_AVG, 
                                       y2 = df_hourly_full_tbl_4[COLUMN_8], #LIST_RAW_SIZE_MAX, 
                                       ))

    vbar_tbl4_tot_col2 = figure(plot_width=smallplotWidth, plot_height=smallplotHeight,  x_axis_type="datetime")

    vbar_tbl4_tot_col2.title.text = (HOURLY_TBL)

    vbar_tbl4_tot_col2.title.align = "center"

    vbar_tbl4_tot_col2.title.text_color = "yellow"

    vbar_tbl4_tot_col2.title.text_font_size = "15px"

    vbar_tbl4_tot_col2.title.background_fill_color = "darkblue"

    vbar_tbl4_tot_col2.vbar(x = 'x', top = 'y2', color= "red",  width = 3, source=varea_tbl4_stack_source, legend_label = COLUMN_8)

    vbar_tbl4_tot_col2.legend.location = legend_location

    vbar_tbl4_tot_col2.legend.label_text_font_size = legend_font_size

###################################
# Prepare visualization by grouping charts into rows and columns
###################################

    p_tbl1  = column(vbar_tbl1_tot_col1, vbar_tbl1_tot_col2)

###################################
# Add Row heading
###################################

    p_ctbl1 = column(Div(text = "<H3 style=\"text-align:center;\">" + COLUMN_1 + " & " + COLUMN_2 + "</H3>"), p_tbl1)

###################################
# Same again  - Prep by grouping and add row headings
###################################

    p_tbl2  = column(vbar_tbl2_tot_col1, vbar_tbl2_tot_col2)

    p_ctbl2 = column(Div(text = "<H3 style=\"text-align:center;\">" + COLUMN_3 + "\t&\t" + COLUMN_4 + "</H3>"), p_tbl2)

    p_tbl3  = column(vbar_tbl3_tot_col1, vbar_tbl3_tot_col2)

    p_ctbl3 = column(Div(text = "<H3 style=\"text-align:center;\">" + COLUMN_5 + "\t&\t" + COLUMN_6 + "</H3>"), p_tbl3)

    p_tbl4 = column(vbar_tbl4_tot_col1, vbar_tbl4_tot_col2)

    p_ctbl4 = column(Div(text = "<H3 style=\"text-align:center;\">" + COLUMN_7 + "\t&\t" + COLUMN_8 + "</H3>"), p_tbl4)


    MEM_OBJECT_GRIDPLOT = gridplot([[p_ctbl1, 
        line1_tbl1_daily, 
        line1_tbl1_hourly_7_day], 
        [p_ctbl2, 
        line2_tbl2_daily,
        line2_tbl2_hourly_7_day],
        [p_ctbl3,
        line3_tbl3_daily,
        line3_tbl3_hourly_7_day],
        [p_ctbl4,
        line4_tbl4_daily,
        line4_tbl4_hourly_7_day]], toolbar_location='right')

    line1_tbl1_daily.add_tools(HoverTool(tooltips = [(COLUMN_DATE, "$x{%F}")],
                                        formatters = {"$x" :'datetime'}))

    line1_tbl1_hourly_7_day.add_tools(HoverTool(tooltips = [(COLUMN_DATE, "$x{%Y-%m-%d  hour:%H}")],
                                        formatters = {"$x" :'datetime'}))
 
    line2_tbl2_daily.add_tools(HoverTool(tooltips = [(COLUMN_DATE, "$x{%F}")],
                                        formatters = {"$x" :'datetime'}))

    line2_tbl2_hourly_7_day.add_tools(HoverTool(tooltips = [(COLUMN_DATE, "$x{%Y-%m-%d  hour:%H}")],
                                        formatters = {"$x" :'datetime'}))

    line3_tbl3_daily.add_tools(HoverTool(tooltips = [(COLUMN_DATE, "$x{%F}")],
                                        formatters = {"$x" :'datetime'}))

    line3_tbl3_hourly_7_day.add_tools(HoverTool(tooltips = [(COLUMN_DATE, "$x{%Y-%m-%d  hour:%H}")],
                                        formatters = {"$x" :'datetime'}))

    line4_tbl4_daily.add_tools(HoverTool(tooltips = [(COLUMN_DATE, "$x{%F}")],
                                        formatters = {"$x" :'datetime'}))

    line4_tbl4_hourly_7_day.add_tools(HoverTool(tooltips = [(COLUMN_DATE, "$x{%Y-%m-%d  hour:%H}")],
                                        formatters = {"$x" :'datetime'}))

    show(column(Div(text = "<H1 style=\"text-align:center;border:1px solid red;color:yellow;background-color: darkblue;\">" + DAILY_TBL + " & " + HOURLY_TBL + "</H1>"), MEM_OBJECT_GRIDPLOT))

    log_and_print_info("#--------------------------------------#")

    log_and_print_info("# " + os.path.basename(__file__) + " Exit Stats")
    
    log_and_print_info("# " + os.path.basename(__file__) + " Config section:\t " + config_section)

    log_and_print_info("# " + os.path.basename(__file__) + " with HOURLY_TBL:\t " + HOURLY_TBL)

    log_and_print_info("# " + os.path.basename(__file__) + " and DAILY_TBL:\t " +  DAILY_TBL)

    log_and_print_info("#--------------------------------------#")

    log_and_print_info("")

    log_and_print_info("#--------------------------------------#")

    log_and_print_info("# " + os.path.basename(__file__) + " successfully exited after processing " + config_in)

    log_and_print_info("#--------------------------------------#")