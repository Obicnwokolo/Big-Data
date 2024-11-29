 -- INNER JOIN
SELECT e.EmployeeID, e.FirstName, e.LastName, 
d.DepartmentName
FROM Employees e
INNER JOIN Departments d
	ON e.EmployeeID = d.ManagerID;

-- LEFT JOIN (LEFT OUTER JOIN)
SELECT e.EmployeeID, e.FirstName, e.LastName, 
d.DepartmentName
FROM Employees e
LEFT JOIN Departments d
	ON e.EmployeeID = d.ManagerID;

-- RIGHT JOIN (RIGHT OUTER JOIN)
SELECT e.EmployeeID, e.FirstName, e.LastName, 
d.DepartmentName
FROM Employees e
RIGHT JOIN Departments d
	ON e.EmployeeID = d.ManagerID;

-- FULL OUTER JOIN
SELECT e.EmployeeID, e.FirstName, e.LastName, 
d.DepartmentName
FROM Employees e
LEFT JOIN Departments d
	ON e.EmployeeID = d.ManagerID
UNION
SELECT e.EmployeeID, e.FirstName, e.LastName, 
d.DepartmentName
FROM Employees e
RIGHT JOIN Departments d
	ON e.EmployeeID = d.ManagerID;

-- CROSS JOIN
SELECT e.EmployeeID, e.FirstName, 
d.DepartmentName
FROM Employees e
CROSS JOIN Departments d;

-- SELF JOIN
SELECT 
	E1.EmployeeID AS Employee1, E1.FirstName AS Employee1Name, 
	E2.EmployeeID AS Employee2, E2.FirstName AS Employee2Name
FROM Employees E1
INNER JOIN Employees E2
	ON E1.Department = E2.Department
WHERE E1.EmployeeID <> E2.EmployeeID;

-- MULTIPLE JOIN
SELECT 
	E.EmployeeID, E.FirstName, E.LastName, 
    D.DepartmentName, 
    M.FirstName AS ManagerFirstName, M.LastName AS ManagerLastName
FROM Employees E
INNER JOIN Departments D
	ON E.EmployeeID = D.ManagerID
INNER JOIN Employees M
	ON D.ManagerID = M.EmployeeID;