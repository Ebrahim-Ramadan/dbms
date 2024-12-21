-- Create the students table
CREATE TABLE students (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    major VARCHAR(100) NULL,
    age INT NULL,
    enrollment_year INT NULL,
    gpa DECIMAL(3,2) NULL
);

-- Basic INSERT statement
INSERT INTO students (name, major, age, enrollment_year, gpa)
VALUES ('John Doe', 'Computer Science', 20, 2023, 3.75);

-- INSERT with NULL values
INSERT INTO students (name, major, age, enrollment_year, gpa)
VALUES ('Jane Smith', 'Physics', NULL, 2024, NULL);

-- INSERT multiple records
INSERT INTO students (name, major, age, enrollment_year, gpa)
VALUES 
    ('Bob Johnson', 'Mathematics', 19, 2023, 3.50),
    ('Alice Brown', 'Chemistry', 21, 2022, 3.90),
    ('Charlie Wilson', 'Biology', 20, 2023, 3.25);

-- SELECT all students
SELECT id, name, major, age, enrollment_year, gpa
FROM students;

-- SELECT specific student
SELECT id, name, major, age, enrollment_year, gpa
FROM students
WHERE id = ?;

-- SELECT with filtering
SELECT id, name, major, age, enrollment_year, gpa
FROM students
WHERE enrollment_year = 2023
AND gpa >= 3.0;

-- UPDATE single student
UPDATE students
SET name = ?,
    major = ?,
    age = ?,
    enrollment_year = ?,
    gpa = ?
WHERE id = ?;

-- UPDATE multiple students
UPDATE students
SET enrollment_year = 2024
WHERE enrollment_year = 2023;

-- UPDATE gpa with NULL handling
UPDATE students
SET gpa = CASE 
    WHEN ? = '' THEN NULL 
    ELSE CAST(? AS DECIMAL(3,2))
END
WHERE id = ?;

-- DELETE single student
DELETE FROM students
WHERE id = ?;

-- DELETE multiple students
DELETE FROM students
WHERE enrollment_year < 2020;

-- DELETE all students (use with caution)
DELETE FROM students;

-- Useful queries for analytics

-- Average GPA by major
SELECT major, 
       AVG(gpa) as average_gpa,
       COUNT(*) as student_count
FROM students
WHERE gpa IS NOT NULL
GROUP BY major;

-- Distribution of students by enrollment year
SELECT enrollment_year,
       COUNT(*) as student_count
FROM students
GROUP BY enrollment_year
ORDER BY enrollment_year DESC;

-- Students with missing data
SELECT id, name
FROM students
WHERE gpa IS NULL
   OR age IS NULL
   OR major IS NULL
   OR enrollment_year IS NULL;

-- Top performing students (GPA >= 3.5)
SELECT name, major, gpa
FROM students
WHERE gpa >= 3.5
ORDER BY gpa DESC;

-- Create indexes for better performance
CREATE INDEX idx_students_enrollment_year ON students(enrollment_year);
CREATE INDEX idx_students_major ON students(major);
CREATE INDEX idx_students_gpa ON students(gpa);

-- Constraints for data integrity
ALTER TABLE students
ADD CONSTRAINT chk_gpa_range 
CHECK (gpa >= 0.00 AND gpa <= 4.00);

ALTER TABLE students
ADD CONSTRAINT chk_age_range 
CHECK (age >= 16 AND age <= 120);

ALTER TABLE students
ADD CONSTRAINT chk_enrollment_year 
CHECK (enrollment_year >= 1900 AND enrollment_year <= 2100);