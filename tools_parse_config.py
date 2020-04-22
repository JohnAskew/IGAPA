import os, sys

try:

    import configparser

except:

    os.system('pip install configparser')

    import configparser

#######################################
class ParseConfig:
#######################################
#-------------------------------------#
    def __init__(self, myconfig):
#-------------------------------------#

        self.myconfig = myconfig

#-------------------------------------#
    def read_config_sections(self, path = '.'):
#-------------------------------------#

        self.path = path

        config = configparser.ConfigParser()

        x = (self.path + '/config.ini')

        y = config.read(x)

        if len(y) == 0:

            print("#######################################")

            print("# FATAL:", os.path.basename(__file__))

            print("# config.ini not found or is not readable.")

            print("# This program was looking for:", x)

            print("#")

            print("# Ensure config.ini exists in this directory:", os.getcwd())

            print("# ---> Does config.ini exist?")

            print("# ---> Is config.ini a readable file?")

            print("# Here is the output from attempted config file read:", y)

            print("# Aborting with no action taken.")

            print("#######################################")

            sys.exit(0)


        try:

            z = config.sections()

            print("#######################################")

            print("# INFO:", os.path.basename(__file__),"found config.ini with these sections:", z)

            print()

            return z

        except:

            print("#######################################")

            print("ERROR:", os.path.basename(__file__))

            print("#Unable to parse config.ini. ")

            print("# Aborting with no action taken")

            print("#######################################")

            print(e)

            sys.exit(0)

        

#-------------------------------------#
    def run(self, path = '.'):
#-------------------------------------#

        self.path = path

        myConfig = self.myconfig

        pass_fail = True
        
        config = configparser.ConfigParser()

        x = (self.path + '/config.ini')

        try:

            config.read(x)

        except Exception as e:

            print("#######################################")

            print("FATAL:", os.path.basename(__file__))

            print("# Unable to config.read('config.ini')")

            print("# in section run with config.read:", config.read('config.ini'))

            print("# Aborting with no action taken.")

            print("#######################################")

            print(e)

            sys.exit(0)

        for item in ['CONFIG_HOURLY_TBL','CONFIG_DAILY_TBL','CONFIG_ROW1_COL_X_AXIS','CONFIG_ROW1_COL_Y_AXIS_1','CONFIG_ROW1_COL_Y_AXIS_2','CONFIG_ROW2_COL_X_AXIS','CONFIG_ROW2_COL_Y_AXIS_1','CONFIG_ROW2_COL_Y_AXIS_2','CONFIG_ROW3_COL_X_AXIS','CONFIG_ROW3_COL_Y_AXIS_1','CONFIG_ROW3_COL_Y_AXIS_2','CONFIG_ROW4_COL_X_AXIS','CONFIG_ROW4_COL_Y_AXIS_1','CONFIG_ROW4_COL_Y_AXIS_2']:

            try:

                config.get(myConfig, item)

            except Exception as e:

                print("# ERROR:", os.path.basename(__file__), "config.ini", myConfig, "missing -->\t", item)

                pass_fail = False


        print("#######################################")
        if not pass_fail:

            quit(0)
                  
        return config[myConfig]['CONFIG_HOURLY_TBL'] \
        ,config[myConfig]['CONFIG_DAILY_TBL']        \
        ,config[myConfig]['CONFIG_ROW1_COL_X_AXIS']       \
        ,config[myConfig]['CONFIG_ROW1_COL_Y_AXIS_1']     \
        ,config[myConfig]['CONFIG_ROW1_COL_Y_AXIS_2']     \
        ,config[myConfig]['CONFIG_ROW2_COL_X_AXIS']       \
        ,config[myConfig]['CONFIG_ROW2_COL_Y_AXIS_1']     \
        ,config[myConfig]['CONFIG_ROW2_COL_Y_AXIS_2']     \
        ,config[myConfig]['CONFIG_ROW3_COL_X_AXIS']       \
        ,config[myConfig]['CONFIG_ROW3_COL_Y_AXIS_1']     \
        ,config[myConfig]['CONFIG_ROW3_COL_Y_AXIS_2']     \
        ,config[myConfig]['CONFIG_ROW4_COL_X_AXIS']       \
        ,config[myConfig]['CONFIG_ROW4_COL_Y_AXIS_1']     \
        ,config[myConfig]['CONFIG_ROW4_COL_Y_AXIS_2']     

#######################################
# M A I N   L O G I C
#######################################
if __name__ == '__main__':

    a = ParseConfig('DB_SIZE')

    a.read_config_sections()

    CONFIG_ROW1_HOURLY_TBL, CONFIG_ROW1_DAILY_TBL, CONFIG_ROW1_COL_X_AXIS, CONFIG_ROW1_COL_Y_AXIS_1, CONFIG_ROW1_COL_Y_AXIS_2, CONFIG_ROW2_COL_X_AXIS, CONFIG_ROW2_COL_Y_AXIS_1, CONFIG_ROW2_COL_Y_AXIS_2, CONFIG_ROW3_COL_X_AXIS, CONFIG_ROW3_COL_Y_AXIS_1, CONFIG_ROW3_COL_Y_AXIS_2, CONFIG_ROW4_COL_X_AXIS, CONFIG_ROW4_COL_Y_AXIS_1, CONFIG_ROW4_COL_Y_AXIS_2 = a.run()

    print("==> Returning:", CONFIG_ROW1_HOURLY_TBL, CONFIG_ROW1_DAILY_TBL, CONFIG_ROW1_COL_X_AXIS, CONFIG_ROW1_COL_Y_AXIS_1, CONFIG_ROW1_COL_Y_AXIS_2, CONFIG_ROW2_COL_X_AXIS, CONFIG_ROW2_COL_Y_AXIS_1, CONFIG_ROW2_COL_Y_AXIS_2, CONFIG_ROW3_COL_X_AXIS, CONFIG_ROW3_COL_Y_AXIS_1, CONFIG_ROW3_COL_Y_AXIS_2, CONFIG_ROW4_COL_X_AXIS, CONFIG_ROW4_COL_Y_AXIS_1, CONFIG_ROW4_COL_Y_AXIS_2)







