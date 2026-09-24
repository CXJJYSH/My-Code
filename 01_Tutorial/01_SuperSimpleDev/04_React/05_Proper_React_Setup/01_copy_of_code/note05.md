**Command Line Review**<br>
mkdir = make directory  
Directory = a folder  
mkdir = creates a new folder

The command line runs inside a specific folder.  
pwd = print working directory

cd = change directory

**NodeJS Review**<br>
node = lets us run JavaScript code outside of a browser  
npm = node package manager  
package = external library  
npm = lets us install external libraries (or packages) into our project  
NPM contains millions of packages that we can download and use.  
<a>npmjs.com</a><br>

**Proper React Setup**<br>
Some packages also add a command to our command line.

Package create-vite adds a commmand create-vite to the command line.  
create-vite = helps us set up a new React project<br>

1. Install the create-vite package.
2. Run create-vite in the command line.

npx create-vite (x = execute)

@ = use a specific version of create-vite<br>

npm create vite = npx create-vite<br>

cd chatbot-project
npm install
npm run dev

In package.json, there is a list of all the packages needed for this project.  
npm install will install all of these packages.<br>

npm run dev = start up our new React website.<br>

public folder = contains files that should be available to the public.(we can access these using a URL)<br>

**Git**<br>
For the chatbot project, we're not going to use git.<br>

eslint = highlights problems in our JavaScript code.<br>

npm automatically updates package-lock.json<br>

Vite = tool that we used to set up this project.<br>

- Vite also helps us "build" the website.
- Vite also creates a server. (A server puts our website at a URL)
  - Vite Server also refreshes the website when we change some code.
  - Vite Server is a replacement for Live Server.

**Move our previosu Chatbot Project into this setup**<br>
<u>Best Practice</u>  
Load external libraries from node_modules instead of using a `<script>` tag.

rule = tells ESLint what to check for<br>

create new rule:  
"react/prop-types": "off",

**main.jsx**<br>
Sets up React

`<StrictMode>` = gives us some additional checks and warnings when developing our app

**A feature of Vite**<br>
Vite lets us import any type of file.

<u>Best Practice</u>  
Split up our CSS into different files.

<u>Advantage of This Setup</u><br>
We can separate our code into different files.

<u>Best Practice</u>  
Separate each component into its own file.

**JavaScript Modules Review**<br>
Vite adds .js or .jsx automatically.

**Separate the CSS so that each component has its own CSS file**<br>

**In this lesson:**<br>

1. Proper React Setup (using command line, npm, and Vite)
2. Command Line = give commands to our computer
3. NPM = download and use external libraries (or packages)
4. create-vite Package = helps us create a Proper React Setup
5. Moved our Chatbot Project into the new React Setup
6. ESLint = highlights problems in our JavaScript code
7. JavaScript Modules = separate our code into different files
8. Separated each component into its own .jsx and .css files
