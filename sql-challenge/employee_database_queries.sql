-- 1. List the following details of each employee: employee number, last name, first name, gender, and salary.
select employees.emp_no, employees.last_name, employees.first_name, employees.sex, salaries.salary
from employees
join salaries
using (emp_no);

-- 2. List employees who were hired in 1986.
select emp_no, first_name, last_name, hire_date
from employees
where hire_date between '1986-01-01' and '1986-12-31'
order by hire_date asc;

-- 3. List the manager of each department with the following information: 
---- department number, department name, the manager's employee number, 
---- last name, first name, and start and end employment dates

select  dept_manager.dept_no, departments.dept_name, dept_manager.emp_no, employees.last_name, employees.first_name, employees.hire_date
from dept_manager
join departments
using (dept_no)
join employees
using (emp_no)
order by dept_manager.dept_no asc;

-- 4. List the department of each employee with the following information: 
-- employee number, last name, first name, and department name.

select dept_emp.emp_no, employees.last_name, employees.first_name, departments.dept_name
from dept_emp
join departments
using (dept_no)
join employees
using (emp_no)
order by emp_no asc;

-- 5. List all employees whose first name is "Hercules" and last names begin with "B."
select emp_no, first_name, last_name 
from employees
where first_name = 'Hercules' and last_name like 'B%'
order by last_name asc;

-- 6. List all employees in the Sales department, 
-- including their employee number, last name, first name, and department name.

select dept_emp.emp_no, employees.first_name, employees.last_name, departments.dept_name
from dept_emp
join departments
using (dept_no)
join employees
using (emp_no)
where dept_name = 'Sales'
order by emp_no asc;

-- 7. List all employees in the Sales and Development departments, 
-- including their employee number, last name, first name, and department name.

select dept_emp.emp_no, departments.dept_name, employees.first_name, employees.last_name
from dept_emp
join departments
using (dept_no)
join employees
using (emp_no)
where dept_name = 'Sales' or dept_name = 'Development'
order by emp_no asc;

-- 8. In descending order, list the frequency count of employee last names, 
-- i.e., how many employees share each last name.


select last_name, count(last_name) as name_frequency
from employees
group by last_name
order by count(last_name) asc;


