-- public.flats definition

-- Drop table

-- DROP TABLE public.flats;

CREATE TABLE public.flats (
	id int8 NOT NULL GENERATED ALWAYS AS IDENTITY,
	title varchar NOT NULL,
	imageurl varchar NOT NULL
);
