// backend/middleware/multer.js

const multer = require("multer");

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, "uploads");
  },
  filename: (req, file, cb) => {
    const ext = file.mimetype.split("/")[1];
    cb(null, `item-${file.fieldname}-${Date.now()}.${ext}`);
  },
});

exports.upload = multer({ storage });
