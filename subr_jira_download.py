#######################################
# Name: jira_download.py
# Desc: Provide numeric part of EXA-ticket
#       and download the attachments
# 
#----------------------------------------------------------------Modules
import sys, os

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

logging_filename = "igapa_master.py.log"

logging.basicConfig(filename = logging_filename, level=logging.INFO, filemode = 'a', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

logging.info("#--------------------------------------#")

logging.info("# Entering " + os.path.basename(__file__))

logging.info(("#--------------------------------------#"))

try:

    from subr_validate_ticket import ticket_validation

except:

    logging.error("########################################")

    logging.error("# Error: " + os.path.basename(__file__))

    logging.error("# program subr_validate_ticket.py not found")

    logging.error("# so we are unable to validate the ticket.")

    logging.error("# Aborting with no action taken...")

    logging.error("########################################")

    print()

    print("########################################")

    print("# Error:")

    print("#")

    print("# program subr_validate_ticket.py not found")

    print("# so we are unable to validate the ticket.")

    print("#")

    print("# Aborting with no action taken...")

    print("########################################")

    print()
    
    sys.exit(13)

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

try:
    
    import configparser

except:
    
    os.system('pip install configparser')
    
    import configparser

try:

    from tools_parse_config import ParseConfig

except:
    
    msg = "Unable to find tools_parse_config.py"

    logging.error("#######################################")

    logging.error("# ERROR in " +  os.path.basename(__file__))
    
    logging.error("# " + msg)

    logging.error("# " +  os.path.basename(__file__) + " aborting with no action taken.")

    logging.error("#######################################")

    print("#######################################")

    print("# ERROR in", os.path.basename(__file__))
    
    print(msg)

    print("#", os.path.basename(__file__), "aborting with no action taken.")

    print("#######################################")

    sys.exit(13)



#----------------------------------------------------------------Variables

if __name__ == "__main__":

    if len(sys.argv) > 1:

        in_ticket = sys.argv[1]

        logging.info("# " + os.path.basename(__file__) + " read in parameter in_ticket: " + str(in_ticket))

    else:
       
        in_ticket = 28615

        logging.info("# " + os.path.basename(__file__) + " read in parameter in_ticket: " + str(in_ticket))
else:

    in_ticket = sys.argv[1]

    logging.info("# " + os.path.basename(__file__) + " read in parameter in_ticket: " + str(in_ticket))

print("#####################################")

print("# INFO:", os.path.basename(__file__), "received ticket", str(in_ticket))

print("#####################################")

now = dt.today().strftime('%Y%m%d-%H%M%S')

a = ticket_validation(in_ticket)

myTicket= a.ticket_validate_number() # Your ticket: EXA-1234x

work_ticket = 0

class_chart = "DB_SIZE"

try:

    b = ParseConfig(class_chart)

except Exception as e:

    logging.error("#######################################")

    logging.error("FATAL: " +  os.path.basename(__file__))

    logging.error("# Unable to reference ParseConfig using:")

    logging.error("# b = ParseConfig(class_chart)")

    logging.error("# Does pgm tools_parse_config.py exist in " +  os.getcwd(),"?" )

    logging.error("# Aborting with no action taken.")

    logging.error(e, exc_info = True)

    logging.error("#######################################")

    print("#######################################")

    print("FATAL:", os.path.basename(__file__))

    print("# Unable to reference ParseConfig using:")

    print("# b = ParseConfig(class_chart)")

    print("# Does pgm tools_parse_config.py exist in", os.getcwd(),"?" )

    print("# Aborting with no action taken.")

    print("#######################################")

    print(e)

    sys.exit(13)

user, pasw = b.read_config_admin_admin('.', 'config_admin.ini')

logging.info("# " + os.path.basename(__file__) + " using JIRA credentials for user " + user)

print("#######################################")

print("# INFO:", os.path.basename(__file__),"using JIRA credentials for user", user)

print("#######################################")

jiraURL = 'https://www.exasol.com/support/rest/api/2/issue/EXA-'

attachment_final_url="" # To validate if there are or not attachments

logging.info("# " + os.path.basename(__file__) + " processing ticket for myTicket: " + str(myTicket))

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
        
        logging.info("# " + os.path.basename(__file__) + " making URL Call: " + jiraURL + myTicket)

        r = requests.get(jiraURL+myTicket, auth=(user, pasw),timeout=5)

    except Exception as e:

        logging.error("#####################################")

        logging.error("# Error " + os.path.basename(__file__))

        logging.error("# " + os.path.basename(__file__) + " Unable to find ticket " +  str(myTicket))

        logging.error("# " + os.path.basename(__file__) + " Aborting with no action taken.")

        logging.error(e, exc_info = True)

        logging.error("#####################################")

        print("#####################################")

        print("# Error " + os.path.basename(__file__))

        print("# " + os.path.basename(__file__) + " Unable to find ticket", myTicket)

        print("# " + os.path.basename(__file__) + " Aborting with no action taken.")

        print("#")

        print("#####################################")

        print(e)

        sys.exit(13)

    # status of the request
    rstatus = r.status_code

    work_ticket = str('EXA-' + str(myTicket))

    if rstatus == 200:

        data = r.json()
#-------------------------------------#
# Create new directory same as ticket
#-------------------------------------#

        print("#######################################")

        if os.path.exists(work_ticket):

            try:
                
                dest_dir = str(work_ticket + '_' + now)

                os.rename(work_ticket, dest_dir )

                logging.info("# " + os.path.basename(__file__) + " renaming " + str(work_ticket) + " to " + dest_dir)

                print("# INFO:", os.path.basename(__file__), " renaming", work_ticket, "to ", dest_dir)

            except:

                logging.warning("#-------------------------------------#")

                logging.warning("# WARNING: " +  os.path.basename(__file__) + " unable to rename")

                logging.warning("# from: " +  str(work_ticket) +  " to " +  dest_dir)

                logging.warning("#-------------------------------------#")

                print("#######################################")

                print("# WARNING:")

                print("#", os.path.basename(__file__), " unable to rename")

                print("# from:", work_ticket, "to", dest_dir)

                print("#######################################")


        os.mkdir(work_ticket)

        work_dir = os.path.join(save_dir, work_ticket)

        logging.info("# " + os.path.basename(__file__) + " saving work in: " + work_dir)

        print("# INFO:", os.path.basename(__file__), "saving work in:", work_dir)

        print("#######################################")

        #######################################
        # C H A N G I N G    D I R E C T O R Y
        #######################################

        os.chdir(work_ticket)

    else:

        logging.error("#####################################")

        logging.error("# " + os.path.basename(__file__) + " Error: accessing JIRA with return code: " + str(rstatus))

        logging.error("# " + os.path.basename(__file__) + " Unable to process ticket " +  work_ticket)

        logging.error("# ---> Does ticket " + work_ticket + " even exist?")

        logging.error("# ---> For ticket " + work_ticket + " Do you have access permission on JIRA?")

        logging.error("# " + os.path.basename(__file__) + " had URL read return code: " + str(rstatus))

        logging.error("# " + os.path.basename(__file__) + " Aborting with no action taken.")

        logging.error("#####################################")

        print("#####################################")

        print("# " + os.path.basename(__file__) + " Error: accessing JIRA with return code:" + str(rstatus))

        print("# " + os.path.basename(__file__) + " Unable to process ticket", work_ticket)

        print("# ---> Does ticket " + work_ticket + " even exist?")

        print("# ---> For ticket " + work_ticket + " Do you have access permission on JIRA?")

        print("# " + os.path.basename(__file__) + " Aborting with no action taken.")

        print("#####################################")

        sys.exit(13)

    if not data['fields']['attachment'] :

        status_attachment = 'ERROR: Nothing attached'

        attachment_final_url=""

        logging.warning("#####################################")

        logging.warning("# " + os.path.basename(__file__) + " WARNING")

        logging.warning("#  No Attachments found for " +  work_ticket)

        logging.warning("# The folder " +  work_ticket, "will be empty")

        logging.warning("# and no reports will be run")

        logging.warning("#####################################")

        print("#####################################")

        print("# WARNING")

        print("#")

        print("# No Attachments found for", work_ticket)

        print("# The folder", work_ticket, "will be empty")

        print("# and no reports will be run")

        print("#####################################")

        sys.exit(13)

    else:

        for i in data['fields']['attachment'] :

             attachment_final_url = i['content']
            
             attachment_filename = i['filename']
            
             status_attachment_name = 'OK: The desired attachment exists: ' + attachment_filename
            
             logging.info("# " + os.path.basename(__file__) + " trying to download " + attachment_final_url)

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

logging.info("#-------------------------------------#")

logging.info("# " + os.path.basename(__file__) + " successfully exited")

logging.info("#-------------------------------------#")