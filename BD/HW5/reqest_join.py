sqlalchemy
from sqlalchemy import create_engine


engine = create_engine(
    'postgresql://test:12345678@localhost:5432/music_websitedb')

connection = engine.connect()

# количество исполнителей в каждом жанре;
count_performers = connection.execute('''
    SELECT S.style_name, count(PS.id_performer)
    FROM Style S
    JOIN  PerformersStyle PS ON S.id = PS.id_style
    GROUP BY S.style_name
    ''').fetchall()
print()
print(count_performers)

# количество треков, вошедших в альбомы 2019-2020 годов;
count_treck_19_20 = connection.execute('''
    SELECT a.albom_name, a.release_year, count(t.id)
    FROM Albom a
    JOIN Tracks t ON a.id = t.id_albom
    WHERE a.release_year >= 2019 AND a.release_year <= 2020
    GROUP BY a.albom_name, a.release_year
    ''').fetchall()
print()
print(count_treck_19_20)

# средняя продолжительность треков по каждому альбому;
average_duration_track = connection.execute('''
    SELECT  a.albom_name, AVG(t.duration)
    FROM Albom a
    JOIN Tracks t ON a.id = t.id_albom
    GROUP BY a.albom_name
    ''').fetchall()
print()
print(average_duration_track)

# все исполнители, которые не выпустили альбомы в 2020 году;
performers_albom_no20 = connection.execute('''
    SELECT p.nickname, a.release_year
    FROM Performers p
    JOIN PerformersAlbom pa ON p.id = pa.id_performer
    JOIN Albom a ON pa.id_albom = a.id
    WHERE a.release_year != 2020
    ''').fetchall()
print()
print(performers_albom_no20)

# названия сборников, в которых присутствует конкретный исполнитель
# (выберите сами);
splin_in_collection = connection.execute('''
    SELECT DISTINCT c.titel
    FROM Collection c
    JOIN Collection_List cl ON c.id = cl.id_collection
    JOIN Tracks t ON cl.id_track = t.id
    JOIN Albom a ON t.id_albom = a.id
    JOIN PerformersAlbom pa ON a.id = pa.id_albom
    JOIN Performers p ON pa.id_performer = p.id
    WHERE p.nickname LIKE '%%Сплин%%'
    ''').fetchall()
print()
print(splin_in_collection)

# название альбомов, в которых присутствуют исполнители более 1 жанра;
albom_many_styles = connection.execute('''
     SELECT a.albom_name
     FROM Albom a
     JOIN PerformersAlbom pa ON a.id = pa.id_albom
     JOIN Performers p ON pa.id_performer = p.id
     JOIN PerformersStyle ps ON p.id = ps.id_performer
     GROUP BY p.nickname, a.albom_name
     HAVING count(ps.id_style) > 1
    ''').fetchall()
print()
print(albom_many_styles)

# наименование треков, которые не входят в сборники;
lonely_track = connection.execute('''
    SELECT t.track_name
    FROM Tracks t
    LEFT JOIN Collection_List cl ON t.id = cl.id_track
    where cl.id_track IS NULL
    ''').fetchall()
print
print(lonely_track)


# исполнителя(-ей), написавшего самый короткий по продолжительности трек
# (теоретически таких треков может быть несколько);
the_shortest_track = connection.execute('''
    SELECT p.nickname, t.duration
    FROM Performers p
    JOIN PerformersAlbom pa ON p.id = pa.id_performer
    JOIN Albom a ON pa.id_albom = a.id
    JOIN Tracks t ON a.id = t.id_albom
    WHERE t.duration IN (SELECT MIN(duration) FROM Tracks)
    ''').fetchall()
print()
print(the_shortest_track)

# название альбомов, содержащих наименьшее количество треков.
the_shortest_albome = connection.execute('''
    SELECT a.albom_name, count(t.id)
    FROM Albom a
    JOIN Tracks t  ON a.id = t.id_albom
    GROUP BY a.albom_name 
    HAVING count(t.id) in (
        SELECT count(t.id)
        FROM Albom a
        JOIN Tracks t  ON a.id = t.id_albom
        GROUP BY a.albom_name
        ORDER BY count(t.id)\
        LIMIT 1)
    ''').fetchall()
print()
print(the_shortest_albome)
