#THIS FILE IS ONLY FOR TESTING, DO NOT USE THIS
import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(
  host="localhost",
  user="root",
  password="msvcr100",
  database="iot"
)

# Create a cursor
cursor = cnx.cursor()

# Execute a query
query = "SELECT * FROM user_dup"
cursor.execute(query)

# Fetch all the rows
rows = cursor.fetchall()

# Loop through the rows
for row in rows:
  print(row[0])

print(rows[0][0].encode('utf8'))
# Clean up
cursor.close()
cnx.close()