
def initial(username,passwd):
    import pymysql

    db = pymysql.connect(host='localhost',user=username,password=passwd)
    cur = db.cursor()

    sql = 'CREATE DATABASE  IF NOT EXISTS TWEET_DATA'
    cur.execute(sql)
    sql = 'USE  TWEET_DATA'
    cur.execute(sql)

    sql = 'CREATE TABLE IF NOT EXISTS USER(ID CHAR(20) PRIMARY KEY,SCREEN_NAME CHAR(20),PLACE CHAR(20),STATUS CHAR(20),DOB DATE)'
    cur.execute(sql)

    sql = 'CREATE TABLE IF NOT EXISTS TWEETS(ID CHAR(20),TID CHAR(20) UNIQUE,FOREIGN KEY(ID) REFERENCES USER(ID),PRIMARY KEY(ID,TID))'
    cur.execute(sql)

    sql = 'CREATE TABLE IF NOT EXISTS TWEET_INFO(TID CHAR(20), TEXT CHAR(145), FOREIGN KEY(TID) REFERENCES TWEETS(TID))'
    cur.execute(sql)

    sql = 'CREATE TABLE IF NOT EXISTS FOLLOWING(ID CHAR(20),FID CHAR(20) UNIQUE,FOREIGN KEY(ID) REFERENCES USER(ID),PRIMARY KEY(ID,FID))'
    cur.execute(sql)

    sql = 'CREATE TABLE IF NOT EXISTS INTERACTION(ID CHAR(20),TID CHAR(20),FOREIGN KEY(ID) REFERENCES USER(ID),PRIMARY KEY(ID,TID))'
    cur.execute(sql)





