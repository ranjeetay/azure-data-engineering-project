CREATE TABLE dim_customer (
customer_id INT,
customer_name VARCHAR(100)
);

CREATE TABLE dim_product (
product_id INT,
product_name VARCHAR(100),
category VARCHAR(50)
);

CREATE TABLE fact_sales (
order_id INT,
customer_id INT,
product_id INT,
quantity INT,
price DECIMAL(10,2),
total_revenue DECIMAL(10,2)
);
