import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

class VKinder_db:

    def __init__(self, user: str, password: str, db: str, port=5432):
        """
        Подключение к БД
        :param user: Имя пользователя БД
        :param password: Пороль пользователя БД
        :param db: Имя БД
        :param port: Порт подключения (по умолчанию 5432)
        """

        Base = declarative_base()
        engine = sq.create_engine(f'postgresql://{user}:{password}@localhost:{port}/{db}')
        session = sessionmaker(bind=engine)

        class User_table(Base):
            __tablename__ = 'user_table'

            id_user = sq.Column(sq.Integer, primary_key=True)
            name_user = sq.Column(sq.String(40))

        class Marital_Status(Base):
            __tablename__ = 'marital_status'

            id_status = sq.Column(sq.Integer, primary_key=True)
            marital_status = sq.Column(sq.String)

        class User_request(Base):
            __tablename__ = 'user_request'

            request_id = sq.Column(sq.Integer, nullable=False)
            id_user = sq.Column(sq.Integer, sq.ForeignKey('user_table.id_user'), passive_deletes=True)
            age = sq.Column(sq.Integer, nullable=False)
            sex = sq.Column(sq.Integer, sq.CheckConstraint('sex>=0 and sex<=2'), nullable=False)
            city = sq.Column(sq.String, nullable=False)
            marital_status = sq.Column(sq.String, sq.ForeignKey('marital_status.id_status'), passive_deletes=True)
            sq.PrimaryKeyConstraint(request_id, id_user, name='user_request_pk')

        class Search_users(Base):
            __tablename__ = 'search_users'

            id_search = sq.Column(sq.Integer, nullable=False)
            search_user_id = sq.Column(sq.Integer, nullable=False)
            to_id_user = sq.Column(sq.Integer, sq.ForeignKey('user_table.id_user'), passive_deletes=True)
            age = sq.Column(sq.Integer, nullable=False)
            sex = sq.Column(sq.Integer, nullable=False)
            city = sq.Column(sq.String, nullable=False)
            marital_status = sq.Column(sq.String, sq.ForeignKey('marital_status.id_status'), passive_deletes=True)
            sq.PrimaryKeyConstraint(id_search, search_user_id, name='search_users_pk')



        engine = create_engine(
            f'postgresql://{user}:{password}@localhost:{port}/{db}')
        self.connection = engine.connect()

    # engine = create_engine(
    # 	'postgresql://vk:12345678@localhost:5432/vkinder_db')
    # connection = engine.connect()

    # 	создание базы с минимальными значениями
    def new_db(self):
        """
        Создания  базы с нуля если она не создана или повреждена.
        """
        # создание таблицы для пользователей
        self.connection.execute('''
        CREATE TABLE IF NOT EXISTS User_table(
            id_user integer primary key,
            name_user varchar(40)
            );
            ''')

        # таблица 'семейное положение'
        self.connection.execute('''
        CREATE TABLE IF NOT EXISTS Marital_Status(
            id_status serial primary key,
            marital_status varchar
            );
            ''')

        # таблица 'запросы пользователя'
        self.connection.execute('''
        CREATE TABLE IF NOT EXISTS User_request(
            request_id serial NOT NULL,
            id_user integer references User_table(id_user) ON DELETE CASCADE,
            age integer not null,
            sex integer CHECK ( sex>=0 and sex<=2),
            city varchar not null,
            marital_status integer references Marital_Status(id_status),
            CONSTRAINT User_request_pk PRIMARY KEY (request_id, id_user)
            );
            ''')

        # таблица 'найденные пользователи для запрашиваемого'
        self.connection.execute('''
        CREATE TABLE IF NOT EXISTS Search_users(
            id_search serial NOT NULL,
            search_user_id integer NOT NULL,
            to_id_user integer references User_table(id_user) ON DELETE CASCADE,
            age integer not null,
            sex integer not null,
            city varchar not null,
            marital_status integer references Marital_Status(id_status),
            CONSTRAINT Search_users_pk PRIMARY KEY (id_search, search_user_id)
            );
            ''')

        # дефолтное заполнение таблицы 'семейное положение'
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

    # 	добавление нового запроса
    def add_request(self, id_user: int, age: int, sex: int, city: str, marital_status: int):
        self.connection.execute(
            f'''
            INSERT INTO User_request(id_user, age, sex, city, marital_status)
            VALUES({id_user}, {age}, {sex}, {city}, {marital_status});
            '''
        )

    # 	добавление нового пользователя
    def add_user(self, id_user: int, name_user: str):
        self.connection.execute(
            f'''
            INSERT INTO User_table(id_user, name_user)
            VALUES({id_user}, {name_user});
            '''
        )

    # 	добавление пользователя из результата запроса
    def add_search(self, search_user_id: int, to_id_user: int, age: int, sex: int, city: str, marital_status: int):
        self.connection.execute(
            f'''
            INSERT INTO User_request(search_user_id, to_id_user, age, sex, city, marital_status)
            VALUES({search_user_id}, {to_id_user}, {age}, {sex}, {city}, {marital_status});
                    '''
        )

    #   удаление запроса
    def delete_request(self):
        pass

    #   Удаление пользователя
    def delete_user(self):
        pass

    #   Удаление пользователя из результата запроса
    def delete_search(self):
        pass

    #   Проверка на нового пользователя
    def checking_new_user(self, user_id):
        self.connection.execute(f'''
        SELECT id_user
        FROM User_table
        WHERE id_user = '{user_id}';
        ''')

    #   Выдача последнего запроса пользователя

    #
