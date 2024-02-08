/* 
  Name: Jeremy Lates
  Date: 02/03/2024
  Code Attributions:  1) Professor Krasso class documentation 
                      2) MongoDB: The definitive Guide (Chodorow)
*/

//Add a new user to the users collection
lates = {
  firstName: "Jeremy",
  lastName: "Lates",
  employeeId: "2010",
  email: "lates@me.com",
  dateCreated: new Date(),
};
db.users.insertOne(lates);

//Update Mozart's email address to mozart@me.com
db.users.updateOne(
  { lastName: "Mozart" },
  { $set: { email: "mozart@me.com" } }
);

//List all documents in the users collection.  Use projection to only display firstName, lastName, and email
db.users.aggregate([{ $project: { firstName: 1, lastName: 1, email: 1 } }]);
