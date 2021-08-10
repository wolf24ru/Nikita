from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://test:12345678@localhost:5432/music_websitedb')

connection = engine.connect()

# connection.execute('DELETE FROM Style')
Создание  5 жанров
connection.execute('''INSERT INTO Style(style_name)
	VALUES ('Классика'),
	('Кантри'),
	('Поп'),
	('Рок-н-ролл'),
	('Джаз'),
	('Блюз'); 
	''')

# Создание  8 исполнителей
connection.execute(''' INSERT INTO Performers(surname, name, birth_year, nickname)
	VALUES ('Иванцив', 'Елизавета', '1982-06-02', 'Ёлка'),
	('Billie', 'Eilish', '2001-12-18', 'Billie Eilish'),
	('Louis', 'Daniel Armstrong', '1901-08-04', 'Louis Armstrong'),
	('Елизавета', 'Гырдымова', '1998-06-01', 'Монеточка'),
	('Александр', 'Васильев', '1969-07-15', 'Сплин'),
	('Рустем', 'Булатов', '1980-07-26', 'Lumen'),
	('Бетховен', 'Людвиг ван', '1770-12-16', 'Ludwig van Beethoven'),
	('Алан', 'Джексон', '1958-10-17', 'Alan Eugene Jackson'),
	('Riley', 'B. King', '1925-09-16', 'B. B. King');
	''')

# # Соотношение исполнитель - жанр
connection.execute('''INSERT INTO PerformersStyle
	VALUES(1, 3),
	(2, 3),
	(3, 5),
	(4, 3),
	(5, 4),
	(6, 4),
	(7, 1),
	(8, 5),
	(9, 6);
	''')

# # Создание 8 сборников
connection.execute('''INSERT INTO Collection(titel, year)
	VALUES('классика жанра', 2000),
	('лучшее', 2010),
	('какое-то название', 2006),
	('песни молодости', 2007),
	('Грустная музыка', 2014),
	('под настроение', 2020),
	('для спорта', 2021),
	('для фона', 1995);
	''')

# # Создание  8 альбомов
connection.execute(''' INSERT INTO Albom(albom_name, release_year)
	VALUES('Past Perfect', 2020), --елка
	('WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?', 2019), --Billie Eilish
	('Loving You', 1957), --Louis Armstrong
	('Раскраски для взрослых', 2018), --Монеточка
	('Новые люди', 2003), --Сплин
	('Правда?', 2007), --Lumen
	('Airs célèbres du monde entier', 1900), --Ludwig van Beethoven
	('The Greatest Hits Collection', 1995), --Alan Eugene Jackson
	('Every day I have the blues', 2011); --B. B. King
	''')

# # Создание  15 треков
connection.execute('''INSERT INTO Tracks(id_albom, track_name, duration)
	VALUES(1, 'Я не такая, как вы!', 215), --Past Perfect
	(1, 'Синтетический мир', 251), --Past Perfect
	(1, 'Под восьмеркой', 215), --Past Perfect
	(2, 'bad guy', 188), --WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?
	(2, 'you should see me in a crown', 180), --WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?
	(2, 'ilomilo', 142), --WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?
	(3, 'Hot Dog', 67), --Loving You
	(3, 'All Shook Up', 120), --Loving You
	(3, 'Loving You', 129), --Loving You
	(4, 'Каждый раз', 197), --Раскраски для взрослых
	(4, 'Нимфоманка', 144), --Раскраски для взрослых
	(4, 'Нет монет', 263), --Раскраски для взрослых
	(5, 'Новые люди', 206), --Новые люди
	(5, 'Время, назад!', 247), --Новые люди
	(5, 'Девятиэтажный дом', 258), --Новые люди
	(6, 'Далеко', 197), --Правда?
	(6, 'Хватит!', 196), --Правда?
	(6, 'Гореть', 311), --Правда?
	(7, 'The Bat: Overture', 500), --Airs célèbres du monde entier
	(7, 'Carmen: Habanera', 136), --Airs célèbres du monde entier
	(7, 'El Amor Brujo: Ritual Fire Dance', 206), --Airs célèbres du monde entier
	(8, 'Gone Country', 251), --The Greatest Hits Collection
	(8, 'Tall, Tall Trees', 137), --The Greatest Hits Collection
	(8, 'Mercury Blues', 203), --The Greatest Hits Collection
	(9, 'Please Love Me', 151), --Every day I have the blues
	(9, 'Blind Love', 184), --Every day I have the blues
	(9, 'Sweet Little Angel', 180) --Every day I have the blues
''')

# Соотношение сборник - трек
connection.execute('''INSERT INTO Collection_List
	VALUES(1, 19),
	(1, 20),
	(1, 21),
	(1, 25),
	(1, 26),
	(1, 27),
	(2, 1),
	(2, 18),
	(2, 14),
	(2, 4),
	(2, 12),
	(2, 19),
	(3, 1),
	(3, 5),
	(3, 14),
	(3, 20),
	(3, 25),
	(4, 13),
	(4, 14),
	(4, 15),
	(4, 16),
	(4, 17),
	(4, 18),
	(5, 13),
	(5, 14),
	(5, 15),
	(5, 16),
	(5, 25),
	(5, 26),
	(6, 2),
	(6, 8),
	(6, 10),
	(6, 3),
	(6, 15),
	(7, 15),
	(7, 16),
	(7, 17),
	(7, 4),
	(7, 5),
	(7, 6),
	(7, 12),
	(7, 10),
	(8, 1),
	(8, 2),
	(8, 3),
	(8, 19),
	(8, 20),
	(8, 21),
	(8, 8);
	''')

# Соотношение исполнитель - альбом
connection.execute('''INSERT INTO PerformersAlbom
	VALUES(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
	(6, 6),
	(7, 7),
	(8, 8),
	(9, 9),
	(4, 6);
''')