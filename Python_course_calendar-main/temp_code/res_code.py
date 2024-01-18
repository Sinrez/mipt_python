    # def get_user_by_mail(self, user_mail):
    #     # Поиск пользователя по почте в базе данных
    #     Session = sessionmaker(bind=self.engine)
    #     session = Session()
    #     try:
    #         user = session.query(User).filter_by(user_mail=user_mail).first()
    #         # print(f"Found user by mail {user_mail}: {user}")
    #         return user
    #     finally:
    #         session.close()


    # def get_user_by_mail(self, user_mail):
    #     # Поиск пользователя по почте в базе данных
    #     Session = sessionmaker(bind=self.engine)
    #     session = Session()
    #     try:
    #         user = session.query(User.user_mail).filter_by(user_mail=user_mail).first()
    #         if user:
    #             print(f'Юзер из базы: {user.user_mail}')
    #             return True
    #         else:
    #             return False
    #     finally:
    #         session.close()
