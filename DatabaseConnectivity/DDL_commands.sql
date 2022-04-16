CREATE DATABASE SquareShift_Test;

CREATE TABLE PRODUCT (
id INT,
name VARCHAR(255),
price FLOAT,
description VARCHAR(1025),
category VARCHAR(255),
image VARCHAR(255),
discount_percentage FLOAT,
weight_in_grams FLOAT,
PRIMARY KEY (id)
);

CREATE TABLE WAREHOUSE (
postal_code INT,
distance_in_kilometers INT,
PRIMARY KEY (postal_code)
);

CREATE TABLE ITEMS (
product_id INT,
quantity INT,

PRIMARY KEY (product_id)
FOREIGN KEY (product_id) REFERENCES PRODUCT(id)
);