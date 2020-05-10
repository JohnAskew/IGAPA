#! python3
#------------------------------------#
# This section will install python 
# modules needed to run this script
#------------------------------------#
import os, sys

try:

    import subprocess

except:

    os.system("pip install subprocess")

    import subprocess

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

    from tools_parse_config import ParseConfig

except:
    
    msg = "Unable to find tools_parse_config.py"

    logger.error("#######################################")

    logger.error("# ERROR in " +  os.path.basename(__file__))
    
    logger.error("# " + msg)

    logger.error("# " +  os.path.basename(__file__) + " aborting with no action taken.")

    logger.error("#######################################")

    print("#######################################")

    print("# ERROR in", os.path.basename(__file__))
    
    print(msg)

    print("#", os.path.basename(__file__), "aborting with no action taken.")

    print("#######################################")

    sys.exit(13)


#######################################
# VARIABLES
#######################################

now = dt.today().strftime('%Y%m%d_%H%M%S')

dir_path = os.path.dirname(os.path.realpath(__file__))

new_dir =""

global in_ticket

in_ticket = ""

class_chart = 'DB_SIZE'

log_level = "WARNING"

######################################
# START LOGIC for MAIN
######################################
if __name__ == "__main__":

    if len(sys.argv) > 1:

        in_ticket = sys.argv[1]

        new_dir = str("EXA-" + str(in_ticket))

    else:

        in_ticket = 28727

        new_dir = str("EXA-" + str(in_ticket))

    if len(sys.argv) > 2:

        config_in = sys.argv[2]

    else:

        config_in = 'config_reports.ini'

else:

    in_ticket - 28727

    new_dir = str("EXA-" + str(in_ticket))

    config_in = 'config_reports.ini'

#######################################
#######################################
# BEGIN MAIN LOGIC
#######################################
#######################################

#-------------------------------------#
# Extract log_level for reporting details
# ------------------------------------#
try:

    b = ParseConfig(class_chart, 'config_admin.ini')

except Exception as e:

    print("#######################################")

    print("# WARNING" + os.path.basename(__file__) )

    print("#-------------------------------------#")

    print("# Unable to read config_admin.ini section REPORTING to get log_level")

    print("# Using defaults:")

    print("# ===> " + os.path.basename(__file__) + " using log_level of WARNING")

    print(e)

try:

    log_level, outlier_threshold, reports_hourly, reports_daily = b.read_config_admin_reporting('.', 'config_admin.ini')

    print("# " + os.path.basename(__file__) + " REPORTING variables log_level " + log_level )


except Exception as e:

    print("#------------------------------------#")

    print("WARNING: " + os.path.basename(__file__))
    print("#------------------------------------#")

    print("# " + os.path.basename(__file__) + " unable to reference REPORTING section of config_admin.ini")

    print("# Using defaults:")

    print("# ==> log_level " + log_level)

    print(e)


#######################################
# Start by extracting the LOGGING 
#    reporting level for output 
#    granularity (how much detail).
#######################################


#######################################
# Save off the old report - do not overlay
#######################################

logging_filename = str(os.path.basename(__file__) + '.log')

if os.path.exists(logging_filename):

    dest = str(logging_filename + '_' + now + '.log')

    try:

        os.rename(logging_filename, dest)

    except Exception as e:

        print("#--------------------------------------#")

        print("# WARNING: " + os.path.basename(__file__) + " Unable to rename " + logging_filename + " to " + dest)

        print("# " + os.path.basename(__file__) + " REUSING " + logging_filename)

        print(e)

        print("#--------------------------------------#")


#######################################
# Log the beginning of processsing
#######################################



logger = logging.getLogger()

if log_level in ("DEBUG", "INFO"):

    logger.setLevel(logging.INFO)
else:

    logger.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

fh = logging.FileHandler(logging_filename, mode = 'a')

fh.setLevel(logging.INFO)

fh.setFormatter(formatter)

logger.addHandler(fh)

ch = logging.StreamHandler()

ch.setLevel(logging.INFO)

ch.setFormatter(formatter)

logger.addHandler(ch)




#logger.basicConfig(level = logger.INFO, filename = logging_filename, filemode = 'a', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

logger.info("#####################################")

msg_info = "# Starting " + os.path.basename(__file__)

logger.info(msg_info)

filename = str(os.getcwd() + '\\' + config_in)

if os.path.exists(filename):

    logger.info("# " + os.path.basename(__file__) + " was given config file " + config_in)

else:

    logger.error("#####################################")

    logger.error("# " + os.path.basename(__file__)) 

    logger.error("# " + os.path.basename(__file__) + " Could not find config file: " + config_in)

    logger.error("# " + os.path.basename(__file__) + " Ensure " + config_in + " exists in this directory: " + os.getcwd())

    logger.error("# ---> Does " + config_in + " exist?")

    logger.error("# ---> Is "  + config_in + " a readable file?")

    logger.error("# " + os.path.basename(__file__) + " Aborting with no action taken")

    logger.error("#####################################")

    print("#####################################")

    print("# " + os.path.basename(__file__)) 

    print("# Could not find config file: " + config_in)

    print("# Ensure " + config_in + " exists in this directory: " + os.getcwd())

    print("# ---> Does " + config_in + " exist?")

    print("# ---> Is "  + config_in + " a readable file?")

    print("# " + os.path.basename(__file__) + " Aborting with no action taken")

    print("#####################################")

    sys.exit(0)






msg_info = "# " + os.path.basename(__file__) + " is calling jira_download.py with " + str(in_ticket)

logger.info(msg_info)

print("# INFO:", os.path.basename(__file__))

print("# is calling jira_download.py with", str(in_ticket))

print("#####################################")

print()

msg_info = "# Executing call " + dir_path + '\\' + "subr_jira_download.py " + str(in_ticket)

logger.info(msg_info)


subr_rc = subprocess.call(["python", dir_path + "/" + "subr_jira_download.py", str(in_ticket)])

if subr_rc != 0:

    logger.error("# " + os.path.basename(__file__) + " received return code " + str(subr_rc) + " from subr_jira_download.py")

    logger.error("# " + os.path.basename(__file__) + " Aborting with no action taken.")

    print("# " + os.path.basename(__file__) + " Aborting after receiving subr_rc:" + str(subr_rc) + " from subr_jira_download.py")

    print("#####################################")

    sys.exit(-1)

#######################################
# Return to processing the attachments
#######################################

work_dir = os.path.join(dir_path, new_dir)

msg_info = "# " + os.path.basename(__file__) + " received ticket: " + str(in_ticket) + " creating new_dir " + new_dir

logger.info(msg_info)

msg_info = "# " + os.path.basename(__file__) + " | Current directory is " + os.getcwd() + " | Working directory is " + new_dir + " |  Output_dir: " + work_dir

logger.info(msg_info)

print("#####################################")

print("#INFO:", os.path.basename(__file__))

print("# received ticket:", in_ticket, "creating new_dir", new_dir)

print("# Current directory is", os.getcwd())

print("# Working directory is", new_dir)

print("# Output_dir:", work_dir)

print("#####################################")

print()

DAILY_TBLZ   = ['EXA_DB_SIZE_DAILY', 'EXA_SQL_DAILY', 'EXA_MONITOR_DAILY', 'EXA_USAGE_DAILY']

HOURLY_TBLZ  = ['EXA_DB_SIZE_HOURLY','EXA_SQL_HOURLY','EXA_MONITOR_HOURLY','EXA_USAGE_HOURLY']

for table in range(len(DAILY_TBLZ)):

    DAILY_TBLZ[table] = str(DAILY_TBLZ[table] + '.csv')

    HOURLY_TBLZ[table] = str(HOURLY_TBLZ[table] + '.csv')

os.chdir(dir_path)

msg_info = "# " + os.path.basename(__file__) + " processing igapa pgms in directory " + os.getcwd()

logger.info(msg_info)

print("#####################################")

print("#INFO:", os.path.basename(__file__))

print("# processing igapa pgms in directory", os.getcwd())

print("#####################################")

print()

if (
     (os.path.exists(work_dir + '\\' + DAILY_TBLZ[0])  and (os.path.exists(work_dir + '\\' + HOURLY_TBLZ[0]))) or

     (os.path.exists(work_dir + '\\' + DAILY_TBLZ[1])  and (os.path.exists(work_dir + '\\' + HOURLY_TBLZ[1]))) or 

     (os.path.exists(work_dir + '\\' + DAILY_TBLZ[2])  and (os.path.exists(work_dir + '\\' + HOURLY_TBLZ[2]))) or 

     (os.path.exists(work_dir + '\\' + DAILY_TBLZ[3])  and (os.path.exists(work_dir + '\\' + HOURLY_TBLZ[3]))) 
    ):

        msg_info = "# " + os.path.basename(__file__) + " calling python " + dir_path + "\\" + "subr_chart_4_rows.py " + str(in_ticket)  + " " + str(config_in)

        logger.info(msg_info)

        subr_rc = subprocess.call(["python", dir_path + "/" + "subr_chart_4_rows.py", str(in_ticket), str(config_in)])

else:

    print("#####################################")

    msg_info = "#####################################"

    logger.warning(msg_info)

    logger.warning("# ===> Check other logs for ERRORS! <=== ")

    logger.warning("# ===> Check other logs for ERRORS! <=== ")

    logger.warning("# ===> Check other logs for ERRORS! <=== ")
 
    msg_info = "# WARNING: " + os.path.basename(__file__)

    logger.warning(msg_info)

    logger.warning("# processed ticket:\t " +  new_dir)

    logger.warning("# BUT did not find any usable CSV files for")

    logger.warning("# generating charts. Ending processing without any charts.")

    logger.warning("#")

    logger.warning("# This solution is looking for either: ")

    logger.warning("# " +  str(new_dir + '\\' + DAILY_TBLZ[0]) + " and " +  str(new_dir + '\\' + HOURLY_TBLZ[0]) )

    logger.warning("# OR")

    logger.warning("# " +  str(new_dir + '\\' + DAILY_TBLZ[1]) +" and " +  str(new_dir + '\\' + HOURLY_TBLZ[1]) )

    logger.warning("# OR")

    logger.warning("# " +  str(new_dir + '\\' + DAILY_TBLZ[2]) + " and " +  str(new_dir + '\\' + HOURLY_TBLZ[2]) )

    logger.warning("# OR")

    logger.warning("# " +  str(new_dir + '\\' + DAILY_TBLZ[3]) + " and " +  str(new_dir + '\\' + HOURLY_TBLZ[3]) )

    logger.warning("#####################################")

    print("# WARNING:", os.path.basename(__file__))

    print("# processed ticket:\t", new_dir)

    print("# BUT did not find any usable CSV files for")

    print("# generating charts. Ending processing without any charts.")

    print("#")

    print("# This solution is looking for either: ")

    print("#", str(new_dir + '\\' + DAILY_TBLZ[0]), "and", str(new_dir + '\\' + HOURLY_TBLZ[0]) )

    print("# OR")

    print("#", str(new_dir + '\\' + DAILY_TBLZ[1]), "and", str(new_dir + '\\' + HOURLY_TBLZ[1]) )

    print("# OR")

    print("#", str(new_dir + '\\' + DAILY_TBLZ[2]), "and", str(new_dir + '\\' + HOURLY_TBLZ[2]) )

    print("# OR")

    print("#", str(new_dir + '\\' + DAILY_TBLZ[3]), "and", str(new_dir + '\\' + HOURLY_TBLZ[3]) )

    print("#####################################")

logging.info("# " + os.path.basename(__file__) + " Removing CSV files downloaded.")

# for table in range(len(DAILY_TBLZ)):

#     DAILY_TBLZ[table] = str(new_dir + '\\' + DAILY_TBLZ[table])

#     if os.path.exists( DAILY_TBLZ[table]):

#         os.remove(DAILY_TBLZ[table])

#     HOURLY_TBLZ[table] = str(new_dir + '\\' + HOURLY_TBLZ[table])

#     if os.path.exists( HOURLY_TBLZ[table]):

#         os.remove(HOURLY_TBLZ[table])

logger.info("# " + os.path.basename(__file__) + " succeessful exit.")

logger.info("#####################################")
