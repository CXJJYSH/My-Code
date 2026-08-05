1. Put all imports at the top of the file.
2. We need to use live server.

Benefits of Modules:

1. Helps us avoid naming conflicts.
2. Don't have to worry about order of files.

Modules = better way to organize our code

Best practice:
Group related code together into its own file.

Another syntax of import:
`import * as cartModule from '../data/cart.js';`
`cartModule.cart;`
`cartModule.addToCart('id');`
cartModule is an object.
We can access each import as a property or a method.

Create the checkout page.
