SELECT class FROM (


SELECT COUNT(student) as c, class FROM Courses
GROUP BY class
HAVING c>=5) as T