//const http = require('http');
//const app = require('./app');

//const port = process.env.port || 3000;

//const server = http.createServer(app);

//server.listen(port);

//a simple server set up

var express = require('express'),
    app = express(),
    port = process.env.port || 3000,
    mongoose = require('mongoose'),
    Task = require('./api/models/todoListModel'),
    bodyParser = require('body-parser');

mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost/Tododb');

app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());
app.use(function(req, res){
    res.status(404).send({url: req.originalUrl + 'not found'})
});

var routes = require('./api/routes/todoListRoutes');
routes(app);

app.listen(port);

console.log('todo list RESTful API server started on: ' + port);
//http://localhost:27017