CREATE VIEW top_students AS
SELECT id, name, major, gpa
FROM students
WHERE gpa > 3.5;


-- A view is a virtual table that consists of a stored query.
