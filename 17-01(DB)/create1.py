import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="1234",
	database="test"
)
# Test the connection
print(mydb.is_connected())  # Should print True if the connection is successful


mycursor = mydb.cursor()
mycursor.execute("create table factory(id int,name varchar(20),production int)")
print("table created")
mydb.commit()