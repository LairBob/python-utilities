
import logging


#%% Logging setup modules

def logSetup():
    myLogger = logging.getLogger("log_main")
    myLogger.setLevel(logging.INFO)
    
 
    # create the logging file handler
    fh = logging.FileHandler("log_main.log", mode="w")
 
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
 
    # add handler to logger object
    myLogger.addHandler(fh)
    return myLogger

 
myLogger = logSetup()