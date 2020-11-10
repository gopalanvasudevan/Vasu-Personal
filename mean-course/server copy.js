console.log('Default port no. is '+process.env.PORT);
console.log("Hello");

const http = require('http');
const app = require('./backend/app');

const port = process.env.PORT || 3000;
const server = http.createServer(app);
// const server = http.createServer((req,res) => {
//   res.end('This is my response');
// });
server.listen(port);

