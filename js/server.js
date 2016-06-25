'use strict'
const express = require('express');
const natural = require('natural');
const routes = require('./app/routes/routes');
const generate = require('./app/handlers/getInfo')
const details = require('./app/handlers/handleDetails');
const HTML5Tokenizer = require('simple-html-tokenizer');
const app = express();


app.get('/', generate.generateText);
//app.get('/details',details.extract(generate.generateText) );

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
