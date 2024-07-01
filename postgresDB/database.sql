CREATE SCHEMA IF NOT EXISTS homeassigment;

CREATE TABLE IF NOT EXISTS homeassigment.questions (
    id SERIAL PRIMARY KEY,
    question VARCHAR(4096) NOT NULL,
    answer VARCHAR(4096) NOT NULL,
    created_at TIMESTAMP
);