const mongoose = require ('mongoose');

//create schema
const postSchema = mongoose.Schema({
    title: {type : String, required : true},
    content: {type : String, required : true}
})

module.exports = mongoose.model('Post', postSchema);
