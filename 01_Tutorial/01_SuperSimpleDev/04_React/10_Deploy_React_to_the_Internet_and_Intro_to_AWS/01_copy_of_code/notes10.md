**Deploying**<br>
= how to put a React app on the Internet

**AWS (Amazon Web Services)**<br>
= a collection of services that help us put stuff on the Internet

**EC2**<br>
EC2 = rent a computer from AWS

<u>Infrastructure as a Service (Iaas)</u>

1 instance = 1 EC2 computer

EC2 just gives us a computer.  
We still need to:

1. Install NodeJS
2. Connect it to the Internet
3. Upload our code

**Elastic Beanstalk**<br>

1. Uses EC2 to rent a computer
2. Installs all the software we need

<u>Platform as a Service (PaaS)</u>

**Role**<br>
= gives Elastic BeacStalk permission to use other services in AWS

**Instance types**<br>
Size of the computer to rent from EC2

**Elastic Beanstalk is going to:**<br>

1. Rent a computer using EC2
2. Install NodeJS and npm
3. Connect it to the Internet

**Part**<br>

1. Backend
2. Frontend

Put the Backend on the Internet first.

We need to upload the code as a zip file.

`npm run build` minified (compressed) the code.

We can just reuse this backend computer.

We only need to set up one computer.
