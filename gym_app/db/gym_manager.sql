DROP TABLE bookings;
DROP TABLE members;
DROP TABLE exclasses;

CREATE TABLE exclasses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    activity_type VARCHAR(255),
    duration INT,
    capacity INT
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
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    exclass_id INT REFERENCES exclasses(id) ON DELETE CASCADE
);