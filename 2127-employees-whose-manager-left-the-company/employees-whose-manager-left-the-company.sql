# Write your MySQL query statement below
SELECT employee_id FROM Employees
WHERE salary < 30000 AND manager_id not in (SELECT e1.manager_id FROM Employees as e1 JOIN Employees as e2 on e2.employee_id = e1.manager_id) 
ORDER BY employee_id