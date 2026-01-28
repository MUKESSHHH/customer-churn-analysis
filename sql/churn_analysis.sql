CREATE DATABASE customer_churn;
USE customer_churn;

CREATE TABLE churn_data (
    customerID VARCHAR(50),
    gender VARCHAR(10),
    SeniorCitizen INT,
    tenure INT,
    MonthlyCharges FLOAT,
    TotalCharges VARCHAR(50),
    Contract VARCHAR(50),
    InternetService VARCHAR(50),
    PaymentMethod VARCHAR(50),
    Churn VARCHAR(10)
);

-- Total customers
SELECT COUNT(*) FROM churn_data;

-- Churn count
SELECT COUNT(*) FROM churn_data WHERE Churn = 'Yes';

-- Churn by contract
SELECT Contract, COUNT(*) AS churn_count
FROM churn_data
WHERE Churn = 'Yes'
GROUP BY Contract;