import os, sys

try:

    import configparser

except:

    os.system('pip install configparser')

    import configparser

try:

    import hashlib

except:

    os.system('pip install hashlib')

    import hashlib

try:

    import getpass

except:

    os.system('pip install getpass')

    import getpass

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

#logging_filename = str(os.path.basename(__file__) + '.log')

logging_filename = "igapa_master.py.log"

logging.basicConfig(filename = logging_filename, level=logging.INFO, filemode = 'a', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

#######################################
class ParseConfig:
#######################################
#-------------------------------------#
    def __init__(self, myconfig = 'DB_SIZE', which_config = 'config_reports.ini'):
#-------------------------------------#

        self.myconfig = myconfig

        self.which_config = which_config

        logging.info("#--------------------------------------#")

        logging.info("# Entering " + os.path.basename(__file__))

        logging.info("#--------------------------------------#")

        logging.info("# " + os.path.basename(__file__) + " Class ParseConfig received section heading: " + self.myconfig + " using this config file: " + self.which_config)

#-------------------------------------#
    def read_config_admin_admin(self, path = '.', config_admin = 'config_admin.ini'):
#-------------------------------------#

        self.path = path

        self.config_admin = config_admin

        logging.info("# " + os.path.basename(__file__) + " section read_config_admin_admin path: " + self.path + " using this config file: " + self.config_admin)

        print("# INFO:", os.path.basename(__file__), "section read_config_admin_admin path:", self.path, "using this config file:", self.config_admin)

        config = configparser.ConfigParser()

        x = (self.path + '/' + self.config_admin)

        y = config.read(x)

        if len(y) == 0:

            logging.error("#######################################")

            logging.error("# FATAL: " + os.path.basename(__file__))

            logging.error("# config_admin.ini not found or is not readable.")

            logging.error("# This program was looking for:", x)

            logging.error("#")

            logging.error("# Ensure config_admin.ini exists in this directory: " + os.getcwd())

            logging.error("# ---> Does config_admin.ini exist?")

            logging.error("# ---> Is config_admin.ini a readable file?")

            logging.error("# Here is the output from attempted config file read: " +  y)

            logging.error("# Aborting with no action taken.")

            logging.error("#######################################")

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

            if len(user) == 0 or len(passwd) == 0:

                user = input('Enter user name for JIRA access')

                print("You are logging in as user:", user)

                passwd  = getpass.getpass(prompt='Enter password, it will NOT be displayed ')


        except Exception as e:

            logging.error("#######################################")

            logging.error("# ERROR:", os.path.basename(__file__) + " config_admin.ini " + self.config_admin + " missing login credentials")

            logging.error("#######################################")

            logging.error(e, exc_info = True)

            print("#######################################")

            print("# ERROR:", os.path.basename(__file__), "config_admin.ini", self.config_admin, "missing login credentials")

            print("#######################################")

            user = input('Enter user name for JIRA access')

            print("You are logging in as user:", user)

            logging.info("# " + os.path.basename(__file__) + " Interactively received Jira user: " + user)

            passwd  = getpass.getpass(prompt='Enter password, it will NOT be displayed ')

        m = hashlib.sha256()

        b = bytes(passwd, 'utf-8')

        m.update(b)

        logging.info("# " + os.path.basename(__file__) + " is successfully returning user " + user + ' and encrypted passwd ' + str(m.hexdigest()))

        return (user, passwd)

#-------------------------------------#
    def read_config_admin_layout(self, path = '.', config_admin = 'config_admin.ini'):
#-------------------------------------#

        self.path = path

        self.config_admin = config_admin

        config = configparser.ConfigParser()

        x = (self.path + '/' + self.config_admin)

        y = config.read(x)

        if len(y) == 0:

            logging.error("#######################################")

            logging.error("# FATAL: " + os.path.basename(__file__))

            logging.error("# config_admin.ini not found or is not readable.")

            logging.error("# This program was looking for: " + x)

            logging.error("#")

            logging.error("# Ensure config_admin.ini exists in this directory: " + os.getcwd())

            logging.error("# ---> Does config_admin.ini exist?")

            logging.error("# ---> Is config_admin.ini a readable file?")

            logging.error("# Here is the output from attempted config file read: " +  y)

            logging.error("# Aborting with no action taken.")

            logging.error("#######################################")

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

            legend_font_size   = config.get('MASTER-LAYOUT', 'legend_font_size')

            legend_location    = config.get('MASTER-LAYOUT', 'legend_location')

            plotWidth          = config.get('MASTER-LAYOUT', 'plotWidth')

            plotHeight         = config.get('MASTER-LAYOUT', 'plotHeight')

            smallplotWidth     = config.get('MASTER-LAYOUT', 'smallplotWidth')

            smallplotHeight    = config.get('MASTER-LAYOUT', 'smallplotHeight')

            largeplotWidth     = config.get('MASTER-LAYOUT', 'largeplotWidth')

            largeplotHeight    = config.get('MASTER-LAYOUT', 'largeplotHeight')
   
        except Exception as e:

            logging.error("#######################################")

            logging.error("# " + os.path.basename(__file__) + " config_admin.ini " + self.config_admin + "")

            logging.error(e, exc_info = True)

            logging.error("#######################################")

            print("#######################################")

            print("# ERROR:", os.path.basename(__file__), "config_admin.ini", self.config_admin, "")

            pass_fail = False

            print("#######################################")

            print(e)

            sys.exit(0)

        return (legend_font_size, legend_location, plotWidth, plotHeight, smallplotWidth, smallplotHeight, largeplotWidth, largeplotHeight)

#-------------------------------------#
    def read_config_admin_reporting(self, path = '.', config_admin = 'config_admin.ini'):
#-------------------------------------#

        self.path = path

        self.config_admin = config_admin

        config = configparser.ConfigParser()

        x = (self.path + '/' + self.config_admin)

        y = config.read(x)

        if len(y) == 0:

            logging.error("#######################################")

            logging.error("# FATAL: " + os.path.basename(__file__))

            logging.error("# config_admin.ini not found or is not readable.")

            logging.error("# This program was looking for: " + x)

            logging.error("#")

            logging.error("# Ensure config_admin.ini exists in this directory: " + os.getcwd())

            logging.error("# ---> Does config_admin.ini exist?")

            logging.error("# ---> Is config_admin.ini a readable file?")

            logging.error("# Here is the output from attempted config file read: " +  y)

            logging.error("# Aborting with no action taken.")

            logging.error("#######################################")

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

            log_level   = config.get('REPORTING', 'log_level')

            outlier_threshold = config.get('REPORTING', 'outlier_threshold')

            return log_level, outlier_threshold

               
        except Exception as e:

            logging.error("#######################################")

            logging.error("# " + os.path.basename(__file__) + " config_admin.ini " + self.config_admin + "")

            logging.error(e, exc_info = True)

            logging.error("#######################################")

            print("#######################################")

            print("# ERROR:", os.path.basename(__file__), "config_admin.ini", self.config_admin, "")

            pass_fail = False

            print("#######################################")

            print(e)

            sys.exit(0)

#-------------------------------------#
    def read_config_sections(self, path = '.'):
#-------------------------------------#

        self.path = path

        config = configparser.ConfigParser()

        x = (self.path + '\\' + self.which_config)

        y = config.read(x)

        if len(y) == 0:

            logging.error("#######################################")

            logging.error("# " + os.path.basename(__file__))

            logging.error("# config file " + self.which_config + " not found or is not readable.")

            logging.error("# This program was looking for config file: " + x)

            logging.error("# Ensure ini files exists in this directory: " +  save_dir)

            logging.error("# ---> Does " +  self.which_config + " exist?")

            logging.error("# ---> Is " +  self.which_config + " a readable file?")

            logging.error("# Aborting with no action taken.")

            logging.error("#######################################")

            print("#######################################")

            print("# FATAL:", os.path.basename(__file__))

            print("#", self.which_config, "not found or is not readable.")

            print("# This program was looking for:", x)

            print("#")

            print("# Ensure ini files exists in this directory:", save_dir)

            print("# ---> Does", self.which_config, "exist?")

            print("# ---> Is", self.which_config, "a readable file?")

            #print("# Here is the output from attempted config file read:", y)

            print("# Aborting with no action taken.")

            print("#######################################")

            sys.exit(-1)


        try:

            z = config.sections()

            for item in z:

                logging.info("# " + os.path.basename(__file__) + " found " + self.which_config + " with these sections: " +  item)

            print("# INFO:", os.path.basename(__file__),"found " + self.which_config  + " with these sections:", z)

            return z

        except Exception as e:

            logging.error("#######################################")

            logging.error("# " + os.path.basename(__file__))

            logging.error("#Unable to parse config file " + self.which_config)

            logging.error("# Aborting with no action taken")

            logging.error(e, exc_info = True)

            logging.error("#######################################")

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

            logging.error("#######################################")

            logging.error("FATAL: " + os.path.basename(__file__))

            logging.error("# Unable to config.read " + self.which_config)

            logging.error("# in section run with config.read: " +  config.read(self.which_config))

            logging.error("# Aborting with no action taken.")

            logging.error(e, exc_info = True)

            logging.error("#######################################")

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

                logging.error("# " + os.path.basename(__file__) + " config_reports.ini " + myConfig + " missing -->\t" + item)

                print("# ERROR:", os.path.basename(__file__), "config_reports.ini", myConfig, "missing -->\t", item)

                pass_fail = False

        print("#######################################")

        if not pass_fail:

            quit(0)
                  
        logging.info("# " + os.path.basename(__file__) + " successfully exit.")

        logging.info(("#--------------------------------------#"))

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

    print("#######################################")

    print("# INFO:", os.path.basename(__file__))

    print("# --> is accessing ParseConfig with ParseConfig('DB_SIZE', 'config_reports.ini'")

    a = ParseConfig('DB_SIZE', 'config_reports.ini')

    user, passwd  = a.read_config_admin_admin('.', 'config_admin.ini')

    print("# INFO: config_admin.ini has section ADMIN user", user, "password", passwd)

    legend_font_size, legend_location, plotWidth, plotHeight, smallplotWidth, smallplotHeight, largeplotWidth, largeplotHeight = a.read_config_admin_layout('.', 'config_admin.ini')

    print("# INFO: config_admin.ini has section MASTER-LAYOUT with", legend_font_size, legend_location, plotWidth, plotHeight, smallplotWidth, smallplotHeight, largeplotWidth, largeplotHeight)

    log_level, outlier_threshold = a.read_config_admin_reporting('.', 'config_admin.ini')

    print("# INFO: config_admin.ini has section REPORTING with " + str(log_level) + " AND outlier_threshold of " + outlier_threshold)


    a.read_config_sections('.')

    CONFIG_ROW1_HOURLY_TBL, CONFIG_ROW1_DAILY_TBL, CONFIG_ROW1_COL_X_AXIS, CONFIG_ROW1_COL_Y_AXIS_1, CONFIG_ROW1_COL_Y_AXIS_2, CONFIG_ROW2_COL_X_AXIS, CONFIG_ROW2_COL_Y_AXIS_1, CONFIG_ROW2_COL_Y_AXIS_2, CONFIG_ROW3_COL_X_AXIS, CONFIG_ROW3_COL_Y_AXIS_1, CONFIG_ROW3_COL_Y_AXIS_2, CONFIG_ROW4_COL_X_AXIS, CONFIG_ROW4_COL_Y_AXIS_1, CONFIG_ROW4_COL_Y_AXIS_2 = a.run('.')

    print("==> Returning:", CONFIG_ROW1_HOURLY_TBL, CONFIG_ROW1_DAILY_TBL, CONFIG_ROW1_COL_X_AXIS, CONFIG_ROW1_COL_Y_AXIS_1, CONFIG_ROW1_COL_Y_AXIS_2, CONFIG_ROW2_COL_X_AXIS, CONFIG_ROW2_COL_Y_AXIS_1, CONFIG_ROW2_COL_Y_AXIS_2, CONFIG_ROW3_COL_X_AXIS, CONFIG_ROW3_COL_Y_AXIS_1, CONFIG_ROW3_COL_Y_AXIS_2, CONFIG_ROW4_COL_X_AXIS, CONFIG_ROW4_COL_Y_AXIS_1, CONFIG_ROW4_COL_Y_AXIS_2)

    logging.info("# " + os.path.basename(__file__) + " successfully exit.")

    logging.info("#--------------------------------------#")






