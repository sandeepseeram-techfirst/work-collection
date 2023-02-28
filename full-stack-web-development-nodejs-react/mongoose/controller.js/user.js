// backend/controllers/user.js

const { User, validate } = require("../models/user");
const jwt = require("jsonwebtoken");
const bcrypt = require("bcrypt");

exports.signup = async (req, res) => {
  try {
    // Validate the user data
    const { error } = validate(req.body);
    if (error) return res.status(400).send(error.details[0].message);

    const { firstName, lastName, username, email, password } = req.body; // Get the user data

    // Check if the user exists in the database
    const oldUser = await User.findOne({ email });
    if (oldUser) {
      return res.status(409).send("User Already Exist. Please Login");
    }

    // Hash the password
    const salt = await bcrypt.genSalt(Number(process.env.SALT));
    const hashedPassword = await bcrypt.hash(password, salt);

    // Create an user object
    let user = await User.create({
      firstName,
      lastName,
      username,
      email: email.toLowerCase(),
      password: hashedPassword,
    });

    // Create the user token
    const token = jwt.sign(
      { userId: user._id, email },
      process.env.TOKEN_SECRET_KEY,
      {
        expiresIn: "2h",
      }
    );
    user.token = token;

    // Return the created user data
    res.status(201).json(user);
  } catch (err) {
    console.error(err);
  }
};