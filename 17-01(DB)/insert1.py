import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="test"
)

mycursor = mydb.cursor()

machinery_id = input("Enter machinery ID: ")
name = input("Enter name of machinery: ")
production = input("Enter production produced: ")

# Insert the data into the student table
mycursor.execute("INSERT INTO student (id,name,production) VALUES (%s, %s, %s)", (machinery_id,name, production))

# Commit the changes to the database
mydb.commit()

print("Record inserted successfully.")
