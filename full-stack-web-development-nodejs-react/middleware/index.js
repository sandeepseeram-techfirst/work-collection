const auth = require("./middleware/auth");

app.post("/api/hello", auth, (req, res) => {
  res.status(200).send("Hello 🙌 ");
});