CREATE TABLE Style(
 id serial PRIMARY KEY,
 style_name varchar(60) NOT NULL UNIQUE
);

CREATE TABLE Collection(
	id serial PRIMARY KEY,
	titel varchar(60) NOT NULL,
	year date NOT NULL
);

CREATE TABLE Performers(
	id serial PRIMARY KEY,
	surname varchar(40) NOT NULL,
	name varchar(40) NOT NULL,
	birth_year date NOT NULL,
	nickname varchar(100),
	id_style integer REFERENCES Style(id)
);

CREATE TABLE IF NOT EXISTS PerformersStyle (
	id_performer integer REFERENCES Performers(id) ON DELETE CASCADE,
	id_style integer REFERENCES Style(id) ON DELETE CASCADE,
	CONSTRAINT PerformersStyle_pk PRIMARY KEY (id_performer, id_style)
);

CREATE TABLE Albom(
	id serial PRIMARY KEY,
	id_performer integer REFERENCES Performers(id),
	albom_name varchar(150) NOT NULL,
	release_year date NOT NULL
);

CREATE TABLE Tracks(
	id serial PRIMARY KEY,
	id_albom integer REFERENCES Albom(id) ON DELETE CASCADE,
	track_name varchar(150) NOT NULL,
	duration time without time zone NOT NULL
);

CREATE TABLE IF NOT EXISTS PerformersAlbom(
	id_performer integer REFERENCES Performers(id) ON DELETE CASCADE,
	id_albom integer REFERENCES Albom(id) ON DELETE CASCADE,
	CONSTRAINT PerformersAlbom_pk PRIMARY KEY (id_performer, id_albom)
);

CREATE TABLE IF NOT EXISTS Collection_List(
	id_collection integer REFERENCES Collection(id) ON DELETE CASCADE,
	id_track integer REFERENCES Tracks(id) ON DELETE CASCADE,
	CONSTRAINT Collection_List_pk PRIMARY KEY (id_collection, id_track)
);
