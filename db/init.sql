-- Create DDLs for this test

CREATE TABLE departments(
  id INTEGER PRIMARY KEY,
  name VARCHAR(100)
);

CREATE TABLE jobs(
  id INTEGER PRIMARY KEY,
  name VARCHAR(100)
);

CREATE TABLE employees(
  id INTEGER PRIMARY KEY,
  name VARCHAR(100),
  datetime TIMESTAMP,
  department_id INTEGER,
  job_id INTEGER,
  FOREIGN KEY (department_id) REFERENCES departments (id),
  FOREIGN KEY (job_id) REFERENCES jobs (id)
);

