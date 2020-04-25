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

now = dt.today().strftime('%Y-%m-%d-%H:%M:%S')


#######################################
# VARIABLES
#######################################

dir_path = os.path.dirname(os.path.realpath(__file__))

new_dir =""

global in_ticket

in_ticket = ""

if __name__ == "__main__":

    if len(sys.argv) > 1:

        in_ticket = sys.argv[1]

        new_dir = str("EXA-" + str(in_ticket))

    else:

        in_ticket = 28615

        new_dir = str("EXA-" + str(in_ticket))

    if len(sys.argv) > 2:

        config_in = sys.argv[2]

    else:

        config_in = 'config_reports.ini'

else:

    in_ticket - 28615

    new_dir = str("EXA-" + str(in_ticket))

    config_in = 'config_reports.ini'


#######################################
# Send ticket to extract attachments
#######################################
#######################################
# Log the beginning of processsing
#######################################

logging_filename = str(os.path.basename(__file__) + '.log')

logging.basicConfig(level = logging.INFO, filename = logging_filename, filemode = 'w', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

logging.info("#####################################")

msg_info = "# " + os.path.basename(__file__) + " started at " + now

logging.info(msg_info)

msg_info = "# " + os.path.basename(__file__) + " is calling jira_download.py with " + str(in_ticket)

logging.info(msg_info)

print("# INFO:", os.path.basename(__file__))

print("# is calling jira_download.py with", str(in_ticket))

print("#####################################")

print()

msg_info = "# Executing call " + dir_path + '\\' + "subr_jira_download.py " + str(in_ticket)

logging.info(msg_info)

subprocess.call(["python", dir_path + "/" + "subr_jira_download.py", str(in_ticket)])

#######################################
# Return to processing the attachments
#######################################

work_dir = os.path.join(dir_path, new_dir)

msg_info = "# " + os.path.basename(__file__) + " received ticket: " + str(in_ticket) + " creating new_dir " + new_dir

logging.info(msg_info)

msg_info = "# Current directory is " + os.getcwd() + "  Working directory is " + new_dir + "  Output_dir: " + work_dir

logging.info(msg_info)

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

logging.info(msg_info)

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

        msg_info = "# calling python " + dir_path + "\\" + "subr_chart_4_rows.py " + str(in_ticket)  + " " + str(config_in)

        logging.info(msg_info)

        subprocess.call(["python", dir_path + "/" + "subr_chart_4_rows.py", str(in_ticket), str(config_in)])

else:

    print("#####################################")

    msg_info = "#####################################"

    logging.warning(msg_info)
 
    msg_info = "# WARNING: " + os.path.basename(__file__)

    logging.warning(msg_info)

    logging.warning("# ===> Check other logs for ERRORS!")

    logging.warning("# processed ticket:\t " +  new_dir)

    logging.warning("# BUT did not find any usable CSV files for")

    logging.warning("# generating charts. Ending processing without any charts.")

    logging.warning("#")

    logging.warning("# This solution is looking for either: ")

    logging.warning("# " +  str(new_dir + '\\' + DAILY_TBLZ[0]) + " and " +  str(new_dir + '\\' + HOURLY_TBLZ[0]) )

    logging.warning("# OR")

    logging.warning("# " +  str(new_dir + '\\' + DAILY_TBLZ[1]) +" and " +  str(new_dir + '\\' + HOURLY_TBLZ[1]) )

    logging.warning("# OR")

    logging.warning("# " +  str(new_dir + '\\' + DAILY_TBLZ[2]) + " and " +  str(new_dir + '\\' + HOURLY_TBLZ[2]) )

    logging.warning("# OR")

    logging.warning("# " +  str(new_dir + '\\' + DAILY_TBLZ[3]) + " and " +  str(new_dir + '\\' + HOURLY_TBLZ[3]) )

    logging.warning("#####################################")

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
