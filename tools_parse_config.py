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
    def __init__(self, myconfig, which_config = 'config_reports.ini'):
#-------------------------------------#

        self.myconfig = myconfig

        self.which_config = which_config

        print("# DEBUG", os.path.basename(__file__), "ParseConfig received which_config:", self.which_config)

#-------------------------------------#
    def read_config_admin_admin(self, path = '.', config_admin = 'config_admin.ini'):
#-------------------------------------#

        self.path = path

        self.config_admin = config_admin

        config = configparser.ConfigParser()

        x = (self.path + '/' + self.config_admin)

        y = config.read(x)

        if len(y) == 0:

            print("#######################################")

            print("# FATAL:", os.path.basename(__file__))

            print("# config_admin.ini not found or is not readable.")

            print("# This program was looking for:", x)

            print("#")

            print("# Ensure config_admin.ini exists in this directory:", os.getcwd())

            print("# ---> Does config_admin.ini exist?")

            print("# ---> Is config_admin.ini a readable file?")

            print("# Here is the output from attempted config file read:", y)

            print("# Aborting with no action taken.")

            print("#######################################")

            sys.exit(0)
        
        try:

            user   = config.get('ADMIN', 'user')

            passwd = config.get('ADMIN', 'passwd')

        except Exception as e:

            print("#######################################")

            print("# ERROR:", os.path.basename(__file__), "config_admin.ini", self.config_admin, "missing login credentials")

            pass_fail = False

            print("#######################################")

            print(e)

            sys.exit(0)

        return (user, passwd)



#-------------------------------------#
    def read_config_sections(self, path = '.'):
#-------------------------------------#

        self.path = path

        config = configparser.ConfigParser()

        x = (self.path + '\\' + self.which_config)

        y = config.read(x)

        if len(y) == 0:

            print("#######################################")

            print("# FATAL:", os.path.basename(__file__))

            print("#", self.which_config, "not found or is not readable.")

            print("# This program was looking for:", x)

            print("#")

            print("# Ensure ini files exists in this directory:", os.getcwd())

            print("# ---> Does", self.which_config, "exist?")

            print("# ---> Is", self.which_config, "a readable file?")

            print("# Here is the output from attempted config file read:", y)

            print("# Aborting with no action taken.")

            print("#######################################")

            sys.exit(0)


        try:

            z = config.sections()

            print("#######################################")

            print("# INFO:", os.path.basename(__file__),"found config_reports.ini with these sections:", z)

            print()

            return z

        except:

            print("#######################################")

            print("ERROR:", os.path.basename(__file__))

            print("#Unable to parse config_reports.ini. ")

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

        q = (self.path + '\\' + self.which_config)

        try:

            config.read(q)

        except Exception as e:

            print("#######################################")

            print("FATAL:", os.path.basename(__file__))

            print("# Unable to config.read('config_reports.ini')")

            print("# in section run with config.read:", config.read('config_reports.ini'))

            print("# Aborting with no action taken.")

            print("#######################################")

            print(e)

            sys.exit(0)

        for item in ['CONFIG_HOURLY_TBL','CONFIG_DAILY_TBL','CONFIG_ROW1_COL_X_AXIS','CONFIG_ROW1_COL_Y_AXIS_1','CONFIG_ROW1_COL_Y_AXIS_2','CONFIG_ROW2_COL_X_AXIS','CONFIG_ROW2_COL_Y_AXIS_1','CONFIG_ROW2_COL_Y_AXIS_2','CONFIG_ROW3_COL_X_AXIS','CONFIG_ROW3_COL_Y_AXIS_1','CONFIG_ROW3_COL_Y_AXIS_2','CONFIG_ROW4_COL_X_AXIS','CONFIG_ROW4_COL_Y_AXIS_1','CONFIG_ROW4_COL_Y_AXIS_2']:

            try:

                config.get(myConfig, item)

            except Exception as e:

                print("# ERROR:", os.path.basename(__file__), "config_reports.ini", myConfig, "missing -->\t", item)

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

    a = ParseConfig('DB_SIZE', 'config_report2.ini')

    user, passwd  = a.read_config_admin_admin('.', 'config_admin.ini')

    print("config_admin.ini has user", user, "password", passwd)

    a.read_config_sections('.')

    CONFIG_ROW1_HOURLY_TBL, CONFIG_ROW1_DAILY_TBL, CONFIG_ROW1_COL_X_AXIS, CONFIG_ROW1_COL_Y_AXIS_1, CONFIG_ROW1_COL_Y_AXIS_2, CONFIG_ROW2_COL_X_AXIS, CONFIG_ROW2_COL_Y_AXIS_1, CONFIG_ROW2_COL_Y_AXIS_2, CONFIG_ROW3_COL_X_AXIS, CONFIG_ROW3_COL_Y_AXIS_1, CONFIG_ROW3_COL_Y_AXIS_2, CONFIG_ROW4_COL_X_AXIS, CONFIG_ROW4_COL_Y_AXIS_1, CONFIG_ROW4_COL_Y_AXIS_2 = a.run('.')

    print("==> Returning:", CONFIG_ROW1_HOURLY_TBL, CONFIG_ROW1_DAILY_TBL, CONFIG_ROW1_COL_X_AXIS, CONFIG_ROW1_COL_Y_AXIS_1, CONFIG_ROW1_COL_Y_AXIS_2, CONFIG_ROW2_COL_X_AXIS, CONFIG_ROW2_COL_Y_AXIS_1, CONFIG_ROW2_COL_Y_AXIS_2, CONFIG_ROW3_COL_X_AXIS, CONFIG_ROW3_COL_Y_AXIS_1, CONFIG_ROW3_COL_Y_AXIS_2, CONFIG_ROW4_COL_X_AXIS, CONFIG_ROW4_COL_Y_AXIS_1, CONFIG_ROW4_COL_Y_AXIS_2)







