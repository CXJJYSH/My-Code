**Automated Tests**<br>
Using code to test our app

More efficient than manual testing

NPM packages for automated testing:<br>

- Jest
- Vitest

**Vitest**<br>
`npm install --save-dev vitest`
`--save-dev` = only for development

**Type**<br>

1. Unit Test (for example, utils)
   = test 1 unit (or 1 piece) of the code

   it = create a test

   describe = groups tests together

   group of tests = test suite

2. Integration Test (for example, components)
   = test multiple units of code working together

   Testing a function: `expect(formatMoney(1999)).toBe('$19.99');`

   Testing a component: `render(<Product />);`

   render = display the component on the page

   I need to install some other npm packages to create an integration test.

   the command: `npm install --save-dev @testing-library/react@16.3.0 @testing-library/jest-dom@6.6.3 @testing-library/user-event@14.6.1 jsdom@26.1.0`

   jest-dom adds methods to expect()

   ```js
   expect().toBeInTheDocument();
   expect().toHaveAttribute();
   expect().toHaveTextContent();
   ```

   In our tests, we should not contact a real backend.
   Because the backend might not be available during tests.

   Mock = create a fake version of this function

   `vi.fn()` = creates a fake function that doesn't do anything (mock).

   screen = check the fake web page

3. Test User Interactions
   @testing-library/user-event lets us simulate events (like clicking a button)

   Test that our code runs `axios.post`.<br>
   Test if we gave `axios.post` the correct values.<br>

4. Mock the Implementation
   = make the mock do whatever we want

   For `<Link>` components to work, they need to be inside a Router.

   MemoryRouter = specifically for testing

   within() = lets us find things within a specific element

**Next Lesson: Deploying**<br>

**In this lesson:**<br>

1. Automated tests with Vitest
2. Unit test = test 1 piece of the code
3. it(), expect(), describe()
4. Integration tests = test multiple pieces of code
5. Test a commponent (using render and screen)
6. Mock = fake version of a function / package
7. Mock the implementation = make a mock do whatever we want
