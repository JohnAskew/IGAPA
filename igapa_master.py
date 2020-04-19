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

#######################################
# VARIABLES
#######################################

dir_path = os.path.dirname(os.path.realpath(__file__))

new_dir =""

global in_ticket

in_ticket = ""

print("dir_path", dir_path)

if __name__ == "__main__":

    if len(sys.argv) > 1:

        in_ticket = sys.argv[1]

        new_dir = str("EXA-" + str(in_ticket))

    else:

        in_ticket = 28615

        new_dir = str("EXA-" + str(in_ticket))

else:

    in_ticket - 28615

    new_dir = str("EXA-" + str(in_ticket))

#######################################
# Send ticket to extract attachments
#######################################

print("#####################################")

print("# INFO:", os.path.basename(__file__))

print("# is calling jira_download.py with", str(in_ticket))

print("#####################################")

print()

subprocess.call(["python", dir_path + "/" + "subr_jira_download.py", str(in_ticket)])

#######################################
# Return to processing the attachments
#######################################

work_dir = os.path.join(dir_path, new_dir)

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

print(DAILY_TBLZ)

os.chdir(dir_path)

print("#####################################")

print("#INFO:", os.path.basename(__file__))

print("# processing igapa pgms in directory", os.getcwd())

print("#####################################")

print()

if (os.path.exists(work_dir + '\\' + DAILY_TBLZ[0])  and os.path.exists(work_dir + '\\' + HOURLY_TBLZ[0])):

        subprocess.call(["python", dir_path + "/" + "subr_chart_4_rows.py", str(in_ticket)])