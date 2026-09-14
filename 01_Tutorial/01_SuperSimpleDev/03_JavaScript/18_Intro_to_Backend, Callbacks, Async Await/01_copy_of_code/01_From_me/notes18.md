**Backend**

What is backend?
= another computer that manages the data of a website.

HTTP = HyperText Transfer Protocol

**XMLHttpRequest**

This is a built-in class(provided by JavaScript).

Creates a new HTTP message to send to the backen.

message = request

**URL**
= Uniform Resource Locator

- Like an address, but for the internet.
- Helps us locate another computer on the Internet.

https://amazon.com
http: protocol
s: secure
amazon.com: domain name

**Network Tab**

All the HTTP messages that are comming in and out of our computer.

**Terminology**

Request, Response
Request-Response Cycle = 1 request, 1 response

**URL Paths**
https://supersimplebackend.dev/hello

- /hello

https://supersimplebackend.dev/products/first

- /products/first

https://supersimplebackend.dev

- /

Each URL path will give us a different response.

A backend only supports a certain set of URL paths

If we send a request to a URL path that is not supported, the backend will respond with and error.

**Status Code**
Starts with 4 or 5 (400, 404, 500) = failed
Starts with 4 = Our problem
Starts with 5 = Backend's problem

Starts with 2 (200. 201. 204) = succeeded

**How do we know which URL paths are supported?**
Security problem
Som backends provide a documentation page

**List of URL paths**
= Backend API
API = application programming interface
interface = How we interact with something

**The backend can respond with different types of data**
Text
JSON
This allows us to send JavaScript objects across the Internet, to the backend.
HTML
Image

**When we type a URL in the browser, it actually sends a GET request.**
Using the browser = making a GET request

**Use a backend in our project**

**Callback**

回调函数

- a function to run in the future

setTimeout()里依旧有callback。

**Testing With a Backend**

done() lets us control when to go to the next step.
