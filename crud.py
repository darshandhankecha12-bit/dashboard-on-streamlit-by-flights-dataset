import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12345",
    )
    cursor = conn.cursor()  
    print("Connected to MySQL database")
except:
    print("Error connecting to MySQL database")
    exit()

cursor.execute("CREATE DATABASE IF NOT EXISTS indigo")
conn.commit()

cursor.execute("USE indigo")

cursor.execute('''CREATE TABLE IF NOT EXISTS AIRPORT(
    AIRPORT_ID INT PRIMARY KEY,
    CODE VARCHAR(10) NOT NULL,
    CITY VARCHAR(50) NOT NULL,
    NAME VARCHAR(255) NOT NULL
)
''')
conn.commit()

cursor.execute("""INSERT IGNORE INTO AIRPORT VALUES
(1,'DEL','NEW DELHI','IGIA'),
(2,'CCU','KOLKATA','NSCA'),
(3,'BOM','MUMBAI','CSMA')
""")
conn.commit()

cursor.execute("SELECT * FROM AIRPORT where airport_id > 1")
data = cursor.fetchall()
print(data)

for i in data:
    print(i[3])

