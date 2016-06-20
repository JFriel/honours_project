const express = require('express');
const natural = require('natural');
const router = express.Router();



router.get('/', function(){
    res.send("hello!");
});
