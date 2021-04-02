DROP TABLE bookings;
DROP TABLE members;
DROP TABLE classes;

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    duration INT,
    cpacity INT,
    sex_preferences VARCHAR(255)
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
    member_id INT references(member_id) ON DELETE CASCADE,
    class_id INT references(class_id) ON DELETE CASCADE
);