**Testing**

If I get an error, but my code looks correct, I may have some bad data saved in localStorage.

Try running:
localStorage.clear()

[object Object] problem:

1. Check my code, always JSON.stringify() before saving to localStorage.
2. localstorage.clear()
3. Refresh the page

Easiest way to test:
Open the website and try out the code.

Disadvantages of Manual Testing

1. Hard to test every situation
2. Hard to re-test

Automated Testing
= using code to test code

situation = test case

How many test cases should we have?

2 Types of Test Cases:

1. Basic test cases
   = tests if the code is working
2. Edge cases
   = test with values that are tricky

Try to test something different in each test case

Give each test a name

Group related tests together

group of related tests = test suite

**Testing Framework**

Testing Framework
= external library that helps us write tests easier

1. Create test suite
2. Create tests
3. Compare values and display result

The first testing framework I'm going to learn: Jasmine

Most testing frameworks are similar.
Other testing frameworks:
Jest (for ReactJS)
MochaJS
