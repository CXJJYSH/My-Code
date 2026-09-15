# **Backend**

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

# **Use a backend in our project**

## **Callback**

回调函数

- a function to run in the future

setTimeout()里依旧有callback。

**Testing With a Backend**

done() lets us control when to go to the next step.

## **Promises**

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

## **Async Await**

= even better way to handle asynchronous code

Async await is a shortcut for promises.

async = makes a function return a promise

async wraps the code in a promise

async = makes a function return a promise

**What's the point of this feature?**  
= async lets us use await
= lets us wait for a promise to finish, before going to the next line.

**await**<br>
= lets us write asynchronous code like normal code.

We can only use await, when we're inside an async function.

async await can only be used with promises, it doesn't do anything with a callback.

We can write asynchronous code like normal code.

**More details about async await**

1. We can only use await, inside an async function.
   The closest function has to be async.
2. We can save the resolve() result into a variable.
   ```javascript
   const value = await new Promise((resolve) => {
     loadCart(() => {
       resolve("value3");
     });
   });
   ```
3. We can use await with `Promise.all` as well.
4. Use async await over promises annd callbacks.

# **Error Handling**

When we're sending HTTP requests, we could get unexpected errors.

**Handle errors in callbacks**<br>

Set up a separate callback just for errors

**Handle errors in promises**<br>

Use .catch() method.

**Handle errors in async await**<br>

try / catch

**More details about try / catch**<br>

1. We can use try / catch with synchronous code (or normal code)
2. Whenever we get an error, it will skip the rest of the code.
3. Why don't we use try / catch everywhere?<br>

- it's meant to handle **unexpected** errors.(code is correct, outside our control)

4. We can manually create errors.

- In try / catch, we can use `throw "error1"`
- In promises, there are 2 ways to manually create an error.
  1. throw
  2. If we need to create an error in the future, then we need to use different code.
     throw does not work in the future.<br>
     **reject() is a function**
  - it lets us create an error in the future.

# **Now that we learn backend, promises, and async await, let's use them in our project.**

**We're gonna use the backend to create an order.**<br>

**Get the order**

4 types of requests

- GET = get something from the backend
  GET requests don't really let us send data to the backend.
- POST = create something
- PUT = update something
- DELETE = delete something

**Save the order**

localStorage

**After we create an order, go to the orders page**

window.location.href

**track.html**

URL Parameters  
= let us save data directly in the URL

URL parameters = search parameters

URL parameters lets us save different data in each URL
