#
#    Title: lates_userpl2.py
#    Author: Jeremy Lates
#    Date: 02/20/2024
#
#    Code is adapted from Professor Krasso Python Guide
#    Code is adapted from https://pymongo.readthedocs.io/en/stable/examples/tls.html
#    Code is adapted from https://www.w3schools.com/python/python_mongodb_update.asp
#    Code is adapted from https://www.geeksforgeeks.org/python-mongodb-update_one/



# Import the MongoClient
from pymongo import MongoClient
import datetime

#Connection string
conn = "mongodb+srv://web335_user:s3cret@bellevueuniversity.gxluysn.mongodb.net/web335DBretryWrites=true&w=majority"

#Create client
client = MongoClient(conn,tls=True,tlsAllowInvalidCertificates=True)

# configure a variable to access the web335DB
db = client['web335DB']

#Create a new user document 
db.users.insert_one({
  "firstName":"Jordan",
  "lastName":"Lates",
  "employeeId":"2011",
  "email": "lates2@email.com",
  "dateCreated" : datetime.datetime.now()
})

#Display the newly created document
print(db.users.find_one({"employeeId":"2011"}))

#Update the email address on newly created document
#Set the collection filter to get the document you want to update
filter = {"employeeId":"2011"}

#set the new values of the email address
new_values = {"$set":{"email":"laste3@email.com"}}

#Update the document
db.users.update_one(filter,new_values)

#Display the updated document with the new email address
print(db.users.find_one({"employeeId":"2011"}))

#Delete the newly created document
db.users.delete_one({"employeeId":"2011"})

#Prove that the newly created document was deleted
print(db.users.find_one({"employeeId":"2011"}))
