# ----------------------------------------------------------------------
# Advanced Databases in Python
# ----------------------------------------------------------------------
# 1. **SQLAlchemy**:
#    - Object Relational Mapper (ORM) for working with SQL databases.
#    - Allows you to define database schemas as Python classes and interact
#      with the database using Python code instead of raw SQL queries.

# 2. **MongoDB with pymongo**:
#    - A NoSQL database that stores data in JSON-like documents (flexible schema).
#    - Use `pymongo` to interact with MongoDB from Python.

# ----------------------------------------------------------------------
# 1. Object Relational Mappers (ORMs) with SQLAlchemy
# ----------------------------------------------------------------------
# Install SQLAlchemy: `pip install sqlalchemy`

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# a. Setting up the database
# Create a SQLite database (you can use other databases like MySQL or PostgreSQL)
DATABASE_URL = "sqlite:///example.db"
engine = create_engine(DATABASE_URL, echo=True)  # `echo=True` enables SQL query logging

# Create a base class for ORM models
Base = declarative_base()

# b. Defining a table using ORM
class User(Base):
    """A User table defined as an ORM model."""
    __tablename__ = 'users'  # Table name in the database

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, age={self.age}, email={self.email})"

# Create the table in the database
Base.metadata.create_all(engine)  # Creates the users table if it doesn't already exist

# c. Interacting with the database using a session
# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Add new users
new_user = User(name="Alice", age=30, email="alice@example.com")
session.add(new_user)  # Add a single user
session.add_all([  # Add multiple users
    User(name="Bob", age=25, email="bob@example.com"),
    User(name="Charlie", age=35, email="charlie@example.com")
])

# Commit the changes
session.commit()

# Query the database
users = session.query(User).all()  # Fetch all users
for user in users:
    print(user)  # Prints all user objects

# Update a user
user_to_update = session.query(User).filter_by(name="Alice").first()
if user_to_update:
    user_to_update.age = 31  # Update Alice's age
    session.commit()

# Delete a user
user_to_delete = session.query(User).filter_by(name="Charlie").first()
if user_to_delete:
    session.delete(user_to_delete)
    session.commit()

# ----------------------------------------------------------------------
# 2. Using NoSQL Databases (MongoDB with pymongo)
# ----------------------------------------------------------------------
# Install pymongo: `pip install pymongo`

from pymongo import MongoClient

# a. Connecting to MongoDB
# Connect to a MongoDB instance (ensure MongoDB is running)
client = MongoClient("mongodb://localhost:27017/")  # Default MongoDB URI

# Select a database (it will be created if it doesn't exist)
db = client["example_db"]

# Select a collection (equivalent to a table in SQL)
users_collection = db["users"]

# b. Inserting documents into the collection
# Insert a single document
users_collection.insert_one({"name": "Alice", "age": 30, "email": "alice@example.com"})

# Insert multiple documents
users_collection.insert_many([
    {"name": "Bob", "age": 25, "email": "bob@example.com"},
    {"name": "Charlie", "age": 35, "email": "charlie@example.com"}
])

# c. Querying documents
# Find all documents
all_users = users_collection.find()
for user in all_users:
    print(user)  # Prints each document as a dictionary

# Find a specific document
alice = users_collection.find_one({"name": "Alice"})
print(alice)  # Prints Alice's document

# d. Updating documents
# Update one document
users_collection.update_one({"name": "Alice"}, {"$set": {"age": 31}})  # Update Alice's age

# Update multiple documents
users_collection.update_many({}, {"$set": {"verified": True}})  # Add a "verified" field to all documents

# e. Deleting documents
# Delete one document
users_collection.delete_one({"name": "Charlie"})

# Delete all documents
users_collection.delete_many({})  # Deletes all documents in the collection

# ----------------------------------------------------------------------
# Summary: Choosing Between SQL and NoSQL
# ----------------------------------------------------------------------

# 1. **Relational Databases (SQL with SQLAlchemy)**:
#    - Use when you need strict schemas and relationships between tables.
#    - SQLAlchemy allows you to interact with SQL databases using Python objects.

# 2. **NoSQL Databases (MongoDB with pymongo)**:
#    - Use when your data is unstructured or schema flexibility is required.
#    - MongoDB stores data in JSON-like documents, making it ideal for hierarchical or varied data.

# Both approaches have their strengths. Choose based on your application's needs.
