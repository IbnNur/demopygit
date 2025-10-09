import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234")
cursor = mydb.cursor()

cursor.execute("show databases")

for i in cursor:
    print(i)


