SELECT a.Name, a.Salary, c.Name FROM Employee a, 
(SELECT MAX(Salary) AS Salary,DepartmentId FROM Employee GROUP BY DepartmentId) b, 
Department c 
WHERE a.Salary = b.Salary AND a.DepartmentId = b. DepartmentId AND b.DepartmentId = c.Id;
