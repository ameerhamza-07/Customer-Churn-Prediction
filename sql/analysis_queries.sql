SELECT * FROM customer

SELECT COUNT(*) AS total_customers
FROM customer

SELECT
ROUND(AVG(churn_value)*100,2) AS churn_rate
FROM customer;

SELECT
contract,
COUNT(*) AS customers,
ROUND(AVG(churn_value)*100,2) AS churn_rate
FROM customer
GROUP BY contract
ORDER BY churn_rate DESC;


SELECT
internet_service,
COUNT(*) AS customers,
ROUND(AVG(churn_value)*100,2) AS churn_rate
FROM customer
GROUP BY internet_service
ORDER BY churn_rate DESC;



SELECT
payment_method,
COUNT(*) AS customers,
ROUND(AVG(churn_value)*100,2) AS churn_rate
FROM customer
GROUP BY payment_method
ORDER BY churn_rate DESC;


SELECT
state,
COUNT(*) AS customers,
ROUND(AVG(churn_value)*100,2) AS churn_rate
FROM customer
GROUP BY state
ORDER BY churn_rate DESC;


SELECT
city,
COUNT(*) AS customers,
ROUND(AVG(churn_value)*100,2) AS churn_rate
FROM customer
GROUP BY city
ORDER BY churn_rate DESC
LIMIT 10;

SELECT
SUM(total_charges) AS revenue_lost
FROM customer
WHERE churn_value=1;


SELECT
churn_reason,
COUNT(*) AS frequency
FROM customer
WHERE churn_reason IS NOT NULL
GROUP BY churn_reason
ORDER BY frequency DESC
LIMIT 10;


CREATE OR REPLACE VIEW churn_summary AS

SELECT
contract,
internet_service,
COUNT(*) AS customers,
ROUND(AVG(churn_value)*100,2) AS churn_rate

FROM customer

GROUP BY
contract,
internet_service;