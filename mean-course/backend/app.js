const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const Post = require('./models/post');

const app = express();
const mongoDB = 'mongodb://127.0.0.1/admin';
//mongoose.connect("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")
mongoose.connect(mongoDB, { useNewUrlParser: true })
.then(()=>{
  console.log('Connected to database');
  console.log(mongoose.connection);
})
.catch(()=>{
  console.log('Connection to database failed');
});

//parses the JSON etc. that comes along with post request
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:false}));

//write the middleware functions

app.use((req,res,next)=>{
  //set header to allow CORS (Cross Origin Resource Sharing)
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
    );
  res.setHeader(
    "Access-Control-Allow-Methods",
    "GET, POST, PATCH, PUT, DELETE, OPTIONS"
    );
  next();
});

//Update the post to the DB
app.post("/api/posts",(req, res, next)=>{
  //const post = req.body;
  const post = new Post({
    title: req.body.title,
    content: req.body.content
  });
  console.log("The post being added is ", post);
  post.save().then(createdPost => {
    console.log("The added post is ", createdPost);
    res.status(201).json({
      message : 'Post added successfully',
      postId : createdPost._id
    })
  });
  //201 generally used for adding successfully a new resource
  //console.log('Response Status'+res.status);

});

//Delete the post from the DB
app.delete("/api/posts/:id",(req, res, next) => {
  console.log("Id for deletion is ",req.params.id);

  Post.deleteOne({ _id: req.params.id }).then(result => {
    console.log(result);
    res.status(200).json({
      message : 'Post deleted successfully'
    })
  });

});

//For updating/editing a given Post
app.put("/api/posts/:id", (req, res, next)=> {
  console.log('Inside app.put for editing the post');
  const post = new Post({
    _id: req.body.id,
    title: req.body.title,
    content: req.body.content
  });
  Post.updateOne({ _id: req.params.id }, post).then(result => {
    console.log(result);
    res.status(200).json({
      message : 'Post updated successfully'
    })
  });
});

//get the posts from DB
app.use("/api/posts",(req, res, next)=>{
  // const posts = [
  //   {
  //     id:'1',
  //     title:'1st post',
  //     content: '1st content'
  //   },
  //   {
  //     id:'2',
  //     title:'2nd post',
  //     content: '2nd content'
  //   }
  // ];
  Post.find().then(documents => {
    //console.log(documents);
    console.log('Getting records from DB');
    res.status(200).json({
      message: 'Posts fetched successfully',
      posts:documents
  });

  });
  //res.send();

  //res.send('Hello from Express!');
})

//export the app so that it becomes available to server.js
module.exports = app;
