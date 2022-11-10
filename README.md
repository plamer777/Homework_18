## Homework 18 by using Flask, SQLAlchemy, RESTX and Marshmallow
This applications works with movie, director and genre tables from database by using SQLAlchemy package. There're different functions the application provides such as:

 - To get all movies, directors and genres
 - To get single movie, director or genre by id
 - To add new movie
 - To update existing movie
 - To delete any movie from table - 
 ---
The project's structure: 
 - dao - DAOs to work with different tables
 - tests - test files for API
 - data - JSON file and a database
 - services- classes provided a business logic
 - views - there are CBVs to work with different routes
 - implemented- there're DAO, Schema and Service classes' instances
 - config - configuration class with different settings
 - utils - serving function to load data by provided IDs
 - constants - a file containing constants like paths to files, database, etc.
 - requirements.txt - file with the project's dependencies
 - app.py - a main file to start the application
 - setup_db - a file with SQLAlchemy instance
 - README.md - this file with app info
 ---
 The project was created in 10 November 2022 by Aleksey Mavrin
