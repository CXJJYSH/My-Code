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

DROP DATABASE universe;
--
-- Name: universe; Type: DATABASE; Schema: -; Owner: freecodecamp
--

CREATE DATABASE universe WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C.UTF-8' LC_CTYPE = 'C.UTF-8';


ALTER DATABASE universe OWNER TO freecodecamp;

\connect universe

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: galaxy; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.galaxy (
    galaxy_id integer NOT NULL,
    name character varying(60),
    description text NOT NULL,
    has_life boolean NOT NULL,
    age_in_millions_of_years numeric(10,2)
);


ALTER TABLE public.galaxy OWNER TO freecodecamp;

--
-- Name: galaxy_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.galaxy_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.galaxy_id_seq OWNER TO freecodecamp;

--
-- Name: galaxy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.galaxy_id_seq OWNED BY public.galaxy.galaxy_id;


--
-- Name: moon; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.moon (
    moon_id integer NOT NULL,
    name character varying(60),
    description text NOT NULL,
    has_life boolean NOT NULL,
    age_in_millions_of_years integer,
    planet_id integer NOT NULL
);


ALTER TABLE public.moon OWNER TO freecodecamp;

--
-- Name: moon_moon_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.moon_moon_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.moon_moon_id_seq OWNER TO freecodecamp;

--
-- Name: moon_moon_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.moon_moon_id_seq OWNED BY public.moon.moon_id;


--
-- Name: planet; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.planet (
    planet_id integer NOT NULL,
    name character varying(60),
    description text NOT NULL,
    has_life boolean NOT NULL,
    age_in_millions_of_years numeric(10,2),
    star_id integer NOT NULL
);


ALTER TABLE public.planet OWNER TO freecodecamp;

--
-- Name: planet_planet_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.planet_planet_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.planet_planet_id_seq OWNER TO freecodecamp;

--
-- Name: planet_planet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.planet_planet_id_seq OWNED BY public.planet.planet_id;


--
-- Name: species; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.species (
    species_id integer NOT NULL,
    name character varying(60) NOT NULL,
    description text NOT NULL,
    age_in_millions_of_years integer
);


ALTER TABLE public.species OWNER TO freecodecamp;

--
-- Name: species_species_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.species_species_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.species_species_id_seq OWNER TO freecodecamp;

--
-- Name: species_species_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.species_species_id_seq OWNED BY public.species.species_id;


--
-- Name: star; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.star (
    star_id integer NOT NULL,
    name character varying(60),
    description text NOT NULL,
    has_life boolean NOT NULL,
    age_in_millions_of_years numeric(10,2),
    galaxy_id integer NOT NULL
);


ALTER TABLE public.star OWNER TO freecodecamp;

--
-- Name: star_star_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.star_star_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.star_star_id_seq OWNER TO freecodecamp;

--
-- Name: star_star_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.star_star_id_seq OWNED BY public.star.star_id;


--
-- Name: galaxy galaxy_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy ALTER COLUMN galaxy_id SET DEFAULT nextval('public.galaxy_id_seq'::regclass);


--
-- Name: moon moon_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon ALTER COLUMN moon_id SET DEFAULT nextval('public.moon_moon_id_seq'::regclass);


--
-- Name: planet planet_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet ALTER COLUMN planet_id SET DEFAULT nextval('public.planet_planet_id_seq'::regclass);


--
-- Name: species species_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.species ALTER COLUMN species_id SET DEFAULT nextval('public.species_species_id_seq'::regclass);


--
-- Name: star star_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star ALTER COLUMN star_id SET DEFAULT nextval('public.star_star_id_seq'::regclass);


--
-- Data for Name: galaxy; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.galaxy VALUES (1, 'Milky Way', 'Our home galaxy', true, 13600.00);
INSERT INTO public.galaxy VALUES (2, 'Andromeda', 'A nearby spiral galaxy', false, 10000.00);
INSERT INTO public.galaxy VALUES (3, 'Triangulum', 'A small spiral galaxy', false, 10000.00);
INSERT INTO public.galaxy VALUES (4, 'Large Magellanic Cloud', 'A satellite galaxy of the Milky Way', false, 13000.00);
INSERT INTO public.galaxy VALUES (5, 'Small Magellanic Cloud', 'A dwarf galaxy near the Milky Way', false, 13000.00);
INSERT INTO public.galaxy VALUES (6, 'Whirlpool Galaxy', 'A spiral galaxy with prominent arms', false, 10000.00);


--
-- Data for Name: moon; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.moon VALUES (1, 'Moon', 'Earth''s only natural satellite', false, 4530, 15);
INSERT INTO public.moon VALUES (2, 'Phobos', 'The larger and closer moon of Mars', false, 4500, 16);
INSERT INTO public.moon VALUES (3, 'Deimos', 'The smaller moon of Mars', false, 4500, 16);
INSERT INTO public.moon VALUES (4, 'Io', 'A volcanically active moon of Jupiter', false, 4500, 17);
INSERT INTO public.moon VALUES (5, 'Europa', 'An icy moon that may harbor a subsurface ocean', false, 4500, 17);
INSERT INTO public.moon VALUES (6, 'Ganymede', 'The largest moon in the Solar System', false, 4500, 17);
INSERT INTO public.moon VALUES (7, 'Callisto', 'A heavily cratered moon of Jupiter', false, 4500, 17);
INSERT INTO public.moon VALUES (8, 'Titan', 'Saturn''s largest moon with a thick atmosphere', false, 4500, 18);
INSERT INTO public.moon VALUES (9, 'Enceladus', 'An icy moon with water-rich plumes', false, 4500, 18);
INSERT INTO public.moon VALUES (10, 'Mimas', 'A small moon of Saturn with a large crater', false, 4500, 18);
INSERT INTO public.moon VALUES (11, 'Rhea', 'The second-largest moon of Saturn', false, 4500, 18);
INSERT INTO public.moon VALUES (12, 'Titania', 'The largest moon of Uranus', false, 4500, 19);
INSERT INTO public.moon VALUES (13, 'Oberon', 'A large icy moon of Uranus', false, 4500, 19);
INSERT INTO public.moon VALUES (14, 'Ariel', 'A moon of Uranus with a heavily fractured surface', false, 4500, 19);
INSERT INTO public.moon VALUES (15, 'Triton', 'Neptune''s largest moon with a retrograde orbit', false, 4500, 20);
INSERT INTO public.moon VALUES (16, 'Proteus', 'An irregularly shaped moon of Neptune', false, 4500, 20);
INSERT INTO public.moon VALUES (17, 'Nereid', 'A moon of Neptune with an eccentric orbit', false, 4500, 20);
INSERT INTO public.moon VALUES (18, 'Charon', 'The largest moon of Pluto', false, 4500, 21);
INSERT INTO public.moon VALUES (19, 'Dysnomia', 'The known moon of the dwarf planet Eris', false, 4500, 22);
INSERT INTO public.moon VALUES (20, 'Phobos Minor', 'A fictional small moon for database practice', false, 1000, 24);


--
-- Data for Name: planet; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.planet VALUES (13, 'Mercury', 'The smallest planet in the Solar System', false, 4500.00, 7);
INSERT INTO public.planet VALUES (14, 'Venus', 'The hottest planet in the Solar System', false, 4500.00, 7);
INSERT INTO public.planet VALUES (15, 'Earth', 'The only known planet to support life', true, 4540.00, 7);
INSERT INTO public.planet VALUES (16, 'Mars', 'A rocky planet known as the Red Planet', false, 4500.00, 7);
INSERT INTO public.planet VALUES (17, 'Jupiter', 'The largest planet in the Solar System', false, 4500.00, 8);
INSERT INTO public.planet VALUES (18, 'Saturn', 'A gas giant famous for its rings', false, 4500.00, 8);
INSERT INTO public.planet VALUES (19, 'Uranus', 'An ice giant that rotates on its side', false, 4500.00, 9);
INSERT INTO public.planet VALUES (20, 'Neptune', 'A distant ice giant with strong winds', false, 4500.00, 9);
INSERT INTO public.planet VALUES (21, 'Proxima Centauri b', 'An exoplanet orbiting Proxima Centauri', false, 4850.00, 10);
INSERT INTO public.planet VALUES (22, 'Kepler-22b', 'An exoplanet orbiting Kepler-22', false, 4000.00, 10);
INSERT INTO public.planet VALUES (23, 'Sirius b', 'A white dwarf companion of Sirius', false, 242.00, 11);
INSERT INTO public.planet VALUES (24, 'Vega b', 'A hypothetical planet orbiting Vega', false, 455.00, 12);


--
-- Data for Name: species; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.species VALUES (1, 'Animal', 'Multicellular organisms that consume organic matter', 800);
INSERT INTO public.species VALUES (2, 'Plant', 'Multicellular organisms that generally produce food through photosynthesis', 1000);
INSERT INTO public.species VALUES (3, 'Microorganism', 'Microscopic organisms including bacteria and archaea', 3500);


--
-- Data for Name: star; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.star VALUES (7, 'Sun', 'The star at the center of our solar system', true, 4600.00, 1);
INSERT INTO public.star VALUES (8, 'Proxima Centauri', 'The nearest known star to the Sun', false, 4850.00, 1);
INSERT INTO public.star VALUES (9, 'Sirius', 'The brightest star in Earth''s night sky', false, 242.00, 1);
INSERT INTO public.star VALUES (10, 'Vega', 'A bright star in the constellation Lyra', false, 455.00, 1);
INSERT INTO public.star VALUES (11, 'Betelgeuse', 'A red supergiant star', false, 10000.00, 1);
INSERT INTO public.star VALUES (12, 'Polaris', 'The North Star', false, 70000.00, 1);


--
-- Name: galaxy_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.galaxy_id_seq', 6, true);


--
-- Name: moon_moon_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.moon_moon_id_seq', 20, true);


--
-- Name: planet_planet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.planet_planet_id_seq', 24, true);


--
-- Name: species_species_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.species_species_id_seq', 3, true);


--
-- Name: star_star_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.star_star_id_seq', 12, true);


--
-- Name: galaxy galaxy_description_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_description_key UNIQUE (description);


--
-- Name: galaxy galaxy_galaxy_id_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_galaxy_id_key UNIQUE (galaxy_id);


--
-- Name: galaxy galaxy_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_pkey PRIMARY KEY (galaxy_id);


--
-- Name: moon moon_moon_id_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_moon_id_key UNIQUE (moon_id);


--
-- Name: moon moon_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_pkey PRIMARY KEY (moon_id);


--
-- Name: planet planet_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_pkey PRIMARY KEY (planet_id);


--
-- Name: planet planet_planet_id_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_planet_id_key UNIQUE (planet_id);


--
-- Name: species species_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.species
    ADD CONSTRAINT species_pkey PRIMARY KEY (species_id);


--
-- Name: species species_species_id_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.species
    ADD CONSTRAINT species_species_id_key UNIQUE (species_id);


--
-- Name: star star_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_pkey PRIMARY KEY (star_id);


--
-- Name: star star_star_id_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_star_id_key UNIQUE (star_id);


--
-- Name: moon moon_planet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_planet_id_fkey FOREIGN KEY (planet_id) REFERENCES public.planet(planet_id);


--
-- Name: planet planet_star_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_star_id_fkey FOREIGN KEY (star_id) REFERENCES public.star(star_id);


--
-- Name: star star_galaxy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_galaxy_id_fkey FOREIGN KEY (galaxy_id) REFERENCES public.galaxy(galaxy_id);


--
-- PostgreSQL database dump complete
--

