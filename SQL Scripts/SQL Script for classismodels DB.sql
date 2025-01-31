use classicmodels;


SELECT firstName, jobTitle, country
FROM employees
INNER JOIN offices ON employees.officeCode = offices.officeCode
WHERE country = 'USA';

SELECT c.customerName, c.phone, p.amount
FROM customers c
JOIN payments p ON c.customerNumber = p.customerNumber
WHERE p.amount > 100000;

SELECT customerName, city, state
FROM customers
WHERE country = 'Norway';