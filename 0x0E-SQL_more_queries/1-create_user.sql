-- creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'Jack1_hbtn';
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
