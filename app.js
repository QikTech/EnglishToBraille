// Imported Decparations 
// console.log("heya");
const express = require("express");
const app = express();
const fs = require("fs");
const multer = require("multer");
const {TesseractWorker} = require('tesseract.js');
const worker = new TesseractWorker();


// CREATED STORAGE
const storage = multer.diskStorage({
     destination: (req,res,cb) => {
          cb(null, "./uploads");
     },
     filename: (req,res,cb)=>{
          cb(null, req.file);
     }
});


// SPECCIFIED UPLOADS
const upload = multer ({storage: storage}).single("avatar");
app.set("view engine", "ejs");


// ROUTES
app.get('/', (req,res) => {
     res.render('index');
})

// app.get('/uploads', (req, res)=>{
//      console.log('hey')
// })

//start up the server
const PORT = 5000 || process.env.PORT;
app.listen(PORT, () => console.log('Server running at ${PORT}'));