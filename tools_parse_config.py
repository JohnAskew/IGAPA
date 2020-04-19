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
    def read_config_sections(self):
#-------------------------------------#

        config = configparser.ConfigParser()

        config.read('c:\\users\\joas\\desktop\\exasol\\igapa\\config.ini')

        z = config.sections()

        print("#######################################")

        print("# INFO:", os.path.basename(__file__),"found config.ini with these sections:", z)

        print("#")

        if __name__ == '__main__':
            
            pass

        else:

            return z

#-------------------------------------#
    def run(self):
#-------------------------------------#

        myConfig = self.myconfig

        pass_fail = True
        
        config = configparser.ConfigParser()

        config.read('c:\\users\\joas\\desktop\\exasol\\igapa\\config.ini')

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







