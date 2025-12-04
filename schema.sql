-- Create Database Structure
DROP TABLE IF EXISTS students;

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    branch TEXT NOT NULL,
    marks INTEGER,
    email TEXT UNIQUE
);
