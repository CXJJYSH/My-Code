**Data Mutation**<br>
update data in the backend

In the real world, we use the backend to update the data.

axios.get() = get data from the backend

axios.post(a, b) = create data in the backend

b is a request body.

**Rule of Hooks**<br>
We should not put hooks in a loop.

We should put hooks in the top of a component.

Seperate the loop into its own component.

**axios.port**<br>
Based on the URL Path, the backend can do different things.

`/api/products` = gives us the products

`/api/cart-items` = gives us the cart

Every request also has a Type.

`axios.get('/api/cart-items')` = sends GET and /api/cart-items

It sends 2 pieces of information:<br>

1. Type
2. URL Path

`axios.post('/api/cart-items')` = sends POST and /api/cart-items

This sends<br>

1. Type: POST (HTTP Method)
2. URL Path: /api/cart-items

When the backend receives our request, it looks at both the Type and the URL Path, to decide what to do.

4 common types of requests:<br>
GET = get some data<br>
POST = create some data<br>
PUT = update some data<br>
DELETE = delete some data<br>

Each request has a Type and a URL Path.<br>
Both of these determine what the backend will do.

**Dependency Array**<br>
`[value]` = whenever value changes, it will re-run useEffect
