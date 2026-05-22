
-- delete database.
drop database if exists sport_tracker;

-- create DB.
CREATE DATABASE sport_tracker;

-- list all table.
\dt

-- delete all row from alembic version (migration).
DROP TABLE alembic_version;


-- inserts.
truncate table roles restart identity cascade;
insert into roles(id, name) values(1, 'client');
insert into roles(id, name) values(2, 'admin');
select * from roles;

truncate table users restart identity cascade;
--CREATE EXTENSION IF NOT EXISTS pgcrypto;  -- crypt('myPassword', gen_salt('bf'))
insert into users(id, role_id, first_name, last_name, email, password, phone_number, height, weight, birth_date, gender) values
(
 1,
 1,
 'Thomas',
 'Delta',
 'client@gmail.com',
 '$2b$12$.hCTTgyZB6jYs3g1DtFBOebu4XHUqOIoYnckH2OB2XkL2CQ93vHy.',  -- Test1234
 '+32 00-00-00-00',
 '1.80',
 '85',
 '1990-01-01'::date,
 'Male'
);
insert into users(id, role_id, first_name, last_name, email, password, phone_number, height, weight, birth_date, gender) values
(
 2,
 2,
 'Admin',
 'Super',
 'admin@gmail.com',
 '$2b$12$.hCTTgyZB6jYs3g1DtFBOebu4XHUqOIoYnckH2OB2XkL2CQ93vHy.',  -- Test1234
 '+32 00-00-00-00',
 '1.70',
 '90',
 '1980-01-01'::date,
 'Female'
);
select * from users;
--update users set email = 'client@gmail.com' where id = 1;

truncate table exercices restart identity cascade;
insert into exercices(id, name, description, url_details, url_image, amplitude, is_minutes) values
(1, 'Pompes', null, null, null, 0.7, false),
(2, 'Squat', null, null, null, 1.0, false),
(3, 'Tractions', null, null, null, 1.0, false),
(4, 'Abdominaux', null, null, null, 0.3, false),
(5, 'Burpees', null, null, null, 1.0, false);
select * from exercices;

