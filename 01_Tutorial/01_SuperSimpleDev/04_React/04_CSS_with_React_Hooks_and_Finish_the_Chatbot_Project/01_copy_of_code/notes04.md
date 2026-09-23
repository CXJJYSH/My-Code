**CSS Review**<br>
CSS = change the appearance of the website  
CSS with React = just use CSS normally

In React, we use className

- React is JavaScript code
- JavaScript already has a feature called class
- class is a reserved word

**Hooks = insert React features into our component**<br>
React.useState() is a hook  
State automatically updates the HTML when the data changes

Every hook starts with the word "use"

useEffect = run some code after the component is created or updated

In React

- Put hooks at the top of the component
- Hooks should not be inside anything

The array controls when useEffect runs  
[] = only run once, after the component is created.

[chatMessages] = run this function every time chatMessages changes

<u>Best Practice</u>
Give useEffect a dependency array to avoid running too often.

In React, we should not use the DOM manually.  
We should use React features to get this element.

useRef = automatically save an HTML element from the component.  
ref = container with special React features

**In this lesson:**

1. CSS with React
2. Styled the Chatbot Project
3. Flexbox = create a flexible layout
4. Ternary Operator (?:) = if-else statement directly in the JSX
5. hooks = insert React features into a component
6. useEffect = run code after component is created or updated
7. useRef = save an HTML element from the component
8. Created the auto-scroll feature

<!-- 2026.09.23 19:34 -->
