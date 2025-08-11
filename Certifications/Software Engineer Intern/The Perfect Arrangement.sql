/*
Enter your query here.
*/
SELECT 
    id,
    first_name,
    last_name
FROM CUSTOMER
WHERE 
    LENGTH(CONCAT(first_name, last_name)) < 12
ORDER BY 
    LENGTH(CONCAT(first_name, last_name)) ASC,
    UPPER(CONCAT(first_name, last_name)) ASC,
    id ASC;


--     Task: Write a query that concatenates customers' first and last names together and returns only those customers whose combined name is less than 12 characters long.
-- Key Requirements:

-- Concatenate first_name + last_name to create a combined name
-- Filter: Keep only customers where combined name length < 12 characters
-- Sort by: Combined name length (shortest first), then alphabetically by combined name (case insensitive), then by ID
-- Return: id, first_name, last_name columns

-- Skills Tested: String concatenation, length functions, filtering with WHERE clause, multi-level sorting with ORDER BY, and case-insensitive sorting.