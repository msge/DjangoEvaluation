import mysql.connector

databases=mysql.connector.connect(
	host='localhost',
	user='root',
	password=''
	)
cursorObject=databases.cursor()
cursorObject.execute("Create Database evaluation")
print("All done!")