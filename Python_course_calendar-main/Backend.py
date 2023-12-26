"""
Сущность, отвечающая за храние и предоставление данных
Оно хранит пользователей, календари и события.
Хранение в том числе означает сохранение между сессиями в csv файлах
(пароли пользователей хранятся как hash)

Должен быть статическим или Синглтоном

*) Нужно хранить для каждого пользователя все события которые с нима произошли но ещё не были обработаны.
"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from hashlib import sha256

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)

class Calendar(Base):
    __tablename__ = 'calendars'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User')

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)
    organizer_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    organizer = relationship('User')

class PendingEvent(Base):
    __tablename__ = 'pending_events'

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False, primary_key=True)
    user = relationship('User')
    event = relationship('Event')

class Backend:
    _instance = None

    def __new__(cls, database_path="sqlite:///calendar.db"):
        if cls._instance is None:
            cls._instance = super(Backend, cls).__new__(cls)
            cls._instance.database_path = database_path
            cls._instance.engine = create_engine(cls._instance.database_path)
            cls._instance.create_tables()
            # Инициализация данных
            cls._instance.users = {}
            cls._instance.calendars = {}
            cls._instance.events = {}
            cls._instance.pending_events = {}
        return cls._instance

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def save_data_to_database(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        try:
            for user_data in self.users.values():
                user = User(username=user_data["username"], password_hash=user_data["password_hash"])
                session.add(user)

            for calendar_data in self.calendars.values():
                calendar = Calendar(user_id=calendar_data["user_id"])
                session.add(calendar)

            for event_data in self.events.values():
                event = Event(title=event_data["title"], description=event_data["description"],
                            start_time=event_data["start_time"], end_time=event_data["end_time"],
                            organizer_id=event_data["organizer_id"])
                session.add(event)

            for user_id, pending_events in self.pending_events.items():
                for event_id in pending_events:
                    pending_event = PendingEvent(user_id=user_id, event_id=event_id)
                    session.add(pending_event)

            session.commit()
        finally:
            session.close()

    def load_data_from_database(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        try:
            users = session.query(User).all()
            self.users = {user.id: {"username": user.username, "password_hash": user.password_hash} for user in users}

            calendars = session.query(Calendar).all()
            self.calendars = {calendar.id: {"user_id": calendar.user_id} for calendar in calendars}

            events = session.query(Event).all()
            self.events = {event.id: {"title": event.title, "description": event.description,
                                    "start_time": event.start_time, "end_time": event.end_time,
                                    "organizer_id": event.organizer_id} for event in events}

            pending_events = session.query(PendingEvent).all()
            self.pending_events = {pending_event.user_id: [pending_event.event_id] for pending_event in pending_events}

        finally:
            session.close()

    @staticmethod
    def hash_password(password):
        return sha256(password.encode()).hexdigest()
