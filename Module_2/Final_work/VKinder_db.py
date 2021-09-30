import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


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
    id_user = sq.Column(sq.Integer, sq.ForeignKey('user_table.id_user'))
    age_from = sq.Column(sq.Integer, nullable=False)
    age_to = sq.Column(sq.Integer, nullable=False)
    sex = sq.Column(sq.Integer, sq.CheckConstraint('sex>=0 and sex<=2'), nullable=False)
    city = sq.Column(sq.String, nullable=False)
    marital_status = sq.Column(sq.Integer, sq.ForeignKey('marital_status.id_status'))
    sq.PrimaryKeyConstraint(request_id, id_user, name='user_request_pk')


class Search_users(Base):
    __tablename__ = 'search_users'

    id_search = sq.Column(sq.Integer, nullable=False)
    search_user_id = sq.Column(sq.Integer, nullable=False)
    to_id_user = sq.Column(sq.Integer, sq.ForeignKey('user_table.id_user'))
    # age = sq.Column(sq.Integer, nullable=False)
    # sex = sq.Column(sq.Integer, nullable=False)
    # city = sq.Column(sq.String, nullable=False)
    # marital_status = sq.Column(sq.Integer, sq.ForeignKey('marital_status.id_status'))
    sq.PrimaryKeyConstraint(id_search, search_user_id, name='search_users_pk')

class VKinder_db:

    def __init__(self, user: str, password: str, db: str, port=5432):
        """
        Подключение к БД
        :param user: Имя пользователя БД
        :param password: Пороль пользователя БД
        :param db: Имя БД
        :param port: Порт подключения (по умолчанию 5432)
        """

        engine = sq.create_engine(f'postgresql://{user}:{password}@localhost:{port}/{db}')
        Session = sessionmaker(bind=engine)
        self.sess = Session()
        Base.metadata.create_all(engine)


        # engine = create_engine(
        #     f'postgresql://{user}:{password}@localhost:{port}/{db}')
        # self.connection = engine.connect()

    # engine = create_engine(
    # 	'postgresql://vk:12345678@localhost:5432/vkinder_db')
    # connection = engine.connect()

    # 	создание базы с минимальными значениями

    def new_db(self):
        """
        Создания  базы с нуля если она не создана или повреждена.
        """

        self.sess.add_all([
            Marital_Status(marital_status='не женат (не замужем)'),
            Marital_Status(marital_status='встречается'),
            Marital_Status(marital_status='помолвлен(-а)'),
            Marital_Status(marital_status='женат (замужем)'),
            Marital_Status(marital_status='всё сложно'),
            Marital_Status(marital_status='в активном поиске'),
            Marital_Status(marital_status='влюблен(-а)'),
            Marital_Status(marital_status='в гражданском браке'),
        ])
        self.sess.commit()
        # # создание таблицы для пользователей
        # self.connection.execute('''
        # CREATE TABLE IF NOT EXISTS User_table(
        #     id_user integer primary key,
        #     name_user varchar(40)
        #     );
        #     ''')

    #     # таблица 'семейное положение'
    #     self.connection.execute('''
    #     CREATE TABLE IF NOT EXISTS Marital_Status(
    #         id_status serial primary key,
    #         marital_status varchar
    #         );
    #         ''')
    #
    #     # таблица 'запросы пользователя'
    #     self.connection.execute('''
    #     CREATE TABLE IF NOT EXISTS User_request(
    #         request_id serial NOT NULL,
    #         id_user integer references User_table(id_user) ON DELETE CASCADE,
    #         age integer not null,
    #         sex integer CHECK ( sex>=0 and sex<=2),
    #         city varchar not null,
    #         marital_status integer references Marital_Status(id_status),
    #         CONSTRAINT User_request_pk PRIMARY KEY (request_id, id_user)
    #         );
    #         ''')
    #
    #     # таблица 'найденные пользователи для запрашиваемого'
    #     self.connection.execute('''
    #     CREATE TABLE IF NOT EXISTS Search_users(
    #         id_search serial NOT NULL,
    #         search_user_id integer NOT NULL,
    #         to_id_user integer references User_table(id_user) ON DELETE CASCADE,
    #         age integer not null,
    #         sex integer not null,
    #         city varchar not null,
    #         marital_status integer references Marital_Status(id_status),
    #         CONSTRAINT Search_users_pk PRIMARY KEY (id_search, search_user_id)
    #         );
    #         ''')
    #
    #     # дефолтное заполнение таблицы 'семейное положение'
    #     self.connection.execute('''
    #     INSERT INTO Marital_Status(marital_status)
    #     VALUES ('не женат (не замужем)'),
    #     ('встречается'),
    #     ('помолвлен(-а)'),
    #     ('женат (замужем)'),
    #     ('всё сложно'),
    #     ('в активном поиске'),
    #     ('влюблен(-а)'),
    #     ('в гражданском браке');
    #     '''
    #                             )

    # # 	добавление нового запроса
    def add_request(self, id_user: int, age_from: int, age_to: int, sex: int, city: str, marital_status: int):
        self.sess.add(User_request(id_user=id_user,
                                   age_from=age_from,
                                   age_to=age_to,
                                   sex=sex,
                                   city=city,
                                   marital_status=marital_status))
        self.sess.commit()

    # 	добавление нового пользователя
    def add_user(self, id_user: int, name_user: str):

        self.sess.add(User_table(id_user=id_user, name_user=name_user))
        self.sess.commit()

    # 	добавление пользователя из результата запроса
    def add_search(self, search_user_id: int, to_id_user: int):
        self.sess.add(User_request(search_user_id=search_user_id,
                                   to_id_user=to_id_user
                                   ))
        self.sess.commit()

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
    def check_new_user(self, user_id: int, user_name: str) -> bool:
        query = self.sess.query(User_table)
        for id_u in query:
            if user_id == id_u.id_user:
                return False
        self.add_user(user_id, user_name)
        return True

    # Проверка на наличе запроса от пользователя в БД
    #   Выдача последнего запроса пользователя
    def last_request(self, user_id: int) -> dict:
        query = self.sess.query(User_request).where(User_request.id_user == int(user_id))
        if len(query.all()):
            return query.all()[-1]
        return query.all()
