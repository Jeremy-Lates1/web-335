#
#    Title: lates_userpl.py
#    Author: Jeremy Lates
#    Date: 02/14/2024
#
#    Code is adapted from Professor Krasso Python Guide
#    Code is adapted from https://pymongo.readthedocs.io/en/stable/examples/tls.html

# Import the MongoClient
from pymongo import MongoClient
import datetime

#Connection string
conn = "mongodb+srv://web335_user:s3cret@bellevueuniversity.gxluysn.mongodb.net/web335DBretryWrites=true&w=majority"

#Create client
client = MongoClient(conn,tls=True,tlsAllowInvalidCertificates=True)

# configure a variable to access the web335DB
db = client['web335DB']

#Display all documents in the users collection
for user in db.users.find({}):
  print(user)

#Display a document where employeeId is 1011
print(db.users.find_one({"employeeId":"1011"}))

#Display a document where lastName is Mozart
print(db.users.find_one({"lastName":"Mozart"}))

