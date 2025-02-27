# ----------------------------------------------------------------------
# Database Basics with SQLite (`sqlite3` module)
# ----------------------------------------------------------------------
# SQLite is a lightweight, serverless, self-contained SQL database engine that 
# is built into Python via the `sqlite3` module. It allows you to work with 
# relational databases in a simple, file-based manner.

# In this section, we will explore how to:
# - Connect to a SQLite database
# - Perform basic CRUD operations (Create, Read, Update, Delete)
# - Write basic SQL queries to interact with the database.

import sqlite3

# ----------------------------------------------------------------------
# 1. Connecting to an SQLite Database
# ----------------------------------------------------------------------
# To interact with an SQLite database, we first need to connect to a database file.
# If the file doesn't exist, SQLite will create it for you.

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('example.db')  # This creates the 'example.db' file
cursor = connection.cursor()  # A cursor object is used to interact with the database

# ----------------------------------------------------------------------
# 2. Creating a Table (SQL Schema)
# ----------------------------------------------------------------------
# Before performing CRUD operations, we need to create a table to store the data.
# This involves writing SQL `CREATE TABLE` statements.

# SQL command to create a table named "users"
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT
)
''')
connection.commit()  # Commit the changes (save them to the database)

# ----------------------------------------------------------------------
# 3. CRUD Operations (Create, Read, Update, Delete)
# ----------------------------------------------------------------------

# a. Create - Inserting Data
# Inserting new records into the "users" table using SQL `INSERT` statement.
cursor.execute('''
INSERT INTO users (name, age, email) VALUES (?, ?, ?)
''', ("Alice", 30, "alice@example.com"))

cursor.execute('''
INSERT INTO users (name, age, email) VALUES (?, ?, ?)
''', ("Bob", 25, "bob@example.com"))

# Commit the changes
connection.commit()

# b. Read - Retrieving Data
# To fetch data from the database, use the SQL `SELECT` statement.
cursor.execute('SELECT * FROM users')  # Select all rows from the "users" table

# Fetch all rows of the query result
rows = cursor.fetchall()
for row in rows:
    print(row)  # Prints each row as a tuple (id, name, age, email)

# c. Update - Modifying Data
# Updating existing records using SQL `UPDATE` statement.
cursor.execute('''
UPDATE users SET age = ? WHERE name = ?
''', (35, "Alice"))

# Commit the changes
connection.commit()

# d. Delete - Removing Data
# Deleting a record using SQL `DELETE` statement.
cursor.execute('''
DELETE FROM users WHERE name = ?
''', ("Bob",))

# Commit the changes
connection.commit()

# ----------------------------------------------------------------------
# 4. Basic SQL Queries
# ----------------------------------------------------------------------

# a. Select Specific Columns
# You can select specific columns rather than all columns using `SELECT`.
cursor.execute('SELECT name, age FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)  # Prints name and age of users

# b. Filtering Results with `WHERE`
# You can filter results using the `WHERE` clause to match specific conditions.
cursor.execute('SELECT * FROM users WHERE age > ?', (30,))
rows = cursor.fetchall()
for row in rows:
    print(row)  # Prints users whose age is greater than 30

# c. Sorting Results with `ORDER BY`
# You can sort the results using `ORDER BY` clause.
cursor.execute('SELECT * FROM users ORDER BY age DESC')  # Order by age in descending order
rows = cursor.fetchall()
for row in rows:
    print(row)  # Prints users sorted by age in descending order

# d. Counting Rows with `COUNT()`
# You can count rows that match a condition using `COUNT()`.
cursor.execute('SELECT COUNT(*) FROM users WHERE age > ?', (30,))
count = cursor.fetchone()[0]
print(f"Number of users older than 30: {count}")

# ----------------------------------------------------------------------
# 5. Closing the Connection
# ----------------------------------------------------------------------
# Always close the connection to the database when you're done.
connection.close()

# ----------------------------------------------------------------------
# Summary of Basic SQL Queries:
# ----------------------------------------------------------------------
# - **CREATE**: Used to create tables and databases.
# - **INSERT**: Used to insert data into tables.
# - **SELECT**: Used to retrieve data from tables.
# - **UPDATE**: Used to modify existing data in tables.
# - **DELETE**: Used to remove data from tables.
# - **WHERE**: Used to filter records based on specific conditions.
# - **ORDER BY**: Used to sort query results by one or more columns.
# - **COUNT()**: Used to count the number of rows matching certain conditions.
