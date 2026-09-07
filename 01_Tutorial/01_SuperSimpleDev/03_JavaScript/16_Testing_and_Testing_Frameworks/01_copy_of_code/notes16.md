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

Run tests using Jasmine

Write tests using Jasmine

Test a different function using Jasmine

Match the folder structure of the code

Best Practicce:
Test each condition of an if-statement

Test Coverage
= how much of the code is being tested
(Try to maximize test coverage)

Flaky Test = test that sometimes passes and sometimes fails

**Mocks**
= lets us replace a method with a fake version

spyOn() records every time a method is used

1 mock only lasts for 1 test

How to create more complicated tests

Unit Tests = testing 1 piece of the code

Integration Test
= tests many units/pieces of code working together

2 things to test:

1. How the page looks
2. How the page behaves

In our tests, where does the cart get displayed?

Integration Test = tests many units/pieces of code working together

**Hooks**
= lets us run some code for each test

**Hooks in Jasmine**

beforeEach() = runs code before each test
afterEach() = runs code after each test
beforeAll() = runs code before all tests
afterAll() = runs code after all tests

**Process**

1. Make changes to code
2. Re-run the tests
3. Save to Git

**In this lesson:**

1. Manual and automated tests
2. Test cases and test suites
3. Testing Framework = helps us write tests easier
4. Mock and spy on methods
5. Test web pages using integration tests
6. Hooks
