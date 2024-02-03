/* 
  Name: Jeremy Lates
  Date: 02/03/2024
  Code Attributions:  Professor Krasso class documentation 
*/

//Find all of the documents in users collection
db.users.find();

//Find composer with email address jbach@me.com
db.users.find({ email: "jbach@me.com" });

//Find composer with last name Mozart
db.users.find({ lastName: "Mozart" });

//Find composer with last name Mozart
db.users.find({ firstName: "Richard" });

//Find composer with employee id of
db.users.find({ employeeId: "1010" });
