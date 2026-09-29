**Generate the HTML using React**<br>

1. Save the data
2. Generate the HTML

**Add a Backend**<br>

1. What is a backend?
2. Why we use a backend?
   Backend = manages the data<br>
   Backend = share data between computers

<!--  -->

Website = Frontend

**Data Fetching**<br>
Data Fetching = get data from the backend (using our code)

Asynchronous code = code that does not finish right away

fetch() returns a Promise

Promise = lets us wait for asynchronous code to finish

request

response

.json() = gives us the data attached to the response

response.json() is also asynchronous

The backend can also run on the same computer as the frontend.

**axios**<br>
axios = cleaner way to make requests to the backend

Dependency Array = lets us control when useEffect runs

[] = only run once

**StrictMode**<br>
StrictMode runs useEffect() twice to help us catch bugs, and it only does this during development.

**Updater function**<br>

- lets us update the value
- regenerate the HTML

**URL Path**<br>
Whoever creates the backend decides what the URL Paths will be.

**API**<br>
API = Application Programming Interface

/api = these URL Paths are for interacting with the backend

**Older ESLint problems**<br>

```js
rules: {
'react/prop-types': 'off'
}
```

**`<base href="/" />`**
In index.html, `<base href="/" />` adds a "/" in front of any relative URLs.

For example, it can help us convert `images/products/shirt.png` to `/images/products/shirt.png`

**Lifting the State Up**<br>
Use it again.

**Query Parameter**<br>
`/api/cart-items?expand=product`

Query Parameter = lets us add additional info to our request

Backend does this thing.

Backend = manage the data (do calculations)
Frontend = present the data

**Separate our code into smaller components**<br>

Done.

**Async Await In React**<br>
= lets us write asynchronous code like normal code

The inner function in useEffect should not return a Promise.

useEffect should return nothing or a clean-up function, like this:<br>

```js
return () => {
  window.removeEventListener("scroll");
};
```

We need to create a new function when we use async await inside useEffect.
