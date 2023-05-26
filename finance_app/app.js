// Import the necessary modules
const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");

// Create a new Express application
const app = express();

// Configure body parser
app.use(bodyParser.json());

// Connect to the database
mongoose.connect("mongodb://localhost/banking");

// Define the schema for the `accounts` collection
const AccountSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  balance: {
    type: Number,
    required: true,
  },
});

// Create the `accounts` collection
const Account = mongoose.model("Account", AccountSchema);

// Define the routes for the application
app.get("/", (req, res) => {
  // Get all of the accounts from the database
  Account.find({}, (err, accounts) => {
    if (err) {
      res.send(err);
    } else {
      res.json(accounts);
    }
  });
});

app.post("/transfer", (req, res) => {
  // Get the sender and recipient account numbers from the request body
  const senderAccountNumber = req.body.senderAccountNumber;
  const recipientAccountNumber = req.body.recipientAccountNumber;
  const amount = req.body.amount;

  // Check if the sender has enough money in their account
  Account.findOne({
    accountNumber: senderAccountNumber,
  }, (err, senderAccount) => {
    if (err) {
      res.send(err);
    } else if (senderAccount.balance < amount) {
      res.send("Insufficient funds");
    } else {
      // Update the sender's account balance
      senderAccount.balance -= amount;
      senderAccount.save();

      // Create a new transaction
      const transaction = new Account({
        accountNumber: recipientAccountNumber,
        balance: amount,
      });
      transaction.save();

      // Redirect the user to the home page
      res.redirect("/");
    }
  });
});

// Start the application
app.listen(3000, () => {
  console.log("Listening on port 3000");
});