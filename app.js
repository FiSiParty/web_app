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
    response.sendFile(path.join(__dirname + '/page_main.html'));
});
app.post('/auth', function(request, response) {
    var fs = require("fs");
    var name = request.body.name;
    var ip = request.body.ip;
    var id = request.body.id;
    var register = request.body.register;
    var datatype = request.body.datatype;
    var readtype = request.body.readtype;
    var precision = request.body.precision;
    var topic = request.body.topic;
    request.session.name = name;
    request.session.topic = topic;

  
    fs.writeFile('input.txt', [
        name + "\n" +
        ip + "\n" +
        id + "\n" +
        register + "\n" +
        datatype + "\n" +
        readtype + "\n" +
        precision + "\n" +
        topic

    ], function(err) {
        if (err) {
            return console.log(err);
        }
        console.log("save");
    });
    
    response.redirect('/convert');

});

app.get('/convert', function(request, response) {
    
    
    response.sendFile(path.join(__dirname + '/public_mqtt.html'));
    const { PythonShell } = require("python-shell");
    var python_convert_input = 'convert.py';
    //var python_public_input = 'Public_to_mqtt.py';
    var pyshell_convert_in = new PythonShell(python_convert_input);
    //var pyshell_public_in = new PythonShell(python_public_input);

    pyshell_convert_in.on('message', function(message) {
        console.log(message);
    });
    pyshell_convert_in.end(function(err) {
        if (err) {
            throw err;
        };
        console.log('finished');
    });

    

   
});


app.get('/send_mqtt', function(request, response) {
    
    response.sendFile(path.join(__dirname + '/page_result.html'));
    const { PythonShell } = require("python-shell");
    var python_public_input = 'Public_input.py';
    var python_sub_input = 'sub_input.py';


    
    var pyshell_public_in = new PythonShell(python_public_input);
    var pyshell_sub_in = new PythonShell(python_sub_input);

    pyshell_public_in.on('message', function(message) {
       
        console.log(message);
    });

    
    pyshell_public_in.end(function(err) {
        if (err) {
            throw err;
        };

        console.log('finished');
    });
    
    pyshell_sub_in.on('message', function(message) {
       
        console.log(message);
    });

    
    pyshell_sub_in.end(function(err) {
        if (err) {
            throw err;
        };

        console.log('sub input');
    });
    

});


// app.get('/send_to_mqtt', function(request, response) {

    
//     const { PythonShell } = require("python-shell");
//     var myPythonScriptPath = 'convert.py';

    
//     var pyshell = new PythonShell(myPythonScriptPath);

//     pyshell.on('message', function(message) {
       
//         console.log(message);
//     });

    
//     pyshell.end(function(err) {
//         if (err) {
//             throw err;
//         };

//         console.log('finished');
//     });

    
//     response.send('Welcome back ' + request.session.topic + '!')
//     response.end();
// });

app.listen(1883);