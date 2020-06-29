-- 1. List the following details of each employee: employee number, last name, first name, gender, AND salary.

SELECT employees.emp_no, employees.last_name, employees.first_name, employees.sex, salaries.salary
FROM employees
JOIN salaries
USING (emp_no);

-- 2. List employees who were hired in 1986.

SELECT emp_no, first_name, last_name, hire_date
FROM employees
WHERE hire_date between '1986-01-01' AND '1986-12-31'
ORDER BY hire_date ASC;

-- 3. List the manager of each department with the following information: 
---- department number, department name, the manager's employee number, 
---- last name, first name, AND start AND end employment dates

SELECT  dept_manager.dept_no, departments.dept_name, dept_manager.emp_no, employees.last_name, employees.first_name, employees.hire_date
FROM dept_manager
JOIN departments
USING (dept_no)
JOIN employees
USING (emp_no)
ORDER BY dept_manager.dept_no ASC;

-- 4. List the department of each employee with the following information: 
-- employee number, last name, first name, AND department name.

SELECT dept_emp.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM dept_emp
JOIN departments
USING (dept_no)
JOIN employees
USING (emp_no)
ORDER BY emp_no ASC;

-- 5. List all employees whose first name is "Hercules" AND last names begin with "B."
SELECT emp_no, first_name, last_name 
FROM employees
WHERE first_name = 'Hercules' AND last_name LIKE 'B%'
ORDER BY last_name ASC;

-- 6. List all employees in the Sales department, 
-- including their employee number, last name, first name, and department name.

SELECT dept_emp.emp_no, employees.first_name, employees.last_name, departments.dept_name
FROM dept_emp
JOIN departments
USING (dept_no)
JOIN employees
USING (emp_no)
WHERE dept_name = 'Sales'
ORDER BY emp_no ASC;

-- 7. List all employees in the Sales and Development departments, 
-- including their employee number, last name, first name, and department name.

SELECT dept_emp.emp_no, departments.dept_name, employees.first_name, employees.last_name
FROM dept_emp
JOIN departments
USING (dept_no)
JOIN employees
USING (emp_no)
WHERE dept_name = 'Sales' or dept_name = 'Development'
ORDER BY emp_no ASC;

-- 8. In descending ORDER, list the frequency count of employee last names, 
-- i.e., how many employees share each last name.


SELECT last_name, count(last_name) AS name_frequency
FROM employees
group BY last_name
ORDER BY count(last_name) ASC;


