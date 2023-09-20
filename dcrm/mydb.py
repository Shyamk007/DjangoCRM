import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Stark@1203"
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE dcrm")

print("All Done !")

# import mysql.connector

# # Connect to MySQL using the 'caching_sha2_password' plugin
# dataBase = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="Stark@1203",
#     auth_plugin='caching_sha2_password'
# )

# # Prepare a cursor object
# cursorObject = dataBase.cursor()

# # Change the authentication method for the 'root' user to 'mysql_native_password'
# cursorObject.execute("ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'Stark@1203';")

# # Commit the change
# dataBase.commit()

# # Close the connection with old authentication method
# dataBase.close()

# # Reconnect to MySQL with 'mysql_native_password' authentication
# dataBase = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="Stark@1203"
# )

# # Prepare a cursor object again
# cursorObject = dataBase.cursor()

# # Create the 'dcrm' database
# cursorObject.execute("CREATE DATABASE dcrm")

# print("All Done!")
