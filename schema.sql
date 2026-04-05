-- Database schema for clinic website

CREATE TABLE patients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    contact TEXT NOT NULL
);