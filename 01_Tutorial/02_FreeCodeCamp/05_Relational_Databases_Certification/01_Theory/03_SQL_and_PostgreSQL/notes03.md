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
FROM dogs
WHERE age < 3;
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

## What Are Primary and Foreign Keys in SQL, and How Do They Work?

### What Is a Primary Key?

Let's start with primary keys.

A primary key is a column or set of columns that uniquely identifies each record (row) in a table. This constraint ensures that no records in the table will have the same value for the primary key.

This is why a table can only have one primary key.

Values in the primary key column can't be NULL either, so they will always have a valid value.

In PostgreSQL, to make a column the primary key of your table, you just need to add PRIMARY KEY after the data type:

```sql
column_name data_type PRIMARY KEY

```

This is an example of a students table:

```sql
CREATE TABLE students (
  student_id SERIAL PRIMARY KEY,
  name VARCHAR(100));

```

Each student will have its own student_id, and this ID will be the primary key of the table. The SERIAL type is useful here because it ensures the student_id will always have a unique value.

A composite primary key is for when a table doesn't have a single unique column to identify the row. In this case, you can use a combination of two or more columns as the primary key that, together, are unique.

To do this, denote which columns are the composite primary key when you create the table like this:

```sql
CREATE TABLE table_name (
  column1 data_type column_constraint,
  column2 data_type column_constraint,
  column3 data_type column_constraint,
  ...
  PRIMARY KEY (column1, column2));

```

Imagine you have a table with student_id and course_id columns that tells you what students are enrolled in various classes.

Each student will be enrolled in several classes, and each class will have several students enrolled in it. So neither column is unique - but you will never have the same student enrolled in the same class more than once. So you can use the combination of the two columns as the primary key:

```sql
CREATE TABLE course_enrollments (
  student_id INT,
  course_id INT,
  ...
  PRIMARY KEY (student_id, course_id),);

```

Primary keys are essential for ensuring data uniqueness and integrity, for optimizing data retrieval, and for establishing relationships with other tables in a relational database.

### What Is a Foreign Key?

That takes us to the next type of key that we will cover in this lesson: foreign keys.

A foreign key is a column (or set of columns) in a table that references the primary key of another table. A table can have multiple foreign keys.

In this example, we have two tables, customers, and orders:

```sql
CREATE TABLE customers (
  customer_id SERIAL PRIMARY KEY,
  first_name VARCHAR(100) NOT NULL,
  ...
);

CREATE TABLE orders (
  order_id SERIAL PRIMARY KEY,
  customer_id INTEGER,
  ...
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

```

The primary key of the customers table is customer_id and the primary key of the orders table is order_id.

But notice that there is also a customer_id column in the orders table.

Why are we storing customer information in the orders table?

We do this to create a relationship between the customers and orders tables. Each order will store the ID of the customer who submitted it.

To create the relationship between the tables, we will make the customer_id column in the orders table a foreign key that references the customer_id column in the customers table:

```sql
FOREIGN KEY (customer_id) REFERENCES customers(customer_id)

```

Values in a foreign key column must either match the primary key values in the referenced table or be NULL (if the foreign key allows NULLs).

Why is this helpful?

By making sure that these columns in both tables match exactly, foreign and primary keys prevent the creation of "orphaned" records, records that refer to a non-existent record in another table.

### Why Primary Keys and Foreign Keys Matter

Primary and foreign keys are fundamental for relational databases. They power the "relational" aspect of these databases, allowing you to model real-world data in an accurate way.

## What Are the Different Types of Relationships in a Relational Database?

### The Main Types of Relationships

The "relational" aspect of "relational databases" comes from the fact that records in different tables can have different types of relationships.

There are five main types of relations:

- one-to-one
- one-to-many
- many-to-one
- many-to-many
- And self-referencing relationships (also known as recursive relationships).

### One-to-One Relationships

Two tables have a one-to-one relationship when each record in the first table can be associated with at most one record in the second table, and vice versa.

For example, let's say a company only assigns one vehicle per employee.

In that case, the database could have an employees table and a vehicles table, where each employee record corresponds to one, and only one, vehicle record in the database.

### One-to-Many and Many-to-One Relationships

In contrast, one-to-many relationships occur when one record in a table can be related to one or more records in another table.

For example, if we have a customers table and an orders table, each customer could be related to one or more orders but each order can only be related to one customer.

This is the same as the many-to-one relation, but from the opposite perspective. One or more orders can be related to one customer.

### Many-to-Many Relationships

Many-to-many relationships occur when a record in a table can be related to multiple records in another table and vice versa.

For example, let's analyze a database for a library. For simplicity purposes, let's assume that this database only has two tables: books and authors.

An author can write multiple books, and a single book can be written by multiple authors.

Implementing this type of relationship is a little bit more complex because the relational model at its core doesn't support many-to-many relationships directly.

To handle this, you would usually create an intermediate table, also known as a junction table.

This table solves these initial limitations by transforming the many-to-many relationship into two one-to-many relationships.

It creates a one-to-many relationship between the first table and the junction table and a one-to-many relationship between the second table and the junction table.

The name of the junction table is usually a combination of the entities. In the context of our example of books and authors, you may call it books_authors.

In the junction table itself, you would associate the authors and their books by creating two columns: a column for the author's id (author_id) and another column for the book's id (book_id).

These would be foreign keys referencing their corresponding primary keys in the authors and books tables, respectively.

With this junction table, you'll be able to query all the authors of a given book or all books written by a given author.

Using a junction table makes it easier to query the data, prevents redundancy, and simplifies the database schema. They are very helpful for implementing many-to-many relationships.

### Self-Referencing Relationships

And finally, we find self-referencing relationships, which occur when the records of a table can be related to other records on the same table. This is also known as a recursive relationship.

Understanding these relationships is essential for designing and modeling complex and efficient relational databases.

## What Are the Different Ways to Join Tables?

### Why SQL's JOIN Matters

Even though relational databases organize data into separate tables, SQL's JOIN operations allow you to combine related information from tables to query data.

### Different Variants of the JOIN Operation

There are several variants of the JOIN operation, including:

- INNER JOIN
- FULL OUTER JOIN
- LEFT OUTER JOIN
- RIGHT OUTER JOIN
- SELF JOIN
- CROSS JOIN

### The INNER JOIN Operation

An INNER JOIN filters the result to include only rows where the values in the joining columns that you specify are equal in both tables. Basically, it gives you the intersection of the data.

### The FULL OUTER JOIN Operation

If a match is found in the specified columns, the data is combined and you get all columns for each matching record.

If there's no match in the specified columns, in either one of the tables, the missing columns are filled with NULL values.

如果在指定的列中找到匹配，数据将被合并，你将获得每个匹配记录的所有列。

如果在任一表格的指定列中没有匹配，则缺失的列将填充为 NULL 值。

### LEFT OUTER JOIN Operation

A LEFT OUTER JOIN is used to get all the records from the left table and the matching information from the right table for each row of the left table.

If no match is found, the columns from the right table are filled in with NULL values.

LEFT OUTER JOIN 用于获取左表的所有记录以及左表每一行对应的右表匹配信息。

如果未找到匹配，则右表的列将填充为 NULL 值。

### The RIGHT OUTER JOIN Operation

A RIGHT OUTER JOIN is very similar, but now we get all the records from the right table and the matching information from the left table for each row of the right table.

If there's no match, the columns from the left table are filled in with NULL values.

### The SELF JOIN Operation

A SELF JOIN allows you to join the table with itself. You can think of it as joining two copies of the same table. This is helpful for comparing different rows within the same table.

SELF JOIN 允许你将表格与其自身连接。你可以将其视为连接同一表格的两个副本。这对于比较同一表格中的不同行非常有用。

### The CROSS JOIN Operation

A CROSS JOIN, also known as a Cartesian Join, joins every row from the first table with every row of the second table. Therefore, it generates all possible row combinations. This operation doesn't need any conditions to join the tables.

CROSS JOIN，也称为笛卡尔连接，将第一个表格的每一行与第二个表格的每一行连接。因此，它生成所有可能的行组合。此操作不需要任何条件来连接表格。

### Why Use JOIN Operations

These JOIN operations are fundamental for working with SQL. By choosing the right one, you can query the data you need as efficiently as possible.

### Examples for SELF JOIN operation and CROSS JOIN operation

#### 1. SELF JOIN（自连接）

**例子：查询每个员工及其直属上级的姓名。**

假设有一张 `employees` 表：

| employee_id | name | manager_id |
| ----------: | ---- | ---------: |
|           1 | 张三 |       NULL |
|           2 | 李四 |          1 |
|           3 | 王五 |          1 |
|           4 | 赵六 |          2 |

其中，`manager_id` 表示直属上级的员工编号。

SQL：

    SELECT
        e.name AS employee,
        m.name AS manager
    FROM employees AS e
    LEFT JOIN employees AS m
        ON e.manager_id = m.employee_id;

查询结果：

| employee | manager |
| -------- | ------- |
| 张三     | NULL    |
| 李四     | 张三    |
| 王五     | 张三    |
| 赵六     | 李四    |

**原理：** 将同一张 `employees` 表当作两张表使用：

- `e`：员工表
- `m`：上级表

通过 `e.manager_id = m.employee_id`，找到每个员工对应的上级。

SELF JOIN 的典型用途就是查询同一张表中记录之间的关系，例如员工与上级、商品与其替代商品等。

#### 2. CROSS JOIN（交叉连接）

**例子：查询所有颜色和所有尺码的组合。**

假设有两张表：

`colors`

| color |
| ----- |
| 红色  |
| 蓝色  |

`sizes`

| size |
| ---- |
| S    |
| M    |
| L    |

SQL：

    SELECT
        colors.color,
        sizes.size
    FROM colors
    CROSS JOIN sizes;

查询结果：

| color | size |
| ----- | ---- |
| 红色  | S    |
| 红色  | M    |
| 红色  | L    |
| 蓝色  | S    |
| 蓝色  | M    |
| 蓝色  | L    |

**原理：** 将第一张表的每一行与第二张表的每一行进行组合。

如果第一张表有 2 行，第二张表有 3 行，那么结果就有：

$$
2 \times 3 = 6 \text{ 行}
$$

CROSS JOIN 的典型用途是生成所有可能的组合，例如商品颜色与尺码的搭配。

---

**核心区别：**

| 对比             | SELF JOIN          | CROSS JOIN               |
| ---------------- | ------------------ | ------------------------ |
| 含义             | 同一张表与自身连接 | 两张表进行交叉组合       |
| 是否需要连接条件 | 通常需要           | 不需要                   |
| 结果             | 取决于连接条件     | 每行与另一张表的每行组合 |

2026.10.21 18:14

# Build a Database of Video Game Characters

```sql
SELECT * FROM character_actions
FULL JOIN characters ON character_actions.character_id=characters.character_id
FULL JOIN actions ON character_actions.action_id=actions.action_id;
```

2026.10.22 16:46
