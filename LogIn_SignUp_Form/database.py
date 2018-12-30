import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = "root",
    passwd = "ant904",
    database = "loginDB"
    #auth_plugin='mysql_native_password'
    )
myCursor = mydb.cursor()

#myCursor.execute("CREATE DATABASE loginDB")
#myCursor.execute("SHOW DATABASES")

#for db in myCursor:
  #  print(db)
#myCursor.execute("CREATE TABLE Users(Name VARCHAR(35), Username VARCHAR(15),\
                 #Email VARCHAR(35),Password VARCHAR(15))")

  
#myCursor.execute("ALTER TABLE Users ADD COLUMN Id INT AUTO_INCREMENT PRIMARY KEY")
#myCursor.execute("SHOW TABLES")

#for tables in myCursor:
    #print(tables)

'''
sql = "INSERT INTO Users(name, Username, Email, Password) VALUES(%s, %s, %s, %s)"
val = [
  ('tanvir', 'ant', "antanvir@gmail.com", 'ant904'),
  ('rezowan', 'rez1', "rez1@hotmail.com", 'rez933')
  
]

myCursor.executemany(sql, val)

mydb.commit()

print(myCursor.rowcount, "row was inserted.") '''

myCursor.execute("SELECT * FROM Users")

myresult = myCursor.fetchall()

for records in myresult:
  print(records)

myCursor.close()
mydb.close()
