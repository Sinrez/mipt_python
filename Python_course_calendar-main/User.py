from hashlib import sha256
from uuid import uuid4
from Backend import Backend

class User:
    def __init__(self, backend, username, user_mail, password):
        self.backend = backend
        self.__user_id = '@'+str(abs(hash(str(uuid4()))))  # Используем строковое представление UUID
        self.username = username
        self.user_mail = user_mail
        self.__password_hash = self.hash_password(password)
        self.save_to_database()
    
    def user_passwd_checker(self, password):
        pass

    def user_mail_checker(self, user_mail):
        pass

    def authenticate(self, password):
        return self.__password_hash == self.hash_password(password)
    
    def get_user_id(self):
        return self.__user_id
    
    def get_user_name(self):
        return self.username
    
    def __str__(self):
        return f"ID: {self.get_user_id()} Пользователь: {self.username} Почта: {self.user_mail}"

    @staticmethod
    def hash_password(password):
        return sha256(password.encode()).hexdigest()
    
    def save_to_database(self):
        user_data = {"user_id":  self.__user_id, "username": self.username, "user_mail": self.user_mail, "password_hash": self.__password_hash}
        self.backend.users[self.__user_id] = user_data
        self.backend.save_data_to_database()

    @classmethod
    def load_from_database(cls, backend, user_id):
        user_data = backend.users.get(user_id)
        if user_data:
            loaded_user = cls(backend, username=user_data["username"],user_mail=user_data["user_mail"], password="")
            # loaded_user.load_calendars_from_database()
            return loaded_user
        return None

    def load_calendars_from_database(self):
        calendar_ids = [calendar_id for calendar_id, data in self.backend.calendars.items() if data["user_id"] == self.__user_id]
        self.calendars = calendar_ids

if __name__ == '__main__':
    backend_instance = Backend()
    user1 = User(backend_instance, 'Bob', 'bob@example.com', 'password')
    print(user1.get_user_id())
