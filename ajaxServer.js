
const express = require('express');
//child process
var spawn = require('child_process').spawn;
//const path =require('path');
const bodyParser = require('body-parser');
const app = express();
//app.use(bodyParser.urlencoded());
app.use(bodyParser.urlencoded({ extended: false }))
app.use(express.json())
//app.use(express.static(path.join(__dirname,'public')));
app.use(express.static(__dirname));

// app.get('/first',(req,res)=>{
//     res.header('Access-Control-Allow-Origin','*')
//     res.send('hello 111')
// });
//rooter post
app.post('/post',(req,res)=>{
    res.header('Access-Control-Allow-Origin','*')
    //get url and use MARS to analyse
    console.log(req.body)
    for (let val in req.body){
        //console.log(req.body[val])
        const process = spawn('python',['./GitImporter.py',req.body[val]])
        process.stdout.on('data',data=>{
        console.log(JSON.parse(data))
        var projet = '{"repos":'+data+'}'
        res.send(JSON.parse(projet));
        });
    }
    // var testProjet=
    // {"testProjetName":{
    //     "name":'testName',
    //     "WC":['testCode1','testCode2','testCode3'],
    //     "CD":['testCode1','testCode2'],
    //     "MS":['testCode1','testCode2']
    //     }
    // }
    // res.send(testProjet);
});

app.listen(process.env.PORT|3000);

//console.log('server start');