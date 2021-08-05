CREATE TABLE Worker(
 id serial PRIMARY KEY,
 name varchar(40) NOT NULL NULL,
 department integer NOT NULL,
 is_chief boolean NOT NULL
);

CREATE TABLE IF NOT EXISTS WorkerChief(
	id_woker integer REFERENCES Worker(id) ON DELETE CASCADE,
	id_chief integer REFERENCES Worker(id) ON DELETE CASCADE,
	CONSTRAINT WorkerChief_pk PRIMARY KEY (id_woker, id_chief)
);