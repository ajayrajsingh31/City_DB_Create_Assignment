import mysql.connector as msc
import json
def db_connect():
    with open("config.json") as fp:
        config=json.load(fp)
        conn=msc.connect(**config)
        cur=conn.cursor()
        return conn,cur