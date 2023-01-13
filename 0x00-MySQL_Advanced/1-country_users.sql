-- Creates a table with unique users.
CREATE TABLE IF NOT EXISTS users(
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255),
    country VARCHAR(10) NOT NULL CHECK (country IN('US', 'CO', 'TN'))
    PRIMARY KEY(ID)
)