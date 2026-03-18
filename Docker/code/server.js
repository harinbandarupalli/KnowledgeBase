const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  res.end('<h1>Hello from Docker!</h1><p>This Node.js app is running inside a container.</p>');
});

server.listen(3000, () => {
  console.log('Server running on port 3000');
});
