const jwt = require("jsonwebtoken");

const verify = (req, res, next) => {
  // Considering the possible 3 methods to pass the token
  const token =
    req.body.token || req.query.token || req.headers["x-access-token"];

  if (!token) {
    // If the token is not represented in any method, return an error
    return res.status(403).send("A token is required for authentication");
  }
  try {
    // decode the token, using the TOKEN_SECRET_KEY that we used to encode it, to get the user data
    const decoded = jwt.verify(token, process.env.TOKEN_SECRET_KEY);
    req.user = decoded;
  } catch (err) {
    // In case of failing to detect the token
    return res.status(401).send("Invalid Token");
  }
  // This is useful if you have much middleware, the next() function passes the request to the next middleware
  return next();
};

module.exports = verify;