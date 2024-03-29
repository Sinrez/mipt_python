from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from hashlib import sha256

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False)
    username = Column(String, nullable=False)
    user_mail = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    calendar = relationship('Calendar', back_populates='user', uselist=False)
    events_organizer = relationship('Event', back_populates='organizer')

class Calendar(Base):
    __tablename__ = 'calendars'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)
    user = relationship('User', back_populates='calendar')
    events = relationship('Event', back_populates='calendar')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False)
    username = Column(String, nullable=False)
    user_mail = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    calendar = relationship('Calendar', back_populates='user', uselist=False)
    events_organizer = relationship('Event', back_populates='organizer')
    pending_events = relationship('Event', secondary='pending_events', back_populates='users_pending')


class PendingEvent(Base):
    __tablename__ = 'pending_events'

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False, primary_key=True)
    user = relationship('User', back_populates='pending_events')
    event = relationship('Event', back_populates='users_pending')

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

    def is_empty(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        try:
            print(f'Число юзеров {session.query(User).count()}')
            return session.query(User).count() == 0
        finally:
            session.close()

    def get_user_by_mail(self, user_mail):
        # Поиск пользователя по почте в базе данных
        Session = sessionmaker(bind=self.engine)
        session = Session()
        try:
            user = session.query(User).filter_by(user_mail=user_mail).first()
            # print(f"Found user by mail {user_mail}: {user}")
            if hasattr(user,'user_mail'):
                return user.user_mail
            else:
                return False
        finally:
            session.close()

    def save_data_to_database(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        try:
            for user_data in self.users.values():
                user = User(user_id=user_data["user_id"], username=user_data["username"], user_mail=user_data["user_mail"], password_hash=user_data["password_hash"])
                session.add(user)

            for calendar_data in self.calendars.values():
                calendar = Calendar(user_id=calendar_data["user_id"])
                session.add(calendar)

            for event_data in self.events.values():
                event = Event(name=event_data["name"], description=event_data["description"],
                            start_time=event_data["start_time"], end_time=event_data["end_time"],
                            location=event_data["location"], organizer_id=event_data["organizer_id"])
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
            self.users = {user.id: {"username": user.username, "user_mail": user.user_mail, "password_hash": user.password_hash} for user in users}

            calendars = session.query(Calendar).all()
            self.calendars = {calendar.id: {"user_id": calendar.user_id} for calendar in calendars}

            events = session.query(Event).all()
            self.events = {event.id: {"name": event.name, "description": event.description,
                                    "start_time": event.start_time, "end_time": event.end_time,
                                    "location": event.location, "organizer_id": event.organizer_id} for event in events}

            pending_events = session.query(PendingEvent).all()
            self.pending_events = {pending_event.user_id: [pending_event.event_id] for pending_event in pending_events}

        finally:
            session.close()

    @staticmethod
    def hash_password(password):
        return sha256(password.encode()).hexdigest()