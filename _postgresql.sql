
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

--truncate table users restart identity cascade;
----CREATE EXTENSION IF NOT EXISTS pgcrypto;  -- crypt('myPassword', gen_salt('bf'))
--insert into users(id, role_id, first_name, last_name, email, password, phone_number, height, weight, birth_date, gender) values
--(
-- 1,
-- 1,
-- 'Thomas',
-- 'Delta',
-- 'client@gmail.com',
-- '$2b$12$.hCTTgyZB6jYs3g1DtFBOebu4XHUqOIoYnckH2OB2XkL2CQ93vHy.',  -- Test1234
-- '+32 00-00-00-00',
-- '1.80',
-- '85',
-- '1990-01-01'::date,
-- 'Male'
--);
--insert into users(id, role_id, first_name, last_name, email, password, phone_number, height, weight, birth_date, gender) values
--(
-- 2,
-- 2,
-- 'Admin',
-- 'Super',
-- 'admin@gmail.com',
-- '$2b$12$.hCTTgyZB6jYs3g1DtFBOebu4XHUqOIoYnckH2OB2XkL2CQ93vHy.',  -- Test1234
-- '+32 00-00-00-00',
-- '1.70',
-- '90',
-- '1980-01-01'::date,
-- 'Female'
--);
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

truncate table schedules restart identity cascade;
insert into schedules(id, user_id, start_date, end_date) values
(1, 1, '2026-06-01'::date, Null);
select * from schedules;

truncate table exercice_to_dos restart identity cascade;
insert into exercice_to_dos(id, schedule_id, exercice_id, days_of_week, repetition, series, additional_weight) values
(1, 1, 1, 1, 30, 2, 0.0), -- pompe lundi.
(2, 1, 4, 2, 20, 2, 0.0), -- abdo mardi.
(3, 1, 2, 8, 12, 3, 9.0), -- squat jeudi.
(4, 1, 3, 32, 12, 3, 10.0); -- traction samedi.
select * from exercice_to_dos;

-- update user.
update users set
id=1,
role_id=1,
first_name='Thomas',
last_name='Du-puits',
email='client@gmail.com',
password='$2b$12$.hCTTgyZB6jYs3g1DtFBOebu4XHUqOIoYnckH2OB2XkL2CQ93vHy.',  -- Test1234
phone_number='+32 00-00-00-00',
height='1.80',
weight='85',
birth_date='1990-01-01'::date,
gender='Male',
url_profil_picture='client@gmail.com'
where id = 1;
update users set
id=2,
role_id=2,
first_name='Sam',
last_name='Wood',
email='admin@gmail.com',
password='$2b$12$.hCTTgyZB6jYs3g1DtFBOebu4XHUqOIoYnckH2OB2XkL2CQ93vHy.',  -- Test1234
phone_number='+32 00-00-00-00',
height='1.70',
weight='90',
birth_date='1980-01-01'::date,
gender='Female',
url_profil_picture='admin@gmail.com'
where id = 2;
select * from users;
