var express = require('express');
var session = require('express-session');
var path = require('path');
var bodyParser = require('body-parser');
const { spawn } = require('child_process');
const { json } = require('express');

var app = express();


app.use(session({
    secret: 'secret',
    resave: true,
    saveUninitialized: true

}));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.get('/', function(request, response) {
    response.sendFile(path.join(__dirname + '/index.html'));
});
app.post('/auth', function(request, response) {
    var fs = require("fs");
    var Name = request.body.Name;
    var IP = request.body.IP;
    var ID = request.body.ID;
    var Register = request.body.Register;
    var readtype = request.body.readtype;
    var precision = request.body.precision;
    var topic = request.body.topic;

    request.session.Name = Name;

    // let data = {
    //     email: email,
    //     username: username
    // }
    // let con = JSON.stringify(data);
    // fs.writeFileSync('seerii.json',con)
    fs.writeFile('test.txt', [
        Name + "\n" +
        IP + "\n" +
        ID + "\n" +
        Register + "\n" +
        readtype + "\n" +
        precision + "\n" +
        topic

    ], function(err) {
        if (err) {
            return console.log(err);
        }
        console.log("save");
    });


    // const writeInfile = require("write-ini-file")


    // writeInfile('foo.txt', {
    //     username:{
    //         email,
    //         username
    //     }

    // }).then( () => {
    //     console.log('done')
    // })




    response.redirect('/home');

});

app.get('/home', function(request, response) {

    const { PythonShell } = require("python-shell");
    var myPythonScriptPath = 'convert.py';

    // Use python shell
    // var PythonShell = require('python-shell');
    var pyshell = new PythonShell(myPythonScriptPath);

    pyshell.on('message', function(message) {
        // received a message sent from the Python script (a simple "print" statement)
        console.log(message);
    });

    // end the input stream and allow the process to exit
    pyshell.end(function(err) {
        if (err) {
            throw err;
        };

        console.log('finished');
    });



    response.send('Welcome back' + request.session.Name + '!')
    response.end();
});

app.listen(1883);