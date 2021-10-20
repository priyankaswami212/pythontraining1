import   mysql.connector

mydb =  mysql.connector.connect(
  host="rdsdb.ca4q3aqf6zpy.ap-southeast-1.rds.amazonaws.com",
  user="admin",
  password="Priyanka212",
  database="rdstraining"
)


mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Ganesh", "Banglore")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
print(myresult)
print("Name |  Address")
for x in myresult:
  print(x[0] +" | " + x[1])
  print(type(x))
mydb.close()
 