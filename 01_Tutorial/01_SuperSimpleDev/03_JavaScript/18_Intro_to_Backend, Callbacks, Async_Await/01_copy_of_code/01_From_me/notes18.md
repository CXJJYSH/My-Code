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

**Promises**

- better way to handle asynchronous code
- similar to done() function
- let us wait for some asynchronous code to finish, before going to the next step

When we create a promise, it is going to run this function immediately.

resolve() lets us control when to go to the next step

**Why do we use Promises?**
Multple callbacks cause a lot of nesting.

For example: Let's say we want to load the cart from the backend.

If we have lots of callbacks, our code will become more and more nested.

Promises let us flatten our code

Use promises instead of callbacks.
Promises keep our code more flat.

**Features**

1. We can give resolve() a parameter.
2. We can run multiple promises at the same time.

**Promises.all()**

- lets us run multiple promises at the same time
- and wait for all of them to finish

**fetch**
fetch() = better way to make HTTP requests

fetch() uses Promises directly.

response.json() is asynchronous, it returns a promise.

<!-- 2026.09.14 16:51 -->

**Async Await**
= even better way to handle asynchronous code
