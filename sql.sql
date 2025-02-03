CREATE SCHEMA `snehal` ;
CREATE TABLE countries (
  country_id INT AUTO_INCREMENT PRIMARY KEY,
  country_name VARCHAR(255) NOT NULL,
  max_size INT NOT NULL,
  max_weight INT NOT NULL,
  custom_duty_tax DECIMAL(10, 2),
  banned_items TEXT);
CREATE TABLE users (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255) UNIQUE,
  password VARCHAR(255));
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  country_id INT,
  parcel_size INT,
  parcel_weight INT,
  shipping_charge DECIMAL(10, 2),
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (country_id) REFERENCES countries(country_id));





