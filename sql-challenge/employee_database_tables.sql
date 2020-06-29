DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS dept_emp;
DROP TABLE IF EXISTS dept_manager;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS salaries;
DROP TABLE IF EXISTS titles;

CREATE TABLE departments (
  dept_no VARCHAR(30) NOT NULL,
  dept_name VARCHAR(30) NOT NULL
);

CREATE TABLE dept_emp (
  emp_no integer NOT NULL,
  dept_no VARCHAR(30) NOT NULL
);

CREATE TABLE dept_manager (
  dept_no VARCHAR(30) NOT NULL,
  emp_no integer NOT NULL
);

CREATE TABLE employees (
  emp_no integer NOT NULL,
  emp_title_id VARCHAR(30) NOT NULL,
  birth_date DATE NOT NULL,
  first_name VARCHAR(30) NOT NULL,
  last_name VARCHAR(30) NOT NULL,
  sex VARCHAR(1) NOT NULL,
  hire_date DATE NOT NULL
);

CREATE TABLE salaries (
  emp_no integer NOT NULL,
  salary VARCHAR(30) NOT NULL
);

CREATE TABLE titles (
  title_id VARCHAR(30) NOT NULL,
  title VARCHAR(30) NOT NULL
);
