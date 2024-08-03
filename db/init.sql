-- Create DDLs for this test

CREATE TABLE departments(
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

CREATE TABLE jobs(
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

CREATE TABLE employees(
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  datetime TIMESTAMP,
  department_id INTEGER,
  job_id INTEGER,
  FOREIGN KEY (department_id) REFERENCES departments (id),
  FOREIGN KEY (job_id) REFERENCES jobs (id)
);

INSERT INTO departments (
  name
) VALUES ('Supply Chain'), ('Maintenance'), ('Staff');


INSERT INTO jobs (
  name) VALUES ('Recruiter'), ('Manager'), ('Analyst');
