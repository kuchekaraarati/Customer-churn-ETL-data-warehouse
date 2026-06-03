CREATE DATABASE CustomerChurnDW;

USE CustomerChurnDW;

CREATE TABLE Stg_Customer_Churn
(
    customer_id VARCHAR(50),
    customer_name VARCHAR(100),
    email VARCHAR(100),
    signup_date DATE,
    last_login_date DATE,
    region VARCHAR(50),
    subscription_plan VARCHAR(50),
    monthly_spend DECIMAL(10,2),
    support_tickets INT,
    feedback_text VARCHAR(500),
    churned INT
);
SELECT * FROM Stg_Customer_Churn;

truncate table Stg_Customer_Churn;

SELECT COUNT(*) AS TotalRecords
FROM Stg_Customer_Churn;

CREATE TABLE DimCustomer
(
    CustomerKey INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID VARCHAR(50),
    CustomerName VARCHAR(100),
    Region VARCHAR(50),
    SubscriptionPlan VARCHAR(50)
);

CREATE TABLE FactCustomerActivity
(
    ActivityKey INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID VARCHAR(50),
    MonthlySpend DECIMAL(10,2),
    SupportTickets INT,
    Churned INT
);

INSERT INTO DimCustomer
(
    CustomerID,
    CustomerName,
    Region,
    SubscriptionPlan
)
SELECT DISTINCT
    customer_id,
    customer_name,
    region,
    subscription_plan
FROM Stg_Customer_Churn;

SELECT COUNT(*) AS CustomerCount
FROM DimCustomer;

INSERT INTO FactCustomerActivity
(
    CustomerID,
    MonthlySpend,
    SupportTickets,
    Churned
)
SELECT
    customer_id,
    monthly_spend,
    support_tickets,
    churned
FROM Stg_Customer_Churn;

SELECT COUNT(*) AS FactCount
FROM FactCustomerActivity;

SELECT
    COUNT(*) AS TotalCustomers,
    SUM(churned) AS ChurnedCustomers,
    ROUND(
        100.0 * SUM(churned) / COUNT(*),
        2
    ) AS ChurnRate
FROM FactCustomerActivity;

SELECT
    d.SubscriptionPlan,
    COUNT(*) AS Customers,
    SUM(f.Churned) AS ChurnedCustomers
FROM FactCustomerActivity f
JOIN DimCustomer d
    ON f.CustomerID = d.CustomerID
GROUP BY d.SubscriptionPlan;

SELECT++
    d.Region,
    AVG(f.MonthlySpend) AS AvgSpend
FROM FactCustomerActivity f
JOIN DimCustomer d
    ON f.CustomerID = d.CustomerID
GROUP BY d.Region;
