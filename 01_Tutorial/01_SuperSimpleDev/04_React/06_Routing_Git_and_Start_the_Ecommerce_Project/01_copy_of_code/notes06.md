**Git Review**<br>
Git = helps us track changes in our code

.gitignore = tells git which files and folders to ignore (not to track changes)

In the real world we often work on an existing project, rather than a new project.

**Home Page**<br>
Web page = a single page

Website = group of web pages

**Components**<br>
Usually, we create a component for each page of the website.

**Routing**<br>
Routing = create multiple pages in React

Routing lets us create multiple pages using 1 HTML file.

This lets us reuse our HTML code.

Install react-router

`<Route>` = tells React all the pages that are in our website

To add a page to our website, we should add a component called Route.

Route = a page

`<Route>` = adds a page to our website

element = which element or component to display

**More details about Routing**<br>
Single Page Application (SPA)

= we only have 1 HTML file

= we use React to create multiple pages

**components and pages**<br>
Components: for shared components

Pages: for components that are specific for specific pages

**`<Link>`**
By default, link elements (`<a>`) reload the page.

`<Link>` = go to another page without reloading

```js
<Link to="">
```

When using react-router, use `<Link>` instead of `<a>`.

Because the `<Link>` component lets us go to another page without reloading.
