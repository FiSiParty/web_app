var express = require('express');
var session = require('express-session');
var path = require('path');
var bodyParser = require('body-parser');
const { json } = require('express');

var app = express();


app.use(session({
    secret: 'secret',
    resave : true,
    saveUninitialized: true

}));
app.use(bodyParser.urlencoded({ extended: true}));
app.use(bodyParser.json());

app.get('/',function(request, response){
    response.sendFile(path.join(__dirname + '/main.html'));
});
app.post('/auth', function(request, response){
    var fs = require("fs");
    var username = request.body.username;
    var email = request.body.email;
    
    request.session.username = username;

    // let data = {
    //     email: email,
    //     username: username
    // }
    // let con = JSON.stringify(data);
    // fs.writeFileSync('seerii.json',con)
    fs.writeFile('test.txt', [
        email + "\n" +
        username

    ], function(err){
        if(err){
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

app.get('/home', function(request, response){
    
    
    response.send('Welcome back' + request.session.username + '!' )
    response.end();
});

app.listen(1883);