External Libraries
= code that is outside of our project

Why we use external libraries

- let us share code
- save time
- avoid duplicating work

Hello external library: https://unpkg.com/supersimpledev@1.0.1/hello.js

DayJS external library: https://unpkg.com/dayjs@1.11.10/dayjs.min.js

To get these dates / Calculate delivery date:

1. Get today's date
2. Do calculations(Add 7 days, ...)
3. Display the date in easy-to-read format

DayJS external library

- Creates a function dayjs()
  On my computer, it will show my current date.

DayJS documentation(link in description)

<!-- 2026.09.02 23:33 -->

Best Practicee:
When we need something complicated,

- Try to find an external library first.
- Before writing the code ourselves.

How to find external libraries:

- Search in Google
- Use an AI tool

External Libraries + JavaScript Modules

The problem with script tags is that they run these code directly on the page, and this might cause naming conflicts.

Such as the hello() in Hello external library.

It is better to use JavaScript modules, because a module will contain the code inside a file, and any variables that created inside the file will not conflict with anything outside of the file.

Then we should use ESM Version of the external libraries.
ESM = EcmaScript Module
(EcmaScript = JavaScript)
A version that works with JavaScript Modules.

<!-- 2026.09.03 16:20 -->

Default Export

- another way of exporting
- we can use it when we only want to export 1 thing

Each file can only have 1 default export

It's up to me which version of export I want to use.

For some external libraries, we still have to use script tags.

<!-- 2026.09.03 16:28 -->
