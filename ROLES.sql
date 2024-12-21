CREATE ROLE admin_role;
CREATE ROLE faculty_role;
CREATE ROLE student_role;

GRANT SELECT, INSERT, UPDATE, DELETE ON students TO admin_role;
GRANT SELECT, INSERT ON students TO faculty_role;
GRANT SELECT ON students TO student_role;

EXEC sp_addrolemember 'admin_role', 'admin_user';
EXEC sp_addrolemember 'faculty_role', 'faculty_user';
EXEC sp_addrolemember 'student_role', 'student_user';

-- SQL Server's roles and permissions