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

if (
     (os.path.exists(work_dir + '\\' + DAILY_TBLZ[0])  and (os.path.exists(work_dir + '\\' + HOURLY_TBLZ[0]))) or

     (os.path.exists(work_dir + '\\' + DAILY_TBLZ[1])  and (os.path.exists(work_dir + '\\' + HOURLY_TBLZ[1]))) or 

     (os.path.exists(work_dir + '\\' + DAILY_TBLZ[2])  and (os.path.exists(work_dir + '\\' + HOURLY_TBLZ[2]))) or 

     (os.path.exists(work_dir + '\\' + DAILY_TBLZ[3])  and (os.path.exists(work_dir + '\\' + HOURLY_TBLZ[3]))) 
    ):

        subprocess.call(["python", dir_path + "/" + "subr_chart_4_rows.py", str(in_ticket)])

else:

    print("#####################################")

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
