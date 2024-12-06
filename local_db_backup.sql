--
-- PostgreSQL database dump
--

-- Dumped from database version 14.14 (Homebrew)
-- Dumped by pg_dump version 15.9 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: alenadocherty
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO alenadocherty;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: tasks; Type: TABLE; Schema: public; Owner: alenadocherty
--

CREATE TABLE public.tasks (
    id integer NOT NULL,
    description text,
    priority integer,
    due_date date,
    completed boolean DEFAULT false
);


ALTER TABLE public.tasks OWNER TO alenadocherty;

--
-- Name: tasks_id_seq; Type: SEQUENCE; Schema: public; Owner: alenadocherty
--

CREATE SEQUENCE public.tasks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tasks_id_seq OWNER TO alenadocherty;

--
-- Name: tasks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: alenadocherty
--

ALTER SEQUENCE public.tasks_id_seq OWNED BY public.tasks.id;


--
-- Name: tasks id; Type: DEFAULT; Schema: public; Owner: alenadocherty
--

ALTER TABLE ONLY public.tasks ALTER COLUMN id SET DEFAULT nextval('public.tasks_id_seq'::regclass);


--
-- Data for Name: tasks; Type: TABLE DATA; Schema: public; Owner: alenadocherty
--

COPY public.tasks (id, description, priority, due_date, completed) FROM stdin;
1	Finish project report	1	2023-11-15	f
2	Buy groceries	2	2023-11-16	f
3	Schedule doctor appointment	3	2023-11-17	f
4	Buy groceries	2	\N	f
9	Buy tickets	2	\N	f
22	Buy hat	2	\N	f
\.


--
-- Name: tasks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: alenadocherty
--

SELECT pg_catalog.setval('public.tasks_id_seq', 22, true);


--
-- Name: tasks tasks_pkey; Type: CONSTRAINT; Schema: public; Owner: alenadocherty
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_pkey PRIMARY KEY (id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: alenadocherty
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- Name: TABLE tasks; Type: ACL; Schema: public; Owner: alenadocherty
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.tasks TO assistant_user;


--
-- Name: SEQUENCE tasks_id_seq; Type: ACL; Schema: public; Owner: alenadocherty
--

GRANT SELECT,USAGE ON SEQUENCE public.tasks_id_seq TO assistant_user;


--
-- PostgreSQL database dump complete
--

