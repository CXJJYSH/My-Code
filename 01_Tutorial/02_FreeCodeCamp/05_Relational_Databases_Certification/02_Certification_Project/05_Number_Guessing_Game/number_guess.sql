--
-- PostgreSQL database dump
--

-- Dumped from database version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)
-- Dumped by pg_dump version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)

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

DROP DATABASE postgres;
--
-- Name: postgres; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C.UTF-8' LC_CTYPE = 'C.UTF-8';


ALTER DATABASE postgres OWNER TO postgres;

\connect postgres

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
-- Name: DATABASE postgres; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: games; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.games (
    game_id integer NOT NULL,
    user_id integer NOT NULL,
    number_of_guesses integer NOT NULL
);


ALTER TABLE public.games OWNER TO freecodecamp;

--
-- Name: games_game_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.games_game_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.games_game_id_seq OWNER TO freecodecamp;

--
-- Name: games_game_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.games_game_id_seq OWNED BY public.games.game_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    username character varying(22) NOT NULL
);


ALTER TABLE public.users OWNER TO freecodecamp;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO freecodecamp;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: games game_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.games ALTER COLUMN game_id SET DEFAULT nextval('public.games_game_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: games; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.games VALUES (1, 1, 467);
INSERT INTO public.games VALUES (2, 2, 529);
INSERT INTO public.games VALUES (3, 1, 768);
INSERT INTO public.games VALUES (4, 1, 439);
INSERT INTO public.games VALUES (5, 1, 379);
INSERT INTO public.games VALUES (6, 4, 325);
INSERT INTO public.games VALUES (7, 5, 385);
INSERT INTO public.games VALUES (8, 4, 513);
INSERT INTO public.games VALUES (9, 4, 157);
INSERT INTO public.games VALUES (10, 4, 828);
INSERT INTO public.games VALUES (11, 6, 1);
INSERT INTO public.games VALUES (12, 7, 249);
INSERT INTO public.games VALUES (13, 7, 883);
INSERT INTO public.games VALUES (14, 8, 984);
INSERT INTO public.games VALUES (15, 8, 427);
INSERT INTO public.games VALUES (16, 7, 466);
INSERT INTO public.games VALUES (17, 7, 306);
INSERT INTO public.games VALUES (18, 7, 677);
INSERT INTO public.games VALUES (19, 6, 1);
INSERT INTO public.games VALUES (20, 9, 958);
INSERT INTO public.games VALUES (21, 10, 115);
INSERT INTO public.games VALUES (22, 9, 348);
INSERT INTO public.games VALUES (23, 9, 422);
INSERT INTO public.games VALUES (24, 9, 693);
INSERT INTO public.games VALUES (25, 11, 789);
INSERT INTO public.games VALUES (26, 11, 886);
INSERT INTO public.games VALUES (27, 12, 502);
INSERT INTO public.games VALUES (28, 12, 904);
INSERT INTO public.games VALUES (29, 11, 730);
INSERT INTO public.games VALUES (30, 11, 612);
INSERT INTO public.games VALUES (31, 11, 697);
INSERT INTO public.games VALUES (32, 13, 106);
INSERT INTO public.games VALUES (33, 13, 609);
INSERT INTO public.games VALUES (34, 14, 457);
INSERT INTO public.games VALUES (35, 14, 967);
INSERT INTO public.games VALUES (36, 13, 970);
INSERT INTO public.games VALUES (37, 13, 984);
INSERT INTO public.games VALUES (38, 13, 977);
INSERT INTO public.games VALUES (39, 15, 11);
INSERT INTO public.games VALUES (40, 16, 20);
INSERT INTO public.games VALUES (41, 16, 353);
INSERT INTO public.games VALUES (42, 17, 849);
INSERT INTO public.games VALUES (43, 17, 786);
INSERT INTO public.games VALUES (44, 16, 712);
INSERT INTO public.games VALUES (45, 16, 619);
INSERT INTO public.games VALUES (46, 16, 500);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.users VALUES (1, 'user_1795668117697');
INSERT INTO public.users VALUES (2, 'user_1795668117696');
INSERT INTO public.users VALUES (3, 'asdf');
INSERT INTO public.users VALUES (4, 'user_1795668539588');
INSERT INTO public.users VALUES (5, 'user_1795668539587');
INSERT INTO public.users VALUES (6, 'a');
INSERT INTO public.users VALUES (7, 'user_1795668787265');
INSERT INTO public.users VALUES (8, 'user_1795668787264');
INSERT INTO public.users VALUES (9, 'user_1795668892574');
INSERT INTO public.users VALUES (10, 'user_1795668892573');
INSERT INTO public.users VALUES (11, 'user_1795668916228');
INSERT INTO public.users VALUES (12, 'user_1795668916227');
INSERT INTO public.users VALUES (13, 'user_1795669040467');
INSERT INTO public.users VALUES (14, 'user_1795669040466');
INSERT INTO public.users VALUES (15, 'A');
INSERT INTO public.users VALUES (16, 'user_1795669174456');
INSERT INTO public.users VALUES (17, 'user_1795669174455');


--
-- Name: games_game_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.games_game_id_seq', 46, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.users_user_id_seq', 17, true);


--
-- Name: games games_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.games
    ADD CONSTRAINT games_pkey PRIMARY KEY (game_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: games games_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.games
    ADD CONSTRAINT games_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

--
-- 2026.11.26 13:02
--