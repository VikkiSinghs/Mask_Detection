import psycopg2

DB_NAME = "iuwubbvc"
DB_USER = "iuwubbvc"
DB_PASS = "wJIkY9ANC0Pe2VWsocTrDCxoft1VSTtm"
DB_HOST = "isilo.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)
print("database connected successfully")

cur=conn.cursor()

cur.execute("INSERT INTO employee (ID,NAME,EMAIL) VALUES (1,'VIKRAM','abc@gmail.com')")
conn.commit()
print("DATA INSERTED SUCCESSFULLY")
conn.close()