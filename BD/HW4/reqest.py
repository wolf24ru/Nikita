
from sqlalchemy import create_engine


engine = create_engine(
    'postgresql://test:12345678@localhost:5432/music_websitedb')

connection = engine.connect()

# название и год выхода альбомов, вышедших в 2018 году;
albom_in_2018 = connection.execute('''SELECT albom_name, release_year
    FROM Albom
    WHERE release_year = 2018
    ''').fetchall()
print()
print(albom_in_2018)

# название и продолжительность самого длительного трека;
max_long_tack = connection.execute('''SELECT track_name, duration 
    FROM Tracks
    ORDER BY duration DESC;
    ''').fetchone()
print()
print(max_long_tack)

# название треков, продолжительность которых не менее 3,5 минуты(210сек);
long_tack = connection.execute('''SELECT track_name, duration
    FROM Tracks
    WHERE duration > 210''').fetchall()
print()
print(long_tack)

# названия сборников, вышедших в период с 2018 по 2020 год включительно;
colection_between = connection.execute('''SELECT titel
    FROM Collection
    WHERE year BETWEEN 2018 AND 2020''').fetchall()
print()
print(colection_between)

# исполнители, чье имя состоит из 1 слова;
nickname_one_word = connection.execute('''SELECT surname, name, nickname
    FROM Performers
    WHERE nickname NOT LIKE '%% %%';''').fetchall()
print()
print(nickname_one_word)

# название треков, которые содержат слово "мой"/"my".
my_track = connection.execute('''SELECT track_name
    FROM Tracks
    WHERE track_name LIKE '%%my%%' OR track_name LIKE '%%мой%%';''').fetchall()
print()
print(my_track)
