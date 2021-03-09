import psycopg2

DB_NAME = "iuwubbvc"
DB_USER = "iuwubbvc"
DB_PASS = "wJIkY9ANC0Pe2VWsocTrDCxoft1VSTtm"
DB_HOST = "isilo.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)
print("database connected successfully")

cur=conn.cursor()

cur.execute("""
 CREATE TABLE employee(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,EMAIL TEXT NOT NULL)           

""")

conn.commit()
print("TABLE CREATED SUCCESSFULLY")
conn.close()
CREATE TABLE Inputs (id serial PRIMARY KEY,image text);