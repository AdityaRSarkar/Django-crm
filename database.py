#Install Mysql on your computer 
#pip install mysql
#pip install mysql-connector-python
#pip install mysql-connector

import pymysql

db = pymysql.connect(
     host='localhost',
     user = 'root',
     password = 'psswrd123'  
    )

#prepare a cursor object
cO = db.cursor()
#Create a database
cO.execute("CREATE DATABASE MyProject2")
print("Database Created !")
