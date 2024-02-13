/* 
  Name: Jeremy Lates
  Date: 02/03/2024
  Code Attributions:  Professor Krasso class documentation 
 
*/

//Find all of the documents in houses collection
db.houses.find();

//Find all of the documents in the students collections
db.students.find();

//Insert a student document to the student collection
lates = {
  firstName: "Jeremy",
  lastName: "Lates",
  studentId: "s2000",
  houseId: "h2000",
};
// Insert the documents.
db.students.insertOne(lates);

//Find lates document in the students collection
db.students.find({ lastName: "Lates" });

//Delete lates document from the students collection
db.students.deleteOne({ lastName: "Lates" });

//Find lates document in the students collection. Should not be there after deleteOne
db.students.find({ lastName: "Lates" });

//Find a list of students by house
db.students.aggregate([
  {
    $lookup: {
      from: "houses",
      localField: "houseId",
      foreignField: "houseId",
      as: "student_houses",
    },
  },
]);

//Find a list of students for the Gryffindor house
db.houses.aggregate([
  { $match: { founder: "Godric Gryffindor" } },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "gryffindor_students",
    },
  },
]);

//Find a list of students for the Eagle Mascot
db.houses.aggregate([
  { $match: { mascot: "Eagle" } },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "eagle_students",
    },
  },
]);
