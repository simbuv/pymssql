import pymssql
import os

REMOTE_SERVER_NAME    = os.environ.get("REMOTE_SERVER_NAME")
REMOTE_USERNAME = os.getenv("REMOTE_USERNAME")
REMOTE_PASSWORD  = os.getenv("REMOTE_PASSWORD")
REMOTE_DB_NAME  = os.getenv("REMOTE_DB_NAME")
REMOTE_DB_PORT  = os.getenv("REMOTE_DB_PORT")


#conn = pymssql.connect(REMOTE_SERVER_NAME+":"+str(REMOTE_DB_PORT), REMOTE_USERNAME, REMOTE_PASSWORD, REMOTE_DB_NAME)
  
def connect_with_pymssql():

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM City')
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()

    conn.close()

def insert_into_db():
    conn = pymssql.connect(REMOTE_SERVER_NAME+":"+str(REMOTE_DB_PORT), REMOTE_USERNAME, REMOTE_PASSWORD, REMOTE_DB_NAME)
    sql = "INSERT INTO City (cname,state)  VALUES ('Barry', 'Ontario')"

    cur = conn.cursor()
    cur.execute(sql)
    #cur.execute(sql, insert_obj)
    conn.commit()
    cur.execute("SELECT * FROM City")
 
    rows = cur.fetchall()
    
    print('rows count : '+str(len(rows)))
    
    if(len(rows) <= 0):
        print('No Data available')

    conn.close()

    connect_with_pymssql()
 

def startpy():
    print('Hey there')
    print(REMOTE_SERVER_NAME)

    #connect_with_pymssql()

    #insert_into_db()

    print('Done!')

if __name__ == '__main__':
    startpy()
