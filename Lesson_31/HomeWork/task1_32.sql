--1. write a query in SQL to display the first name, last name, department number, and department name for each employee

SELECT
    e.first_name,
    e.last_name,
    d.department_id,
    d.depart_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

--2. write a query in SQL to display the first and last name, department, city, and state province for each employee

SELECT
    e.first_name,
    e.last_name,
    d.depart_name,
    l.city,
    l.state_province
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
ORDER BY l.city;

--3. write a query in SQL to display the first name, last name, department number, and department name,
--for all employees for departments 80 or 40

SELECT
    e.first_name,
    e.last_name,
    d.department_id,
    d.depart_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE d.department_id = 80 OR d.department_id = 40;

--4. write a query in SQL to display all departments including those where does not have any employee
SELECT
    d.department_id,
    d.depart_name
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id;

--5. write a query in SQL to display the first name of all employees including the first name of their manager
SELECT
    e.first_name AS employee_name,
    m.first_name AS manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;

--6.write a query in SQL to display the job title, full name (first and last name ) of the employee,
--and the difference between the maximum salary for the job and the salary of the employee

SELECT
    j.job_title,
    e.first_name || ' ' || e.last_name AS full_name,
    j.max_salary - e.salary AS salary_difference
FROM employees e
JOIN jobs j ON e.job_id=j.job_id;

--7. write a query in SQL to display the job title and the average salary of employees
SELECT
    j.job_title,
    AVG(e.salary) AS average_salary
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
GROUP BY j.job_title;

--8. write a query in SQL to display the full name (first and last name),
--and salary of those employees who work in any department located in London

SELECT
    e.first_name || ' ' || e.last_name AS full_name,
    e.salary,
    l.city
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON l.location_id = d.location_id
WHERE l.city = 'London';

--9. write a query in SQL to display the department name and the number of employees in each department

SELECT
    d.depart_name,
    COUNT(e.employee_id) AS employees_in_department
FROM employees e
LEFT JOIN departments d ON e.department_id=d.department_id
GROUP BY d.depart_name;
