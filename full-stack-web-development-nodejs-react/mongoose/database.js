// backend/database/database.js

const mongoose = require("mongoose");

const { MONGO_URI } = process.env;

exports.connect = () => {
  mongoose
    .connect(MONGO_URI)
    .then(() => {
      console.log("connected to database successfully...");
    })
    .catch((error) => {
      console.log(
        "failed to connect to the database. terminating the application..."
      );
      console.error(error);
      process.exit(1);
    });
};