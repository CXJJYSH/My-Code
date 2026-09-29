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
