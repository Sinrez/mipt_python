# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True)
#     user_id = Column(String, nullable=False)
#     username = Column(String, nullable=False)
#     user_mail = Column(String, nullable=False)
#     password_hash = Column(String, nullable=False)
#     calendar = relationship('Calendar', uselist=False, back_populates='user')

# class Calendar(Base):
#     __tablename__ = 'calendars'

#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)
#     user = relationship('User', back_populates='calendar')


# class Event(Base):
#     __tablename__ = 'events'

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     description = Column(String)
#     start_time = Column(String, nullable=False)
#     end_time = Column(String, nullable=False)
#     location = Column(String, nullable=False)
#     organizer_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     organizer = relationship('User', back_populates='events_organizer')
#     calendar_id = Column(Integer, ForeignKey('calendars.id'), nullable=False)
#     calendar = relationship('Calendar', back_populates='events')
