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

**How to Deploy React Without a Backend**<br>
If a React app does not have a backend, we can put the code on the Internet directly.

**Load Balancer**<br>

**Put the Database on a Separate Computer**<br>

**Instance class**<br>
Size of the computer running the database

**Set Up a Domain name**<br>
Short name that makes it easy to access our website.

1. Purchase a Domain Name
2. Set up the Domain Name in AWS  
   Route53 = manage domain names in AWS  
   Hosted Zone = lets us connect a domain name to our app

**Not secure**<br>
Our website is not using encryption.

**Make it secure**<br>
Set up an SSL certificate

HTTPS = Secure connection

DNS = Domain Name System

SSL = Secure Sockets Layer

**How to delete everything we created in AWS**<br>
Do the excecises first, before deletion.

**In this lesson:**<br>

1. AWS = collection of services that put stuff on the Internet
2. EC2 = rent computer from AWS (IaaS)
3. Elastic Beanstalk = sets up all the software (PaaS)
4. Put our backend on the Internet
5. Build and optimize the frontend, put it on the Internet
6. How to deploy React without a backend
7. Added a load balancer and database
8. Set up dommain name, SSL certificate, and HTTPS
