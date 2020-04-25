#----------------------------------------------------------------Modules
import sys, os

try:

    import numbers

except:

    os.system('pip install numbers')

    import numbers

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


#######################################
class ticket_validation:
#######################################

#--------------------------------------
    def __init__(self, ticket_number = 28615):
#--------------------------------------

        self.ticket_number = ticket_number

        logging.info(("#------------------------------------#"))

        logging.info("# Entering " + os.path.basename(__file__) + " Class ticket_validation with ticket_number " + str(self.ticket_number))

        logging.info(("#------------------------------------#"))

#--------------------------------------
    def ticket_validate_number(self):
#--------------------------------------

        logging.info("# " + os.path.basename(__file__) + " method: ticket_validate_number with ticket_number " + str(self.ticket_number))


        if len(str(self.ticket_number))  == 0 or __name__ == "__main__" :

            return 28615

        if len(str(self.ticket_number)) > 1 and len(str(self.ticket_number)) > 5:

            logging.error("#########################################")

            logging.error("# Error: " + os.path.basename(__file__))

            logging.error("# TICKET EXA-xxx expecting up to 5 numbers.")

            logging.error("# ---> Example: 12345")

            logging.error("# received: " + self.ticket_number)

            logging.error("# Aborting with no action taken")

            logging.error("#########################################")

            print("#########################################")

            print("# Error: " + os.path.basename(__file__))

            print("# TICKET EXA-xxx expecting up to 5 numbers.")

            print("# ---> Example: 12345")

            print("# received: " + self.ticket_number)

            print("# Aborting with no action taken")

            print("#########################################")

            sys.exit(-1)

        else:

            try:

                if len(str(self.ticket_number)) <=5 and isinstance(int(self.ticket_number), numbers.Number):

                    myTicket = self.ticket_number

                    logging.info("# " + os.path.basename(__file__) + " validated and returning with: " + str(myTicket))


                    logging.info("#-------------------------------------#")

                    logging.info("# " + os.path.basename(__file__) + " successfully exited.")

                    logging.info("#-------------------------------------#")

                    return myTicket

            except Exception as e:

                            logging.error("#########################################")

                            logging.error("# Error: " + os.path.basename(__file__))

                            logging.error("# TICKET EXA-xxx expecting all numbers.")

                            logging.error("# ---> Example: 12345")

                            logging.error("# received: " + self.ticket_number)

                            logging.error("# Aborting with no action taken")

                            logging.error(e , exc_info=True)

                            logging.error("#########################################")

                            print("#########################################")

                            print("# Error: " + os.path.basename(__file__))

                            print("# TICKET EXA-xxx expecting all numbers.")

                            print("# ---> Example: 12345")

                            print("# received: " + self.ticket_number)

                            print("# Aborting with no action taken")

                            print(e )

                            print("#########################################")

                            sys.exit(-1)



        # logging.info(os.path.basename(__file__) + " validated and returning (exit pgm) with: " + str(myTicket))

        # logging.info("#-------------------------------------#")

        # return myTicket

#######################################
# M A I N   L O G I C
#######################################

if __name__ == "__main__" :

    a = ticket_validation(28615)

    b = a.ticket_validate_number()

    logging.info("# " + os.path.basename(__file__) + " executed as MAIN pgm and self processed " + str(b))

    print("#######################################")

    print("# " + os.path.basename(__file__) + " executed as MAIN pgm and self processed " + str(b))

    print("#######################################")

    logging.info(("#------------------------------------#"))

    logging.info("# " + os.path.basename(__file__) + " successfully exited")

    logging.info(("#------------------------------------#"))