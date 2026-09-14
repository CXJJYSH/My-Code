const xhr = new XMLHttpRequest();

xhr.addEventListener("load", () => {
  console.log(xhr.response);
});
// Set up at first

xhr.open("GET", "https://supersimplebackend.dev");
// Type of HTTP message: GET, GET = get some information from the backend
// Types of requests: GET POST PUT DELETE

// Where to send this HTTP message

xhr.send();

// xhr.response;
// It takes time for the request to travel across the Internet
// Asynchronous code
