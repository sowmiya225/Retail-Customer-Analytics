
-- Total Sales
SELECT SUM(Sales) FROM superstore;

-- Sales by Category
SELECT Category, SUM(Sales)
FROM superstore
GROUP BY Category;

-- Sales by Region
SELECT Region, SUM(Sales)
FROM superstore
GROUP BY Region;

-- Top Customers
SELECT Customer_Name, SUM(Sales) AS total_sales
FROM superstore
GROUP BY Customer_Name
ORDER BY total_sales DESC
LIMIT 10;
