import logging

from DBConnection.dbconnect import db_connect as db
logging.basicConfig(filename='server.log',level=20,format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',datefmt='%d:%m:%Y')
logger=logging.getLogger("city_create.py")
def create_city(read):
    try:
        conn,cur=db()
        create_tables=[]
        for row in read:
            city=row['city']
            if city not in create_tables:
                create=f"create table {city}(id int,name varchar(30),sal int,city varchar(20))"
                cur.execute(create)
                create_tables.append(city)
                logger.info("{} table created successfully".format(city))
            insert=f"insert into {city} values({row['id']},'{row['name']}',{row['sal']},'{row['city']}')"
            cur.execute(insert)
            logger.info("{} Records Inserted Successfully".format(city))
        conn.commit()
        logger.info("All records have been successfully inserted into their respected city tables")
    except Exception as e:
        logging.exception(e)



