const express = require("express");
const app = express();

const port = 3000;

app.get("/", (req, res) => {
  res.send({ message: "Hello, world!" });
});

app.get("/users", function (req, res) {
  res.send("users");
});

app.get("/users.birthday", function (req, res) {
  res.send("users.birthday");
});

app.get("/foe?o", function (req, res) {
  res.send("foe?o");
});

// The application recieves the requests on the port 3000
app.listen(port, () => {
  console.log(`App is listening on port ${port}!`);
});
