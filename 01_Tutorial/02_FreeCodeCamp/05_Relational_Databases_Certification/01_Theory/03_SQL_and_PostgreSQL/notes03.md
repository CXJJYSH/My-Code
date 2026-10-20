# Working with Relational Databases

## What Are Relational Databases, and How Do They Differ from Non-Relational Databases?

### What Is a Relational Database

A relational database is a collection of data organized into tables.

These tables are made of rows and columns.

Rows represent individual records. For example, if you're storing user data, each row could represent a specific user.

Columns represent the attributes or fields that describe each record. The table might include columns for common user attributes, such as name and national ID number.

One of the key characteristics of relational databases is that they allow us to connect different pieces of information by linking tables through common attributes, making it easier to see how they relate to each other.

Relational databases require a schema. The schema defines the overall structure of the database, including its tables, columns, data types, relationships, and constraints.

All tables in a relational database have a primary key, which is a unique identifier for each row. They enable relationships between tables via foreign keys. You'll learn more about primary keys, foreign keys, and how they work in the coming lessons. For now, just know they are fundamental to linking records across tables.

### An Example of a Relational Database

For example, let's say that you're creating a database for an organization that runs a wildlife conservation center for critically endangered animals.

One of the tables could store general information about the animals, you might call it animals. Each row could represent an animal, while each column could represent an attribute of that animal, like species, size, weight, age, and other unique characteristics.

To uniquely identify each animal, you would typically add an id column to the table. This would be the primary key of the table because it's unique for each animal. The ID of each animal could be used to link its record in this table to related records in other tables.

You could also have a species table to store information about each species, such as their habitat and conservation status. Each animal in the animals table could reference a species from this table using a species ID.

You could also create a table to store the veterinary records of the animals. This way, the center can track their health, treatments, and medications.

Once you have this general schema, you could link these tables to the animals table, which acts as the central point for animal-related data.

This way, you don't have to keep all the information about an animal in the same table. Instead, you can store related data in separate tables and link them through relationships. By creating these relationships, you can get the specific data you need with a single query.

### What Is a Query

A query is a request for specific data from the database. Examples of queries that you could make in the context of our example would be finding all animals that need a veterinary checkup, finding the most critically endangered species in the center, finding the number of animals who were born in captivity, and more. You can customize the queries to fit your needs.

### Applications of Relational Databases

Our example was related to wildlife conservation, but relational databases have a wide range of applications across industries such as healthcare, construction, business, gaming, education, government, e-commerce, social media, and more.

### Advantages of Relational Databases

They offer several advantages, including scalability. They can handle large datasets, so they're perfect for complex, real-world applications. They also enforce data integrity through primary keys, foreign keys, and data types, which ensures that the data will be consistent and accurate.

### Relational vs. Non-Relational Databases

In addition to relational databases, you can work with non-relational databases.

The main difference between relational and non-relational databases is how the data is stored. Non-relational databases, also known as NoSQL databases, are more flexible. They store data in individual files that are not connected. Their data model is more flexible too.

While some non-relational databases may have a basic schema or data model, it is often less rigid than the schema defined in relational databases. You can add, modify, or remove data fields if necessary.

The decision to use a relational or non-relational database depends on various factors, including the nature of the data and the specific requirements of the application. You should evaluate the tradeoffs between these two approaches to choose the best one for your application.

2026.10.19 21:44

## What Are Some Common Relational Databases, and How Do You Install and Use Postgres?

### Common Relational Databases

Some of the most common relational databases are MySQL, PostgreSQL, SQLite, and Microsoft SQL Server. Let's learn a little bit about each one of them.

MySQL is an open-source relational database management system. It's very popular for web development because it's easy to use, reliable, and efficient for building real-world applications. It also has an active community of developers that support and maintain it.

PostgreSQL is officially described as "The World's Most Advanced Open Source Relational Database." It's a free, open source object-relational database system known for its reliability, data integrity, and extensibility. For example, you can define your own data types, custom functions, and write code in different programming languages without re-compiling your database.

SQLite is a free, open source, and lightweight file-based SQL database engine. It's one of the most widely used database engines in the world. SQLite is self-contained and serverless. It's a zero-configuration database, which means that it doesn't require an initial setup process, which is great for getting started quickly.

These three databases are free and open source. There are other popular proprietary options too, including Microsoft SQL Server and Oracle database.

Microsoft SQL server is a popular relational database management system developed by Microsoft and used in various applications.

Oracle database is a scalable relational database management system often used for enterprise applications that require high performance.

### Installing PostgreSQL on Windows

### Using pgAdmin and psql

### Installing PostgreSQL on macOS with Homebrew

## What Is SQL, and How Can You Create a Database with Tables?

### What Is SQL?

SQL stands for Structured Query Language.
SQL = 结构化查询语言

SQL stands for Structured Query Language. It was developed in the 1970s, when it was initially known as the structured English query language (SEQUEL). This term was later shortened to SQL.

SQL is a programming language used for storing and managing data in relational databases.

### How Relational Databases Work

Like you learned in a previous lesson, relational databases organize data into tables. Each table has a set of rows and columns, where the data attributes and their relationships are represented. Each row represents a record while each column represents a specific attribute or field of that record.

### Using SQL in Relational Databases

With SQL, you can add, change, delete, find, and retrieve data from a relational database. It provides a comprehensive set of commands for querying, filtering, sorting, and aggregating data.

SQL can help optimize database performance, by querying only the necessary data, and it can be easily integrated with a wide range of programming languages, so you can use it to interact with databases directly from your applications.

It has been also adopted as an industry standard. It enforces data integrity and includes many security features, like support for user authentication and data encryption.

It's also scalable, portable, and compatible with a wide range of database management systems.

SQL is based on commands, commonly known as SQL statements or SQL queries.

### Executing SQL Commands

As a developer, you will write these statements using specific SQL language elements or keywords. They allow you to perform the necessary operations on your database.

Before you can enter SQL commands, you need to open the psql shell so you can directly interact with the PostgreSQL database. In the command prompt or terminal, enter:

```bash
psql -U <username> -d <database_name>

```

Replace username with your username and database_name with the database you want to connect to.

If you have not created your own database yet, PostgreSQL automatically includes a default database called postgres when it is installed. You can use this postgres database to follow along.

Once connected, you will see the prompt change to:

```text
postgres=#

```

It shows the database name you are connected to and waits for SQL commands.

Let's go over some of the most fundamental SQL commands that you should be familiar with. You'll notice that, by convention, SQL commands end with a semicolon (;).

### Creating and Connecting to a Database

First, you can use this command to create a database named my_database:

```sql
CREATE DATABASE my_database;

```

You can type CREATE followed by DATABASE, and the name of the database that you want to create. Notice that the SQL keywords of the command are written in capital letters.

Then, once you have your database, you can connect to it.

How you connect to the database really depends on the environment and tool you're using.

In the command prompt or terminal, you can use the method shown earlier. In the interactive psql shell, you can switch databases with the \c shortcut command followed by the database name like this:

```text
\c my_database

```

Note that the \c command and other shortcut commands (ones with a backslash in front of them) are part of the psql shell and not part of the SQL language itself, so they do not require a semi-colon to complete the command.

Now that you've connected to your new database, you will see the prompt has changed:

```text
my_database=#

```

### Creating a Table

Once you have created and connected to a database, you can create a table with the CREATE TABLE keywords:

```sql
CREATE TABLE products (
  id SERIAL,
  name VARCHAR(255));

```

In the command, you write CREATE TABLE, followed by the name of the table that you want to create. In this case, it will create a table named products.

Then, within parentheses, you write the names of the columns that the table should have and specify the data type of the values that will be stored in each column.

In the example, the table will have two columns, a column for the product ID and another one for the name of the product.

The standard naming convention for table and column names is snake case, writing words in lowercase and separating them with an underscore (\_). For example: delivery_orders

These are few essential SQL commands you should know to get started.

### Benefits of SQL

With SQL, you can easily query, manipulate, and analyze data to make informed decisions and solve real-world problems.

## What Are the Basic Data Types in SQL?

### Creating a Table in SQL

To define a table in SQL, you need to specify the data type of each column.

Remember that this is the basic syntax for creating a table in SQL. Each column has its own data type.

```sql
CREATE TABLE table_name(
    column1 data_type column_constraint,
    column2 data_type column_constraint,
    column3 data_type column_constraint,
    ... etc
);
```

### The Data Type Categories in SQL

As a developer, your goal is to choose these data types as accurately as possible.

There are six popular categories of data types in SQL:

Numeric, such as INTEGER, FLOAT, SERIAL, and DECIMAL.
Date and time, such as TIMESTAMP, DATE, and TIME.
Character and string. These include CHAR, VARCHAR, and TEXT.
Unicode, including NTEXT, and NVARCHAR. These are used to make sure that text will be stored and retrieved correctly, regardless of the characters' origin.
Binary, used to store non-textual data, like images, audio, and video files.
And other miscellaneous data types, such as XML and TABLE.
In this lesson, we'll cover some of the most widely used ones with PostgreSQL. Data types will vary across database management systems, but they are generally pretty similar. So you'll need to check the full list in the documentation.

### Numeric Values

We'll start with numeric values.

First, we have the INTEGER data type:

```sql
units_sold INTEGER

```

In this example, we assign this data type to a units_sold column.

INTEGER types consume 4 bytes in the database and can range in value from -2,147,483,648 to 2,147,483,647. The official PostgreSQL documentation describes it as the "typical choice for integer."

We also have SMALLINT and BIGINT, which are basically the same as INTEGER except have a smaller and bigger range of numbers, respectively, due to how much size they are allotted in the database.

A useful feature available in PostgreSQL is to create a column using the SERIAL keyword. Here, an id column is created using SERIAL:

```sql
id SERIAL

```

While it's not a true data type, it's very helpful for creating unique identifier columns because the column will have an INTEGER type, will not allow NULL values, and automatically increment when rows are added.

For example, the first row will automatically have an id of 1, the second row will have an id of 2, and so on, creating a unique ID for each record.

In MySQL, the equivalent of SERIAL would be the AUTO_INCREMENT attribute, used to generate sequential integers automatically:

```sql
id INT AUTO_INCREMENT

```

You can see that different database management systems may have different ways of achieving exactly the same functionality in your database.

### String Data Types

These are the most commonly used numeric data types, but sometimes, you may need to represent text or sequences of characters.

For this, you have the VARCHAR data type. This data type is used for a variable string length. You can set the maximum character length within parentheses:

```sql
name VARCHAR(50)

```

In this example, we define a name column, where the values can be up to 50 characters long.

This data type sets a maximum length for the strings, but if you need to store strings of any length, you can use TEXT instead:

```sql
name TEXT

```

### Dates and Times

In addition to numbers and strings, it's also common to store dates and times.

For example, if you create a table to store events, you may need to store the date of each event in a specific format. For this, you have the DATE data type:

```sql
event_date DATE

```

To store time, you can also use the TIME data type. For example, you may store the time when an event starts:

```sql
start_time TIME

```

The TIMESTAMP data type combines both of them. It includes both the date and time. It may also include the time zone if you write TIMESTAMP WITH TIME ZONE:

```sql
event_timestamp TIMESTAMP
event_timestamp TIMESTAMP WITH TIME ZONE

```

### The BOOLEAN Data Type

And finally, if you need to store a boolean value, TRUE or FALSE, you can use the BOOLEAN data type:

```sql
is_active BOOLEAN
```

Now you know some of the most common data types in SQL, but there are many more. You can check the documentation of your database management system to find more information about the data types that you can use.

## How Do You Insert and View Data in a Table?

### Inserting Data in a Table

First of all, to view data, you need to insert it. So we'll start with insertions.

The examples that we will cover in this lesson will be based on this table of dog records:

```sql
CREATE TABLE dogs(
  id SERIAL,
  name VARCHAR(100),
  age INTEGER);

```

The table will store the names and ages of various dogs.

If we assume that we are working with PostgreSQL, we can use the SERIAL data type for the id. Since id was created using SERIAL, its value will be an INTEGER, starting from 1, and incremented automatically when a new record is inserted. So you will not need to pass a value for it when you insert a record.

Let's start by inserting records to our dogs table with the INSERT INTO statement. There are many ways to do this. The first one would be inserting a single row and specifying the columns of the values that will be inserted.

You write INSERT INTO, followed by the name of the table (in this case, dogs), then the columns within parentheses, then VALUES, and their corresponding values within parentheses.

This is an example, we're inserting a dog record with the name of 'Gino', whose age is 3, remember that the id will be assigned automatically:

```sql
INSERT INTO dogs (name, age)
VALUES ('Gino', 3);

```

This is usually the safest option because you specify the columns explicitly, so the values will be assigned to those columns in order.

Notice that 'Gino' needs to be in single quotes because it is a VARCHAR type.

Another alternative is to insert the record without specifying the columns, like this:

```sql
INSERT INTO dogs
VALUES ('Gino', 3);

```

This syntax is valid SQL, but it is error-prone.

Since values are assigned based on column order, PostgreSQL will try to insert 'Gino' into the id column, which expects an integer. This results in an error such as invalid input syntax for type integer.

For this reason, it is safer to explicitly specify the column names when inserting data.

You can also insert multiple records in the same SQL command by separating them with a comma.

Here, we are inserting two dog records, one for 'Gino' and another one for 'Nora'.

```sql
INSERT INTO dogs (name, age)
VALUES
  ('Gino', 3),
  ('Nora', 2);

```

### Viewing Data in a Table

And just like you can insert records, you can query information from the database. In the context of databases, a query is a request for data.

In SQL, the SELECT statement is used for querying data from one or more tables. You can customize the query to get the exact information that you need.

If you need to query all the information from the dogs table, you just need to write SELECT, followed by an asterisk (\*), then FROM, and the name of the table, dogs:

```sql
SELECT *
FROM dogs;
```

In this command, the asterisk is a wildcard character that represents "all columns."

You will get all the data of all the records in the table:

```sql
 id | name | age
----+------+-----
  1 | Gino |   3
  2 | Nora |   2
```

To query specific columns, you can write the names of those columns in the command, right after SELECT, separated by a comma. In this example, we query the name and age columns of the dogs table:

```sql
SELECT name, age
FROM dogs;
```

The result will only include the name and age columns:

```sql
 name | age
------+-----
 Gino |   3
 Nora |   2
```

Sometimes, you might need to query data based on a specific condition. For example, to get all dogs who are less than 3 years old you can use the WHERE keyword and the less than (<) comparison operator:

```sql
SELECT *
FROM dogsWHERE age < 3;
```

The result will only include dogs whose age is less than 3:

```sql
 id | name | age
----+------+-----
  2 | Nora |   2
```

If you are just trying to find the age of 'Gino', you can use the equals (=) comparison operator:

```sql
SELECT age
FROM dogs
WHERE name = 'Gino';
```

And here's the result:

```sql
 age
-----
  3
```

These are common and simple ways to insert and view data in SQL, but there are many different options that you can choose from and some of them are more advanced. You'll learn about them in coming lessons.

2026.10.20 17:35
