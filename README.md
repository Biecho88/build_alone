<h1 align="center">Build Alone</h1>

[View the live project here.](https://build-alone-782f5267ecce.herokuapp.com/)

<h2 align="center"><img src="https://i.ibb.co/7n9G9Zx/Main-page.png"  alt="Database_schema" border="0"></h2>

# Welcome to our Build Alone Website!

#### Welcome to ExcavateRents, your premier destination for hassle-free construction machinery rentals, specializing in excavators. Whether you're a seasoned contractor or a DIY enthusiast tackling a home project, we've got you covered with a vast selection of top-quality excavators available for rent at competitive rates.

At ExcavateRents, we understand the importance of having the right equipment for the job, which is why we focus primarily on providing a diverse range of excavators tailored to meet your specific needs. From compact mini excavators perfect for tight spaces to heavy-duty models designed for large-scale projects, our inventory has something for every requirement.

## Here's what you can expect from our Build Alone website:

#### Extensive Excavator Selection: Explore a diverse range of excavators tailored to various project needs, from compact mini excavators to heavy-duty models.

#### Detailed Equipment Information: Access comprehensive specifications, images, and rental options for each excavator, empowering informed decision-making.

#### User-Friendly Interface: Navigate seamlessly through the website's intuitive layout, ensuring a hassle-free browsing experience.

#### Convenient Online Booking: Enjoy the convenience of online booking, allowing users to reserve their desired excavator with just a few clicks.

#### Mobile-Friendly Design: Access our website anytime, anywhere, from any device. Whether you're in the kitchen with your smartphone or planning meals on your tablet, our mobil-friendly design ensures a seamless browsing experience.

#### Flexible Rental Periods: Benefit from flexible rental periods tailored to individual project timelines, ensuring maximum convenience.

## Happy Building!

# User experience (UX)

- ## *User stories*

- #### First time visitor

  1. As a first time visitor, I want to find the right excavator.
  2. As a first time visitor, I want to quickly check rental availability and pricing.
  3. As a first time visitor, I want to explore a diverse range of recipes, discover new flavors, and gain inspiration for my culinary adventures in the kitchen.

- #### Returning visitor goals

  1. As a returning visitor, I want to explore new recipes added to the collection or to rediscover old favorites.
  2. As a returning visitor, I want to continue honing my cooking skills and knowledge.
  3. As a returning visitor, I want to add, edit or delete my recipes.

- #### Frequent User Goals

  1. As a frequent user, I want to check if the new features have been added.
  2. As a frequent user, I want to continuously explore new recipes across various cuisines, dietary preferences, and cooking styles.
  3. As a frequent user, I want to improve their cooking skills and techniques by experimenting with more advanced recipes, trying out different cooking methods, and mastering challenging culinary tasks.

- ## *Design*

- #### Color scheme

    Website features a striking color scheme designed to create a sleek and cohesive visual experience. The main page boasts a clean white background, evoking a sense of simplicity and clarity, with black text providing clear and legible content. Meanwhile, the header and footer sections command attention with their teal color, which adds a vibrant splash of energy to the overall design. Against these teal backgrounds, white text stands out prominently, ensuring that important navigation elements and essential information are easily accessible and visually engaging. This thoughtful combination of colors creates a modern and sophisticated ambiance, inviting users to explore our website with style and ease

- #### Typography
  
    Roboto font is the main font used throughout the whole website with sans-serif as the fallback font in case for any reason the font isn't being imported into the site correctly.

- #### Icons

    Materialize and Font Awesome icons have been used to style the page to boost user experience.

## Languages used

- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


## Frameworks, Libraries & Programs used

1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
2. [GitHub:](https://github.com/)
    - GitHub is used to store the project code after being pushed from Git.
3. [Pixabay](https://pixabay.com/)
    - Pixabay Was used for images.
4. [Materialize 1.0.0](https://materializecss.com/)
    - Materialize is used to assist with the responsiveness and styling of the website.
5. [MongoDB](https://www.mongodb.com/)
    - Mongo is used to store the data andsearch through the recipes by text.
6. [Heroku](https://dashboard.heroku.com/)
    - Heroku is used for cloud-based hosting platform.
7. [Font Awesome](https://fontawesome.com/)
    - Font Awesome styling of the website.

## Database_schema - for planning purposes before creating website

<h2 align="center"><img src="https://i.ibb.co/N7Kr05n/Database-schema.png"  alt="Database_schema" border="0"></h2>

### Relational database explained
A relational database for web development is a type of database management system (DBMS) that organizes data into tables of rows and columns, with relationships defined between them. Here's a brief overview of its components and how it's used in web development:

- Tables: Data is stored in tables, where each table represents a specific entity or concept (e.g., users, products, orders). Each row in a table represents a single record or instance of that entity, and each column represents a specific attribute or field of that entity.

- Primary Keys: Each table typically has a primary key, which uniquely identifies each row within the table. This ensures that each record is uniquely identifiable and facilitates relationships between tables.

- Relationships: Relationships between tables are established using foreign keys. A foreign key in one table refers to the primary key in another table, creating a link between the two tables. Common types of relationships include one-to-one, one-to-many, and many-to-many.

- Normalization: Relational databases are often normalized to minimize redundancy and improve data integrity. Normalization involves organizing data into multiple tables and eliminating redundant information.

- Structured Query Language (SQL): SQL is used to interact with relational databases. It provides a standardized language for querying, updating, and managing data in the database. Common SQL commands include SELECT, INSERT, UPDATE, DELETE, and JOIN.

- ACID Properties: Relational databases ensure data consistency and integrity by adhering to ACID properties: Atomicity, Consistency, Isolation, and Durability. These properties guarantee that database transactions are processed reliably and securely.

In web development, relational databases are commonly used as the backend data storage solution for web applications. They allow developers to store and retrieve data efficiently, support complex queries, and enforce data integrity constraints. Frameworks and libraries such as Django (Python), Ruby on Rails (Ruby), and Laravel (PHP) provide built-in support for relational databases, making it easy to integrate them into web applications.

### Non-Relational database explained
A non-relational database, also known as NoSQL (Not Only SQL), is a type of database management system that stores and retrieves data in a format other than the tabular relations used in relational databases. Here's a brief overview of non-relational databases and their use in web development:

- Document Stores: One common type of non-relational database is the document store, which stores data in flexible, schema-less documents, typically using formats like JSON or BSON. Each document can have its own structure, and related data can be nested within documents.

- Key-Value Stores: Key-value stores are simple databases that store data as a collection of key-value pairs. They are highly efficient for simple data retrieval but may not support complex queries or relationships between data.

- Wide-Column Stores: Wide-column stores organize data into columns rather than rows, allowing for efficient retrieval of large datasets with varying schemas. They are well-suited for storing and analyzing big data.

- Graph Databases: Graph databases represent data as nodes, edges, and properties, making them ideal for storing and querying complex relationships between data entities. They excel at handling interconnected data, such as social networks or recommendation systems.

- In-Memory Databases: In-memory databases store data in system memory rather than on disk, resulting in faster read and write operations. They are commonly used for caching frequently accessed data and improving application performance.

- Distributed Databases: Distributed databases distribute data across multiple nodes or servers, providing scalability and fault tolerance. They are designed to handle large volumes of data and high levels of concurrency, making them suitable for web applications with high traffic and data storage requirements.

Non-relational databases are often used in web development for their flexibility, scalability, and performance advantages, especially in applications with rapidly changing requirements or large volumes of unstructured data. Popular examples of non-relational databases include MongoDB, Redis, Cassandra, and Neo4j. These databases offer a wide range of features and capabilities to meet the diverse needs of modern web applications.

## My Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

- [Home page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhealthy-book-piotr-034b028d3ac7.herokuapp.com%2F)
- [Add Recipe page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhealthy-book-piotr-034b028d3ac7.herokuapp.com%2Fget_category)
- [Recipe page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fhealthy-book-piotr-034b028d3ac7.herokuapp.com%2Fget_recipes)
- [Login page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhealthy-book-piotr-034b028d3ac7.herokuapp.com%2Flog_in)
- [Register page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhealthy-book-piotr-034b028d3ac7.herokuapp.com%2Fregister)
- [CSS test results by text input](https://jigsaw.w3.org/css-validator/validator)

<h2 align="center"><img src="https://i.ibb.co/F03r9yM/CSS-check.png"  alt="CSS validation check" border="0"></h2>

- The text was chacked in the free grammar checker](https://www.grammarly.com/spell-checker)
- The text for website and readme file was partly wrriten by ChatGPT 3.5](https://chat.openai.com/)
  
## PEP8 Python style guide explained - 
PEP 8 is a style guide for writing Python code. PEP stands for Python Enhancement Proposal, and it's a design document providing information or describing a new feature for Python or its processes. PEP 8 specifically focuses on the style conventions for writing Python code in a way that is readable and consistent.

- Here's an overview of some of the key points covered in PEP 8:

- Indentation: Python code should be indented using 4 spaces per indentation level. Tabs should not be used for indentation.

- Line Length: Lines of code should be limited to 79 characters. However, this is not a strict rule, and lines can be up to 120 characters if necessary, but should be avoided when possible.

- Blank Lines: Use blank lines to separate functions, classes, and blocks of code within functions to improve readability.

- Imports: Import statements should usually be on separate lines and should import only one module per line. Standard library imports should be grouped before third-party library imports.

- Whitespace: Surround operators with whitespace, but don't use extraneous whitespace. Also, avoid trailing whitespace at the end of lines.

- Naming Conventions: Use descriptive names for variables, functions, classes, and modules. Variables and functions should be lowercase, with words separated by underscores (snake_case). Classes should be capitalized (CamelCase).

- Comments: Write comments to explain the purpose of the code when necessary. Comments should be clear and concise. Inline comments should be used sparingly and should be preceded by at least two spaces.

- Documentation Strings: Use docstrings to document modules, classes, functions, and methods. Docstrings should be enclosed in triple quotes (""").

- Function and Method Arguments: Don't put spaces around the = sign when used to indicate a keyword argument or a default parameter value.

- Constants: Constants should be defined using all capital letters with underscores separating words.

These are just some of the key points from PEP 8. Adhering to these style conventions helps make Python code more readable and maintainable, especially in collaborative projects where consistency is important.

### Carried out automotion testing with PEP8 installed in terminal with command "$ pip install pep8" : 

#### PEP8 first scan

<h2 align="center"><img src="https://i.ibb.co/4fQfzmy/pep8-first-scan.png" alt="pep8 firsts scan" border="0"></h2>

#### PEP8 second scan

<h2 align="center"><img src="https://i.ibb.co/9HwH4D5/pep8-second-scan.png" alt="pep8 second scan" border="0"></h2>

### Carried out manual testing as follows : 

#### Homepage
- Click on logo or Home and verify that home page appears.
- If visitor is not logged in “Log in” and "Register" should be displayed in the navigation and clicking this link will bring you to the relevant page.
- If visitor is logged in “Your Profile”, “Add recipe”, “Recipes”, “Log out” should be displayed in the navigation and clicking this link will bring you to the relevant page.
- Ensure slider displaying correct images.
- Confirmed that the header links, link to the correct pages
- Confirmed that the header links, link to the correct pages on smaller devices
- Confirmed that the social links in the footer open in a new browser window and go to the correct links

#### Register page
- Confirmed that the form work correctly, and user registration adds details to MongoDB database
- Confirmed that the register form selector work correctly


#### Log in  page
- Confirmed that the form work correctly, and user session is on
- Confirmed that the log in form selector work correctly

#### Add recipe page
- Confirmed that the form work correctly, and recipes are added
- Confirmed that the add recipe form selector work correctly

#### Edit recipe page
- Confirmed that the form work correctly, and recipes are eddited
- Confirmed that the edit form selector work correctly

#### Recipe page
- Confirmed that the website display recipes correctly from the database
- Confirmed that the "delete" button works correctly
    - user authorsation is missing as ones clicked recipe is deleted
- Confirmed that the "edit" button works correctly
- Confirmed that the user can only delete or edit recipes added by him/her
- Confirmed that the "search" button works correctly. Search is performed by text on "list of ingridiens" and "recipe name"

#### Footer
- Confirmed that the footer links, link to the correct pages

### Further testing

- The Website was tested on Google Chrome, Internet Explorer, Firefox and Safari browsers.
- The website was viewed on a variety of devices such as Desktop, Laptop, iPhone 14, iPhone 12 Pro Max & Samsung Galaxy S20
- A large amount of testing was done to ensure that the aplication has no bugs.
- Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Screenshots from testing

#### Tested if registration of the new user works correctly

<h2 align="center"><img src="https://i.ibb.co/SQmjf4F/Registration.png" alt="Registration succesfull" border="0"></h2>

#### Tested if log in of created user works correctly

<h2 align="center"><img src="https://i.ibb.co/RS2Dbjn/Login.png" alt="Log in test" border="0"></h2>

#### Tested if log out of loged in user works correctly

<h2 align="center"><img src="https://i.ibb.co/8KbS3sw/Logout.png" alt="Log out test" border="0"></h2>

#### Tested if adding recipe to the database works correctly

<h2 align="center"><img src="https://i.ibb.co/SV4gWTK/Add-recipe-test.png" alt="Add recipe" border="0"></h2>

#### Tested if editing recipe works correctly

<h2 align="center"><img src="https://i.ibb.co/27d3d2x/Edit-recipe.png" alt="Edit recipe" border="0"></h2>

#### Tested if deleting recipe works correctly

<h2 align="center"><img src="https://i.ibb.co/VgKzYWC/Delete-recipe.png" alt="Delete recipe" border="0"></h2>

#### Check if patterns of the forms works corectly

<h2 align="center"><img src="https://i.ibb.co/bBvqj5h/Check-if-patterns-are-working.png" alt="Pattern check" border="0"></h2>

#### Second check if patters on forms works correctly

<h2 align="center"><img src="https://i.ibb.co/xq0hWxT/Check-if-patterns-are-working-v2.png" alt="Second pattern check" border="0"></h2>

### Known Bugs

- None

## Deployment

Deployment and source control was carried out via GitHub and Heroku. The repository location is as follows:https://github.com/Biecho88/healthy_book

1. Database and Tables were created in an Atlas MongoDB account
2. Project workspace was created in GitHub. In this workspace: Flask was installed  - It was moved to GitPod but still linked to GitHub.
3. Setup run.py file and imported flask and os
4. Create a new Heroku App - unique name and EU Server
5. Login to Heroku to add config variables including IP, Port, Mongo_DB and Mongo_URI
6. Get Flask to talk to MongoDB
7. Add extra libraries to run.py
8. Add DB connection code to run.py 
9. Test connection to DB again to confirm it's working
10. Connect GitHub repository to Heroku using code provided by heroku and github
11. Continue to create app and regular commits
12. Set Debug to False
13. Connect GitHub repository to Heroku using code provided by heroku and github

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures of some of the buttons and more detailed explanations of the above process.

## Credits

### Content

- All content was written by the developer.

### Acknowledgments

- My Mentor for helpful feedback.

- Tutor support at Code Institute for their support.

- Student support on Slack [Link](https://app.slack.com/client/T0L30B202/C058BTPP7A5)