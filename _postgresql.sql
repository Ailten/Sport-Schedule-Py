
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
(5, 'Burpees', null, null, null, 1.0, false),
(6, 'Bench-press', null, null, null, 0.0, false),
(7, 'Curl', null, null, null, 0.0, false),
(8, 'Curl-forearms', null, null, null, 0.0, false),
(9, 'Abdominaux-oblic', null, null, null, 0.12, false),
--(10, 'Full-plank', null, null, null, 1.0, true),
(10, 'Dead-lift', null, null, null, 0.0, false),
(11, 'Pistol-squat', null, null, null, 1.0, false),
(12, 'Mollet', null, null, null, 1.0, false),
--(13, 'L-stand', null, null, null, 1.0, true),
(13, 'Curl-shoulders', null, null, null, 0.0, false),
(14, 'Dips', null, null, null, 1.0, false);
select * from exercices;

truncate table schedules restart identity cascade;
insert into schedules(id, user_id, start_date, end_date) values
(1, 1, '2026-05-01'::date, Null);
select * from schedules;

truncate table exercice_to_dos restart identity cascade;
insert into exercice_to_dos(id, schedule_id, exercice_id, days_of_week, repetition, series, additional_weight) values
(1, 1, 1, 1, 30, 2, 0.0), -- pompe lundi.
(5, 1, 6, 1, 30, 1, 20.0),
(6, 1, 7, 1, 110, 3, 5.0),
(2, 1, 4, 2, 20, 2, 0.0), -- abdo mardi.
(7, 1, 9, 2, 20, 2, 0.0),
--(8, 1, 10, 2, 20, 2, 0.0),
(8, 1, 10, 4, 12, 1, 20.0), -- dos mercredi.
(9, 1, 10, 4, 12, 1, 30.0),
(10, 1, 10, 4, 12, 1, 40.0),
(11, 1, 9, 4, 12, 3, 10.0),
(12, 1, 11, 8, 5, 2, 0.0), -- squat jeudi.
(3, 1, 2, 8, 12, 3, 9.0),
(13, 1, 12, 8, 30, 6, 29.0),
--(14, 1, 13, 16, 5, 3, 0.0), -- L-stand vendredi.
(14, 1, 13, 16, 12, 3, 10.0),
(4, 1, 3, 32, 12, 3, 10.0), -- traction samedi.
(15, 1, 7, 32, 12, 3, 10.0),
(16, 1, 14, 64, 12, 3, 0.0); -- dips dimanche.
select * from exercice_to_dos;

truncate table check_exercices restart identity cascade;
insert into check_exercices(id, exercice_to_do_id, date_check) values
(1, 1, '2026-05-18'::date),
(2, 5, '2026-05-18'::date),
(3, 6, '2026-05-18'::date);
select * from check_exercices;

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


--select extract(day from jour)::integer as jour_du_mois
--from generate_series(
--    '2026-05-01'::date,
--    ('2026-05-01'::date + interval '1 month' - interval '1 day')::date,
--    interval '1 day'
--) as jour;

insert into check_exercices(exercice_to_do_id, date_check) values
(1, '2026-05-04'::date);
select * from check_exercices;

--SELECT *
--FROM exercice_to_dos
--    JOIN schedules ON schedules.id = exercice_to_dos.schedule_id
--    LEFT JOIN check_exercices ON check_exercices.exercice_to_do_id = exercice_to_dos.id AND check_exercices.date_check = '2026-05-04'::date
--WHERE schedules.start_date <= '2026-05-04'::date
--  AND check_exercices is NULL
--  AND (schedules.end_date IS NULL OR schedules.end_date >= '2026-05-04'::date)
--  AND (exercice_to_dos.days_of_week & 1 > 0);
