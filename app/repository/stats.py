hiredEmployeesByQuarterHeader= ['Department', 'Job', 'Q1', 'Q2', 'Q3', 'Q4']
hiredEmployeesByQuarterQuery = """ 
    WITH cte AS ( SELECT
	        d.name as department,
	        j.name as job,
	CASE WHEN e.datetime BETWEEN '2021-01-01 00:00:00' AND '2021-03-31 23:59:59' 
		THEN 1 ELSE 0 END as Q1,
	CASE WHEN e.datetime BETWEEN '2021-04-01 00:00:00' AND '2021-06-30 23:59:59' 
		THEN 1 ELSE 0 END as Q2,
	CASE WHEN e.datetime BETWEEN '2021-07-01 00:00:00' AND '2021-09-30 23:59:59' 
		THEN 1 ELSE 0 END as Q3,
	CASE WHEN e.datetime BETWEEN '2021-10-01 00:00:00' AND '2021-12-31 23:59:59' 
		THEN 1 ELSE 0 END as Q4
    FROM employees e
    INNER JOIN departments d 
	    ON e.department_id = d.id
    INNER JOIN jobs j 
	    ON e.job_id = j.id
    WHERE EXTRACT(YEAR FROM e.datetime) = 2021)
    SELECT department, 
	    job, 
	    SUM(Q1) as Q1, 
	    SUM(Q2) as Q2,
	    SUM(Q3) as Q3, 
	    SUM(Q4) as Q4
    FROM cte
    GROUP BY department, job
    ORDER BY department, job 
            """

hiredCountOverAVGHeader= ['Id', 'Department', 'Hired']
hiredCountOverAVGQuery = """
    with cte as (
    select
	    d.id as id,
	    d.name as Department,
	    count(1) as hired
    FROM departments d
    left join employees e 
	    on d.id = e.department_id
    where EXTRACT(YEAR FROM e.datetime) = 2021
    group by d.id, d.name)
    select *
    from cte
	    where hired > (select avg(hired) from cte)
    """
