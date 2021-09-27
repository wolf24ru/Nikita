from sqlalchemy import create_engine


class VKinder_db:
    def __init__(self, user: str, password: str, db: str, port=5432):
        '''
		Подключение к БД
		:param user: Имя пользователя БД
		:param password: Пороль пользователя БД
		:param db: Имя БД
		:param port: Порт подключения (по умольчанию 5432)
		'''
        engine = create_engine(
            f'postgresql://{user}:{password}@localhost:{port}/{db}')
        self.connection = engine.connect()

    # engine = create_engine(
    # 	'postgresql://vk:12345678@localhost:5432/vkinder_db')
    # connection = engine.connect()

    # 	создание баззы с минимальными значениями
    def new_db(self):
	'''
		Создания  баззы с нуля если она не созданна или поврежденна.
	'''
        # создание таблицы для пользователей
        self.connection.execute('''
		CREATE TABLE IF NOT EXISTS User_table(
			id_user varchar(20) primary key,
			name_user varchar(40)
		);
		''')

        # таблица 'семеное положение'
        self.connection.execute('''
		CREATE TABLE IF NOT EXISTS Marital_Status(
			id_status serial primary key,
			marital_status varchar
		);
		''')

        # таблица 'запросы польщователя'
        self.connection.execute('''
	CREATE TABLE IF NOT EXISTS User_request(
		request_id serial NOT NULL,
		id_user varchar references User_table(id_user) ON DELETE CASCADE,
		age integer not null,
		sex integer CHECK
			( sex>=0 and sex<=2),
		city varchar not null,
		marital_status integer references Marital_Status(id_status),
		CONSTRAINT User_request_pk PRIMARY KEY (request_id, id_user)
	);
		''')
        # таблица 'найденные пользователи для запрашеваемого'
        self.connection.execute('''
	CREATE TABLE IF NOT EXISTS Search_users(
		id_search serial NOT NULL,
		search_user_id varchar NOT NULL,
		to_id_user varchar references User_table(id_user) ON DELETE CASCADE,
		age integer not null,
		sex integer not null,
		city varchar not null,
		marital_status integer references Marital_Status(id_status),
		CONSTRAINT Search_users_pk PRIMARY KEY (id_search, search_user_id)
		);
		''')

        # дефолтное запролнение таблицы 'семейное положенение'
        self.connection.execute('''
	INSERT INTO Marital_Status(marital_status)
		VALUES ('не женат (не замужем)'),
		('встречается'),
		('помолвлен(-а)'),
		('женат (замужем)'),
		('всё сложно'),
		('в активном поиске'),
		('влюблен(-а)'),
		('в гражданском браке');
	'''
								)

    # 	дабовление нового запроса
    def add_reqest(self):
        pass

    # 	дабовление новгого пользователя
    def add_user(self):
        pass

    # 	дабовление пользователя из результата запроса
    def add_search(self):
        pass


if __name__ == '__main__':
    db_connect = VKinder_db('vk', '12345678', 'vkinder_db')
    db_connect.new_db()
