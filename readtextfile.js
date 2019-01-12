var http = require('http');
var fs = require('fs');
var server = http.createServer(function (req, resp) {
        fs.readFile("customerdata.txt", function (error, data) {
            if (error) {
                resp.writeHead(404);
                resp.write('Contents you are looking are Not Found');
            } else {
                resp.writeHead(200, { 'Content-Type': 'text/html' });
                data= data.toString();
                var words = data.split(/\r?\n/);
                words = words.map(function (word) { return word.trim() });
                words = words.filter(function (word) { return word.length > 0 });
                console.log(JSON.stringify(words));
                resp.write(JSON.stringify(words));
            }
             
            resp.end();
        });
});
//5.
server.listen(5050);
console.log('Server Started listening on 5050');