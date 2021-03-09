import psycopg2

DB_NAME = "iuwubbvc"
DB_USER = "iuwubbvc"
DB_PASS = "wJIkY9ANC0Pe2VWsocTrDCxoft1VSTtm"
DB_HOST = "isilo.db.elephantsql.com"
DB_PORT = "5432"

try:
    conn = psycopg2.connect(database=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)
    print("database conected successfully")
    
except:
    print("database not connected")