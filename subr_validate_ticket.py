#----------------------------------------------------------------Modules
import sys, os

try:

    import numbers

except:

    os.system('pip install numbers')

    import numbers

#######################################
class ticket_validation:
#######################################

#--------------------------------------
    def __init__(self, ticket_number):
#--------------------------------------

        self.ticket_number = ticket_number

#--------------------------------------
    def ticket_validate_number(self):
#--------------------------------------

        if len(str(self.ticket_number))  == 0 or __name__ == "__main__" :

            return 28615

        if len(str(self.ticket_number)) > 1 and len(str(self.ticket_number)) > 5:

            print("#########################################")

            print("# Error:", os.path.basename(__file__))

            print("# TICKET EXA-xxx expecting up to 5 numbers.")

            print("# ---> Example: 12345")

            print("# received:", self.ticket_number)

            print("# Aborting with no action taken")

            print("#########################################")

            sys.exit(0)

        else:

            try:

                if len(str(self.ticket_number)) <=5 and isinstance(int(self.ticket_number), numbers.Number):

                    myTicket = self.ticket_number

            except Exception as e:

                            print("#########################################")

                            print("# Error:", os.path.basename(__file__))

                            print("# TICKET EXA-xxx expecting all numbers.")

                            print("# ---> Example: 12345")

                            print("# Aborting with no action taken")

                            print("# Error:\n" + "#", e)

                            print("#########################################")

                            sys.exit(0)

        print("#-------------------------------------#")

        print(os.path.basename(__file__), "validated", self.ticket_number)

        print("#-------------------------------------#")

        return myTicket

#######################################
# M A I N   L O G I C
#######################################

if __name__ == "__main__" :

    a = ticket_validation(28615)

    b = a.ticket_validate_number()

    print("#######################################")

    print("# INFO:", os.path.basename(__file__), "executed as MAIN pgm and self processed", b)

    print("#######################################")