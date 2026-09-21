**What is React?**<br>

React = external library that helps us create websites easier.

React is an external library<br>

- It's a bunch of code that is outside our computer.
- We can load this code on our website and use it.

1. Creating a website with React feels natural
2. JSX lets us find errors easier.
3. We can insert values inside JSX elements -- using {}.

**Why are there 2 external libraries for React?**<br>

React can be used in different places

1. React = shared features
2. ReactDOM = features specific to websites

Using React to create websites:  
= load React & ReactDOM

Using React to create mobile apps:
= load React & ReactNative

**What is Babel?**<br>

Babel<br>
= JavaScript compiler
= translates other languages into JavaScript

When using React, we don't use normal JavaScript, we use an enhanced version of JavaScript -- JSX.

JSX = JavaScript XML = same as JavaScript, but we can write HTML directly in our JavaScript code.

XML = Extensible Markup Language

**How to use React**<br>

When using React, we use JSX instead of normal JavaScript.

Problem with JSX<br>

- Our web browser doesn't understand JSX
- Need to translate JSX into JavaScript

Babel = translates JSX into JavaScript

Minimum amount of code to set up React<br>

```js
<!DOCTYPE html>

<html>

<head>
    <title>React Basics</title>
</head>

<body>
    <div class="js-container"></div>

    <script src="https://unpkg.com/supersimpledev/react.js"></script>
    <script src="https://unpkg.com/supersimpledev/react-dom.js"></script>

    <script src="https://unpkg.com/supersimpledev/babel.js"></script>
    <script type="text/babel">
        const button = <button>hello</button>
        // Use the DOM:
        // const button = document.createElement('button');
        // button.innerHTML = 'hello';

        const container = document.querySelector('.js-container');
        ReactDOM.createRoot(container).render(button);
    </script>
</body>

</html>
```

**Use React to display multiple elements**><br>
Use `<div></div>`

**In this lesson:**<br>

1. React = external library that helps up create websites easier
2. Load the React external library
3. Set up React and use .render()
4. Reviewed basics of HTML and JavaScript
5. JSX = enhanced version of JavaScript
6. Created elements directly with JSX
7. Insert values into JSX elements
