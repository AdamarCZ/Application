from uuid import uuid4
from time import time
from os import remove, path, listdir
from sys import excepthook
import logging
import pip
try:
    from psutil import virtual_memory
except ImportError:
    pip.main(['install', "psutil"])  

logging.basicConfig(filename='log.log', level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

#Start case
class StartCase():
    def __init__(self):
        self.tc_id = uuid4()
        logging.debug("Case with id {} created!".format(self.tc_id))

#Test case 1
class caseOne(StartCase):
    def prep(self):
        if int(time()) % 2 != 0:
            logging.debug("System time is not divisible by 2!")
            return 0
        else:
            return 1

    def run(self):
        homeDir = path.expanduser("~")
        files = listdir(homeDir)
        logging.debug(files)

    def clean_up(self):
        pass

    def execute(self):
        try:
            logging.debug("Running caseOne!")
            if self.prep():
                self.run()
            self.clean_up()
            logging.debug("Finished caseOne!")
        except Exception as e:
            logging.error("Error has occurred in {}".format(self))

#Test case 2
class caseTwo(StartCase):
    def prep(self):
        if virtual_memory().total < 1073741824:
            logging.debug("Ram is not big enough!")
            return 0
        else:
            return 1

    def run(self):
        with open("test.txt", "w") as f:
            logging.debug("Creating test file!")
            line = "".join(str(uuid4()) for i in range(911))[:32768]
            f.write(line*32768)
            logging.debug("Test file created!")

    def clean_up(self):
        logging.debug("Removing test file!")
        remove("test.txt")
        logging.debug("Test file removed!")

    def execute(self):
        try:
            logging.debug("Running caseTwo!")
            if self.prep():
                self.run()
            self.clean_up()
            logging.debug("Finished caseTwo!")
        except Exception as e:
            logging.error(e)


case1 = caseOne()
case2 = caseTwo()

case1.execute()
case2.execute()
