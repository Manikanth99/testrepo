import logging
import os
import sys

logpath=os.getenv('logpath', ".")
filepath=logpath + os.path.sep+"output.log"
loglevel=os.getenv('loglevel', "INFO")


if loglevel=="DEBUG":
    # set up logging to file - see previous section for more details
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s:%(lineno)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=filepath,
                    filemode='w')
else:
    # set up logging to file - see previous section for more details
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(name)-12s:%(lineno)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=filepath,
                        filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
if loglevel=="DEBUG":
    console.setLevel(logging.DEBUG)
else:
    console.setLevel(logging.INFO)

# set a format which is simpler for console use
formatter = logging.Formatter('%(asctime)s %(name)-12s:%(lineno)s %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger().addHandler(console)



class Logger(object):

    @staticmethod
    def getLogger(classname):
        l=logging.getLogger(classname)
        return l