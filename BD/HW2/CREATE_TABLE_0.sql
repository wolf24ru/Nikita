CREATE TABLE Style(
 id serial primary key,
 style_name varchar(60) not null unique
);
 
CREATE TABLE Performers(
	id serial primary key,
	surname varchar(40) not null,
	name varchar(40) not null,
	birth_year date not null,
	nickname varchar(100),
	id_style integer references Style(id)
);

CREATE TABLE Albom(
	id serial primary key,
	id_performer integer references Performers(id),
	albom_name varchar(150) not null,
	release_year date not null
);

CREATE TABLE Tracks(
	id serial primary key,
	id_albom integer references Albom(id),
	track_name varchar(150) not null,
	duration time without time zone not null
);
