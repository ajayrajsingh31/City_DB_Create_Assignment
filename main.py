import csv
import shutil
from data_read.city_create import create_city
import logging
logging.basicConfig(filename='server.log',level=20,format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',datefmt='%d:%m:%Y')
logger=logging.getLogger("main.py")

def read_db(read):
    res=create_city(read)
    return res


def main():
    try:
        file="emp.csv"
        source="Source_Folder"
        destination="Processed_Folder"

        with open(source+"/"+file) as fp:
            read=csv.DictReader(fp)
            read_db(read)
        shutil.move(source+"/"+file,destination)
        logger.info("copied file from {} to {}".format(source+"/"+file,destination))
    except Exception as e:
        logger.exception(e)
if __name__=='__main__':
    main()
