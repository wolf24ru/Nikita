from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://test:12345678@localhost:5432/music_websitedb')

connection = engine.connect()

# Создание  5 жанров
connection.execute(''' INSERT INTO Style
	VALUES("Классика"); 1
	VALUES("Кантри");
	VALUES("Поп");3
	VALUES("Рок-н-ролл");
	VALUES("Джаз");
	VALUES("Блюз"); 6
	''')

# Создание  8 исполнителей
connection.execute(''' INSERT INTO Performers
	VALUES("Иванцив", "Елизавета", 02.06.1982, "Ёлка");
	VALUES("Billie", "Eilish", 18.12.2001, "Billie Eilish");
	VALUES("Louis", "Daniel Armstrong", 04.08.1901, "Louis Armstrong");
	VALUES("Елизавета", "Гырдымова", 01.06.1998, "Монеточка");
	VALUES("Александр", "Васильев", 15.07.1969, "Сплин");
	VALUES("Рустем", "Булатов", 26.07.1980, "Lumen");
	VALUES("Бетховен", "Людвиг ван", 16.12.1770, "Ludwig van Beethoven");
	VALUES("Алан", "Джексон", 17.10.1958, "Alan Eugene Jackson");
	VALUES("Riley", "B. King", 16.09.1925, "B. B. King");
	''')

# Соотношение исполнитель - жанр
connection.execute('''INSERT INTO PerformersStyle
	VALUES(1,3);
	VALUES(2,3);
	VALUES(3,5);
	VALUES(4,3);
	VALUES(5,4);
	VALUES(6,4);
	VALUES(7,1);
	VALUES(8,5);
	VALUES(9,6); 
	''')

# Создание 8 сборников
connection.execute('''INSERT INTO Collection
	VALUES("классика жанра",2000); 
	''')

# Создание  8 альбомов
connection.execute(''' 
	''')

# Создание  15 треков
connection.execute(''' 
	''')

# Соотношение сборник - трек
connection.execute(''' 
	''')

# Соотношение исполнитель - альбом
connection.execute(''' 
	''')
