#######################################
# Name: jira_download.py
# Desc: Provide numeric part of EXA-ticket
#       and download the attachments
# 
#----------------------------------------------------------------Modules
import sys, os

try:

    from subr_validate_ticket import ticket_validation

except:

    print()

    print("########################################")

    print("# Error:")

    print("#")

    print("# program subr_validate_ticket.py not found")

    print("# so we are unable to validate the ticket.")

    print("#")

    print("# Aborting with not action taken...")

    print("########################################")

    print()

    sys.exit(0)

try:

    import csv

except:

    os.system('pip install csv')

    import csv

try:

    import json

except:

    os.system('pip install json')

    import json

try:

    import requests

except:

    os.system('pip install requests')

    import requests

try:

    from datetime import datetime as dt

except:

    os.system('pip install datetime')

    from datetime import datetime as dt
#----------------------------------------------------------------Variables

if __name__ == "__main__":

    if len(sys.argv) > 1:

        in_ticket = sys.argv[1]

    else:
       
        in_ticket = 28615
else:

    in_ticket = sys.argv[1]

print("#####################################")

print("# INFO:", os.path.basename(__file__), "received ticket", in_ticket)

print("#####################################")

now = dt.today().strftime('%Y%m%d-%H%M%S')

a = ticket_validation(in_ticket)

myTicket= a.ticket_validate_number() # Your ticket: EXA-1234x

work_ticket = 0

user = '<user>'     # JIRA user

pasw = '<secret>' # JIRA password

jiraURL = 'https://www.exasol.com/support/rest/api/2/issue/EXA-'

attachment_final_url="" # To validate if there are or not attachments

print("#--------------------------------------#")

print("INFO:", os.path.basename(__file__), "processing ticket for", myTicket)

print("---------------------------------------#")

save_dir = os.getcwd()

#-------------------------------------#
def main() :
#-------------------------------------#
    global myTicket
    
    myTicket = str(myTicket)

    try:
        
        r = requests.get(jiraURL+myTicket, auth=(user, pasw),timeout=5)

    except Exception as e:

        print("#####################################")

        print("# Error")

        print("#")

        print("# Unable to find ticket", myTicket)

        print("# Aborting with no action taken.")

        print("#")

        print("#####################################")

        print(e)

        sys.exit(0)

    # status of the request
    rstatus = r.status_code

    work_ticket = str('EXA-' + str(myTicket))

    if rstatus == 200:

        data = r.json()
#-------------------------------------#
# Create new directory same as ticket
#-------------------------------------#

        if os.path.exists(work_ticket):

            try:
                
                dest_dir = str(work_ticket + '_' + now)

                os.rename(work_ticket, dest_dir )

                print("#######################################")

                print("# INFO:", os.path.basename(__file__), " renaming")

                print("#")

                print("#", work_ticket, "to ", dest_dir)

                print("#######################################")

            except:

                print("#######################################")

                print("# WARNING:")

                print("#", os.path.basename(__file__), " unable to rename")

                print("# from:", work_ticket, "to", dest_dir)

                print("#######################################")


        os.mkdir(work_ticket)

        work_dir = os.path.join(save_dir, work_ticket)

        print("#--------------------------------------#")

        print("INFO: Saving work in:", work_dir)

        print("#--------------------------------------#")

        #######################################
        # C H A N G I N G    D I R E C T O R Y
        #######################################
        os.chdir(work_ticket)

    else:

        print("#####################################")

        print ('# Error: accesing JIRA:' + str(rstatus))

        print("#")

        print("# Unable to process ticket", work_ticket)

        print("#")

        print("# Aborting with no action taken.")

        print("#####################################")

        sys.exit(0)

    if not data['fields']['attachment'] :

        status_attachment = 'ERROR: Nothing attached'

        attachment_final_url=""

        print("#####################################")

        print("# WARNING")

        print("#")

        print("#No Attachments found for", work_ticket)

        print("# The folder", work_ticket, "will be empty")

        print("# and no reports will be run")

        print("#####################################")

        sys.exit(0)

    else:
        for i in data['fields']['attachment'] :
             attachment_final_url = i['content']
             attachment_filename = i['filename']
             status_attachment_name = 'OK: The desired attachment exists: ' + attachment_filename
             print(attachment_final_url)
             attachment_name = False
             attachment_amount = False
             attachment_files = False
             if attachment_final_url != "" :
                 r = requests.get(attachment_final_url, auth=(user, pasw), stream=True)
                 with open(attachment_filename, "wb") as f:
                     f.write(r.content.decode('iso-8859-1').encode('utf8'))
                 f.close()
             else:
               print ("no file")

    #-------------------------------------#
    # C H A N G E   D I R E C T O R Y
    #-------------------------------------#
    os.chdir(save_dir)

if __name__ == "__main__" :
    main() 