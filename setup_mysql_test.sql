-- This script prepares a MySQL server for the project

-- Creating a database with the name 'hbnb_test_db'
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creating a new user 'hbnb_test' in the localhost with password 'hbnb_test_pwd'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED  BY 'hbnb_test_pwd';

-- Granting user `hbnb_test` all privileges on database `hbnb_test_db`
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

-- Granting user `hbnb_test` select privileges on database `performance_schema`
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;


