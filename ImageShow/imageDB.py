import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = "root",
    passwd = "ant904",
    database = "imageDB"
    #auth_plugin='mysql_native_password'
    )
myCursor = mydb.cursor()

#myCursor.execute("CREATE DATABASE imageDB")

myCursor.execute("CREATE TABLE ImagePath(Image_ID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(35),\
                Path VARCHAR(80))")
sql = "INSERT INTO ImagePath(Name, Path) VALUES(%s, %s)"
val = [
  ('mango tree',  "'F:\StudyMaterials\Python_pyQt5\Images\Green_Mango.jpg'"),
  ('single mango',  "'F:\StudyMaterials\Python_pyQt5\Images\Mango_Tree.jpg'"),
  ('sliced green mango',  "'F:\StudyMaterials\Python_pyQt5\Images\green_sliced.jpg'"),
  ('sliced ripe mango',  "'F:\StudyMaterials\Python_pyQt5\Images\ripe_sliced.JPG'")  
]

myCursor.executemany(sql, val)

mydb.commit()
print(myCursor.rowcount, "row was inserted.") 

myCursor.execute("SELECT * FROM ImagePath")

myresult = myCursor.fetchall()

for records in myresult:
  print(records)

myCursor.close()
mydb.close()
