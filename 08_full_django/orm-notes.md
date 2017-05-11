# ORM Notes:

## What is an ORM?
- Let's take a moment to get a better understanding of what an ORM does.

- ORMs are used to create a language-specific object oriented representation of a table. When tables are objects, attributes of these objects represent the columns in the database, while methods will correspond to common queries.

- If the terms methods and attributes don't sound familiar to you, go back and review that section from OOP.

- The reason that ORMs are useful is so that we can write pure Python code without having to manage long SQL query strings in our logic. You know from experience how ugly SQL queries can get when doing complex selects. Given clearly named table methods our code becomes much more clear and easy to read with the help of an ORM.

- Next, we'll get deeper into models and how they work before giving you the tools to try them out!
