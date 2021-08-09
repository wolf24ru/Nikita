from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://test:12345678@localhost:5432/music_websitedb')

connection = engine.connect()

# Создание  5 жанров
connection.execute(''' 
	''')

# Соотношение исполнитель - жанр
connection.execute(''' 
	''')

# Создание  8 исполнителей
connection.execute(''' 
	''')

# Создание 8 сборников
connection.execute(''' 
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
