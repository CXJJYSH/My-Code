Object-Oriented Programming (OOP)

- another style of programming(another way we write our code)

= organizing our code into objects

Procedural Programming
Procedure = a set of step-by-step instructions = a function

Object-Oriented Programming (OOP)
= organize our code into objects

Function inside an object
= method

Shorthand Method Syntax

**this**

**Why do we use Object-Oriented Programming?**

Object-Oriented Programming
= tries to represent the real world

intuitive

Easy to create multiple objects

**We're copy-pasting a lot of code**

Using a function to create multiple objects

**Naming convention in OOP**

Use PascalCase for things that generate objects

PascalCase = start every word with a capital

Create a function that generates objects

**An even better way to generate objects -- Classes**

Class = object generator

Instance

**Benefits of Classes**

A class looks like the object that it generates

Cleaner than using a function

Classes have extra features for OOP

1. Constructor = lets us run setup code
   Constructor lets us put this setup code inside the class

More details about constructor:

1. Has to be named "constructor
2. Should not return anything

class = better way to generate objects in object-oriented programming

**Private properties and methods**

Private = it can only be accessed inside the class

**Use classes in our project**

Converting an object into a class

Same obbject as before, but an enhanced version(It has some extra features from classes)

**.map()**
![.map()](<./images/map().png>)

**Inheritance**

Inheritance = lets us reuse code between classes

Parent class: Product
Child class: Clothing

When one class is a more specific type of another class, we use inheritance.

Add properties and mothods that are more specific

If we don't create a constructor, by default it will run the parents constructor so that's why when the child class was empty the code still worked.

Method overriding, polymorphism

**More details about classes**

1. How to test classes
   Testing classes is the same as normal tests.
2. Built-in classes
   Classes that are provided by the language
   new Date() = generates an object that represents the current date
3. More datails about "this"
   1. "this" lets an object access its own properties
   2. "this" can be used anywhere in our code
   3. Originally in JavaScript, this = window
      When they released JavaScript modules, inside a module, this = undefined.
   4. Use "this" inside a function
   5. Inside a function, we can change "this" to whatever we want.
   6. Arrow functions do not change the value of "this"
      "this" keeps the value that it had outside the arrow function
   7. Why are arrow functions designed this way?
      Arrow functions do not change the value of "this".
      To advoid accidentally overriding "this".

**Summary of "this"**

1. Inside a method, "this" points to the outer object
2. Inside a function, "this" = undefined. But we can change it.
3. Arrow functions, do not change the value of "this".
