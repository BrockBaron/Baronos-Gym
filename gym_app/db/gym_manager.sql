DROP TABLE bookings;
DROP TABLE members;
DROP TABLE classes;

CREATE TABLE exclasses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    duration INT,
    cpacity INT,
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    second_name VARCHAR(255),
    age INT,
    sex VARCHAR(255)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES member(id) ON DELETE CASCADE,
    exclass_id INT REFERENCES exclass(id) ON DELETE CASCADE
);