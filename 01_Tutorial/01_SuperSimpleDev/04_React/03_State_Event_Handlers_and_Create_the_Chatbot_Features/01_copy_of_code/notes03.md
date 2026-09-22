**Use JavaScript to generate these components**<br>

1. Save the data, data = information
2. Generate the HTML
3. Make it interactive

key = helps React track changes in the array
key has to be unique

**Event Handlers**<br>
Event handler = run a function when we interact with the website

**State**<br>
State = data that is connected to the HTML
When we update this data, it will updata the HTML
State = save data that changes over time

**Convert chatMessages into state**<br>

1. The first value we get from React.useState is the current data.
2. The second value we get from React.useState is a function that updates the data.

In React, we should not update the data directly.
If we update the data directly, React will not update the HTML.
If we use this function to update the data, React will update the HTML.

In React, we should not modify the data directly.
We should always create a copy, and then modify the copy.
(This helps React be more efficient)

**Spread Operator**<br>
= takes the values in an array, and copies them into a new array.

**Array Destructuring**<br>

**How to get the text in a textbox**<br>
<u>React Best Practice</u><br>
Do not use the DOM manually(React is managing the website)
We should use React features to get the text from a textbox.

**Lifting the state up**<br>

1. Visualize the Components in our App, such as a component tree.
2. Lifting the state up = share state between multiple components

**Naming Convention**<br>
Use the same names.

**Controlled Inputs**<br>

State does not update immediately, it is updated after all of the code is finished.

**In this lesson:**<br>

1. Save the data (using arrays and objects)
2. Generate the HTML (using .map() and key prop)
3. Make it interactive, using onClick and onChange
4. State = data that changes over time, and is connected to the HTML
5. Updater function = update the state and update the HTML
6. Array Destructuring
7. Lifting the State Up = share state between components
8. Made <ChatInput> interactive
9. Got responses from the Chatbot
