var WebSocketServer = require('websocket').server;
var http = require('http');
//create a server
var server = http.createServer(function(request, response){
    console.log((new Date())+'Received request for'+
    Request.url);
    response.writeHead(404);
    response.end()
});

server.listen(8080,function(){
    console.log((new Date())+'Server is listening on port 8080')
});
//websocket server
wsServer = new WebSocketServer({
    httpServer:server
});

//webscoket connected
wsServer.on('request',function(request){
    var connection =request.accept(null,request.origin);
    console.log((new Date())+'connection accepted');
    connection.on('message',function(message){
        if (message.type === 'utf8'){
            console.log('received message'+
            message.utf8DAta);
            connection.sendUtf(message.utf8DAta);
        }else if(message.type==='binary'){
            console.log('received binary message of'+
            message.binartData.length+'bytes');
            connection.sendBytes(message.binaryData);
        }
    });
    connection.on ('close',function(reasonCode,
        description){
            console.log((new Data()) + 'Peer '+
            connection.remoteAddress + 'disconnected.');
        });
});