#
#    Title: lates_hobbies.py
#    Author: Jeremy Lates
#    Date: 02/09/2024
#
#    Code is adapted from https://www.w3schools.com/python/python_lists_loop.asp
#    Code is adapted from https://www.w3schools.com/python/python_conditions.asp
#    Code is adapted from https://www.w3schools.com/python/python_lists.asp

#Create a list of 5 hobbies
hobbieslist = ["Rock Climbing","Flying Planes","Playing Basketball","Hiking","Playing Pool"]

#Loop through the hobbieslist and print to console window
for hobbie in hobbieslist:
  print(hobbie)

#Create a list of days (Sunday through Saturday)
dayslist = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

#Loop through days and if Saturday or Sunday then print I'm off and for weekdays print work day
for day in dayslist:
  if day == "Saturday" or day == "Sunday":
    print (day + " I am off. It is the weekend! Time to enjoy my hobbies.")
  else:
    print (day + " I am working today :(")

