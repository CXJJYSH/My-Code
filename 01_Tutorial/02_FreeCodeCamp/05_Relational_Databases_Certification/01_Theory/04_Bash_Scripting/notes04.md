# Understanding Bash Scripting

## What Is Bash Scripting, and What Are Some Advantages to Using It?

In previous lessons, you learned about Bash and some of the common commands you might use. But Bash supports a full scripting language, which you can use to perform more complex automated tasks.

Bash scripting involves writing a sequence of Bash commands in a file, which you can then execute with Bash to run the contents of the file.

### Example Bash Script

```bash
#!/bin/bash

servers=("prod" "dev")

for server in "${servers[@]}"
do
  echo "Pulling $server"
  rsync --archive --verbose $server:/etc/nginx/conf.d/server.conf configs/$server.conf
done
```

This script pulls NGINX configuration files from a list of remote servers, which can be useful for backing up those configs into a local repository. NGINX is a popular web server and you will learn more about working with servers in a future module.

#### The Shebang

The first line is called a "shebang" (#!) and tells the system which interpreter should be used to run the script. Common values here are /usr/bin/bash, /bin/bash, or /bin/sh.

#### The servers List

The next line, servers=("prod" "dev"), instantiates a list of strings representing the server names. "prod" is often used to refer to the production site, while "dev" refers to the development site, which is typically used for testing new features and changes before they are deployed to the live production environment.

#### The for Loop

Then, the list is iterated through with a for loop - the servers[@] syntax expands the list into individual elements. Each element is assigned to server with each iteration.

#### The Loop's Logical Block

The do statement indicates the beginning of the loop's logical block, or the code that should run with each iteration.

echo "Pulling $server" interpolates the current value of the server variable, which would be prod or dev in this case, and logs it to the terminal.

Then rsync is used to pull the actual file from the server and save it locally, using more interpolation to manage that command.

done indicates the end of the loop's logical block.

### Advantages of Bash Scripting

There are a number of significant advantages to understanding and leveraging Bash scripting.

#### Wide Availability

The first is that nearly every Unix environment comes with Bash readily available, which means you can run your script as-is without having to configure any language runtimes like Node.js or Python.

#### Access to Binary Applications

The second is that you have access to all of the binary applications available on the system with minimal effort. If your system has doctl installed, your script can execute that binary. A binary is a compiled program that the computer runs. When you have a bash script, you can execute the binary which will launch the program.

#### Testing in the Terminal

And finally, the syntax you use for your script is also executable directly in the terminal. This means that testing a small portion of your script becomes much less convoluted - you can copy and paste that portion directly into your terminal and see the result!

Understanding Bash will not only level up your scripting game, but will make you a wizard in the command line!

2026.10.22 21:45
