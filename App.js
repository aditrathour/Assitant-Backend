// Import the Express module
const express = require('express');

// Create an Express application instance
const app = express();

// Define the port to listen on
const port = 3000; // You can choose any available port, common ones are 3000, 5000, 8080

// Define a basic route for the root URL ("/")
app.get('/', (req, res) => {
  res.send('Hello from Assitant-Backend (Node.js/Express)!');
});

// Start the server and listen for incoming requests
app.listen(port, () => {
  console.log(`Assitant-Backend server listening at http://localhost:${port}`);
});
