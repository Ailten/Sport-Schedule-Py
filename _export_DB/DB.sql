--
-- PostgreSQL database dump
--

\restrict 0377iQMun2jaRNm0IszzdvlpsAHnxA0aWix0frMmO7bU2BFzaACfqQ2yWFWI3vJ

-- Dumped from database version 18.3
-- Dumped by pg_dump version 18.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: pgcrypto; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pgcrypto WITH SCHEMA public;


--
-- Name: EXTENSION pgcrypto; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgcrypto IS 'cryptographic functions';


--
-- Name: gender; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.gender AS ENUM (
    'Male',
    'Female',
    'Other'
);


ALTER TYPE public.gender OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: check_exercices; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.check_exercices (
    id integer NOT NULL,
    exercice_to_do_id integer NOT NULL,
    date_check timestamp without time zone NOT NULL
);


ALTER TABLE public.check_exercices OWNER TO postgres;

--
-- Name: check_exercices_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.check_exercices_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.check_exercices_id_seq OWNER TO postgres;

--
-- Name: check_exercices_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.check_exercices_id_seq OWNED BY public.check_exercices.id;


--
-- Name: exercice_to_dos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.exercice_to_dos (
    id integer NOT NULL,
    schedule_id integer NOT NULL,
    exercice_id integer NOT NULL,
    days_of_week integer NOT NULL,
    repetition integer NOT NULL,
    series integer NOT NULL,
    additional_weight double precision NOT NULL,
    CONSTRAINT days_of_week_range CHECK (((days_of_week >= 1) AND (days_of_week <= 127))),
    CONSTRAINT repetition_min CHECK ((repetition > 0)),
    CONSTRAINT series_min CHECK ((series > 0))
);


ALTER TABLE public.exercice_to_dos OWNER TO postgres;

--
-- Name: exercice_to_dos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.exercice_to_dos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.exercice_to_dos_id_seq OWNER TO postgres;

--
-- Name: exercice_to_dos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.exercice_to_dos_id_seq OWNED BY public.exercice_to_dos.id;


--
-- Name: exercices; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.exercices (
    id integer NOT NULL,
    name character varying NOT NULL,
    description character varying,
    url_details character varying,
    url_image character varying,
    amplitude double precision NOT NULL,
    is_minutes boolean NOT NULL,
    CONSTRAINT amplitude_range CHECK (((amplitude >= (0.0)::double precision) AND (amplitude <= (1.0)::double precision))),
    CONSTRAINT name_format CHECK (((name)::text ~ '[a-zA-Z_ -]{4,}'::text)),
    CONSTRAINT url_details_format CHECK ((((url_details)::text = NULL::text) OR ((url_details)::text ~ '^https://.*(.html)'::text))),
    CONSTRAINT url_image_format CHECK ((((url_image)::text = NULL::text) OR ((url_image)::text ~ '^https://.*(.png|.jpg|.jpeg|.webp)'::text)))
);


ALTER TABLE public.exercices OWNER TO postgres;

--
-- Name: exercices_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.exercices_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.exercices_id_seq OWNER TO postgres;

--
-- Name: exercices_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.exercices_id_seq OWNED BY public.exercices.id;


--
-- Name: roles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.roles (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.roles OWNER TO postgres;

--
-- Name: roles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.roles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.roles_id_seq OWNER TO postgres;

--
-- Name: roles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.roles_id_seq OWNED BY public.roles.id;


--
-- Name: schedules; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.schedules (
    id integer NOT NULL,
    user_id integer NOT NULL,
    start_date date NOT NULL,
    end_date date,
    CONSTRAINT end_date_min CHECK (((end_date = NULL::date) OR (end_date > start_date)))
);


ALTER TABLE public.schedules OWNER TO postgres;

--
-- Name: schedules_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.schedules_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.schedules_id_seq OWNER TO postgres;

--
-- Name: schedules_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.schedules_id_seq OWNED BY public.schedules.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    role_id integer NOT NULL,
    first_name character varying NOT NULL,
    last_name character varying NOT NULL,
    email character varying NOT NULL,
    password character varying NOT NULL,
    phone_number character varying NOT NULL,
    height double precision NOT NULL,
    weight double precision NOT NULL,
    birth_date date NOT NULL,
    gender public.gender NOT NULL,
    url_profil_picture character varying,
    CONSTRAINT birth_date_min CHECK ((birth_date < CURRENT_DATE)),
    CONSTRAINT email_format CHECK (((email)::text ~ '^.*@.*\..*$'::text)),
    CONSTRAINT height_min CHECK ((height > (0)::double precision)),
    CONSTRAINT phone_number_format CHECK (((phone_number)::text ~ '^[0-9 +-]*$'::text)),
    CONSTRAINT weight_min CHECK ((weight > (0)::double precision))
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: check_exercices id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.check_exercices ALTER COLUMN id SET DEFAULT nextval('public.check_exercices_id_seq'::regclass);


--
-- Name: exercice_to_dos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exercice_to_dos ALTER COLUMN id SET DEFAULT nextval('public.exercice_to_dos_id_seq'::regclass);


--
-- Name: exercices id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exercices ALTER COLUMN id SET DEFAULT nextval('public.exercices_id_seq'::regclass);


--
-- Name: roles id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles ALTER COLUMN id SET DEFAULT nextval('public.roles_id_seq'::regclass);


--
-- Name: schedules id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.schedules ALTER COLUMN id SET DEFAULT nextval('public.schedules_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
80a183130b56
\.


--
-- Data for Name: check_exercices; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.check_exercices (id, exercice_to_do_id, date_check) FROM stdin;
1	1	2026-06-01 00:00:00
2	1	2026-06-08 00:00:00
3	1	2026-06-15 00:00:00
4	1	2026-06-22 00:00:00
5	1	2026-07-06 00:00:00
6	1	2026-07-13 00:00:00
\.


--
-- Data for Name: exercice_to_dos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.exercice_to_dos (id, schedule_id, exercice_id, days_of_week, repetition, series, additional_weight) FROM stdin;
1	1	1	1	20	3	0
\.


--
-- Data for Name: exercices; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.exercices (id, name, description, url_details, url_image, amplitude, is_minutes) FROM stdin;
1	Pompes	\N	\N	\N	0.7	f
2	Squat	\N	\N	\N	1	f
3	Tractions	\N	\N	\N	1	f
4	Abdominaux	\N	\N	\N	0.3	f
5	Burpees	\N	\N	\N	1	f
6	Bench-press	\N	\N	\N	0	f
7	Curl	\N	\N	\N	0	f
8	Curl-forearms	\N	\N	\N	0	f
9	Abdominaux-oblic	\N	\N	\N	0.12	f
10	Dead-lift	\N	\N	\N	0	f
11	Pistol-squat	\N	\N	\N	1	f
12	Mollet	\N	\N	\N	1	f
13	Curl-shoulders	\N	\N	\N	0	f
14	Dips	\N	\N	\N	1	f
\.


--
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.roles (id, name) FROM stdin;
1	client
2	admin
\.


--
-- Data for Name: schedules; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.schedules (id, user_id, start_date, end_date) FROM stdin;
1	1	2026-05-27	\N
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, role_id, first_name, last_name, email, password, phone_number, height, weight, birth_date, gender, url_profil_picture) FROM stdin;
2	2	Sam	Wood	admin@gmail.com	$2b$12$.hCTTgyZB6jYs3g1DtFBOebu4XHUqOIoYnckH2OB2XkL2CQ93vHy.	+32 00-00-00-00	1.7	90	1980-01-01	Female	admin@gmail.com
1	1	Thomas	Du-puits	client@gmail.com	$2b$12$.hCTTgyZB6jYs3g1DtFBOebu4XHUqOIoYnckH2OB2XkL2CQ93vHy.	+32 00-00-00-00	1.8	85	1990-01-01	Male	client@gmail.com
\.


--
-- Name: check_exercices_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.check_exercices_id_seq', 6, true);


--
-- Name: exercice_to_dos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.exercice_to_dos_id_seq', 1, true);


--
-- Name: exercices_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.exercices_id_seq', 1, false);


--
-- Name: roles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.roles_id_seq', 1, false);


--
-- Name: schedules_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.schedules_id_seq', 1, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 3, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: check_exercices check_exercices_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.check_exercices
    ADD CONSTRAINT check_exercices_pkey PRIMARY KEY (id);


--
-- Name: exercice_to_dos exercice_to_dos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exercice_to_dos
    ADD CONSTRAINT exercice_to_dos_pkey PRIMARY KEY (id);


--
-- Name: exercices exercices_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exercices
    ADD CONSTRAINT exercices_name_key UNIQUE (name);


--
-- Name: exercices exercices_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exercices
    ADD CONSTRAINT exercices_pkey PRIMARY KEY (id);


--
-- Name: roles roles_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_name_key UNIQUE (name);


--
-- Name: roles roles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id);


--
-- Name: schedules schedules_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.schedules
    ADD CONSTRAINT schedules_pkey PRIMARY KEY (id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: check_exercices check_exercices_exercice_to_do_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.check_exercices
    ADD CONSTRAINT check_exercices_exercice_to_do_id_fkey FOREIGN KEY (exercice_to_do_id) REFERENCES public.exercice_to_dos(id);


--
-- Name: exercice_to_dos exercice_to_dos_exercice_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exercice_to_dos
    ADD CONSTRAINT exercice_to_dos_exercice_id_fkey FOREIGN KEY (exercice_id) REFERENCES public.exercices(id);


--
-- Name: exercice_to_dos exercice_to_dos_schedule_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exercice_to_dos
    ADD CONSTRAINT exercice_to_dos_schedule_id_fkey FOREIGN KEY (schedule_id) REFERENCES public.schedules(id);


--
-- Name: schedules schedules_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.schedules
    ADD CONSTRAINT schedules_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: users users_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_role_id_fkey FOREIGN KEY (role_id) REFERENCES public.roles(id);


--
-- PostgreSQL database dump complete
--

\unrestrict 0377iQMun2jaRNm0IszzdvlpsAHnxA0aWix0frMmO7bU2BFzaACfqQ2yWFWI3vJ

