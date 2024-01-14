"""
Описывает некоторе "событие" - промежуток времени с присвоенными характеристиками
У события должно быть описание, название и список участников
Событие может быть единожды созданым
Или периодическим (каждый день/месяц/год/неделю)

Каждый пользователь ивента имеет свою "роль"
организатор умеет изменять названия, список участников, описание, а так же может удалить событие
участник может покинуть событие

запрос на хранение в таблицу event бд Calendar

Иметь покрытие тестами
Комментарии на нетривиальных методах и в целом документация
"""
from uuid import uuid4

class Event:
    """Класс события"""
    #to do добавить периодичность
    def __init__(self, name, start_date, end_date, location, admin):
        self.event_id = abs(hash(str(uuid4())))
        self.event_name = name
        self.event_start_date = start_date
        self.event_end_date = end_date
        self.event_location = location
        self.event_users = []
        self.event_admin = admin
    
    def add_user(self, user_id):
        self.event_users.append(user_id)

    def delete_user(self, user_id):
        del_us = self.event_users.pop(user_id)
        print(f'Пользователь {del_us} удален')
    
    def get_event_id(self):
        return self.event_id

    def __str__(self):
        return f"ID: {self.event_id} Название: {self.event_name} Начало: {self.event_start_date.strftime('%Y-%m-%d %H:%M')} Завершение: {self.event_end_date.strftime('%Y-%m-%d %H:%M')}  Будет в: {self.event_location}"
    
#локальная проверка
if __name__ == '__main__':
    from datetime import datetime
    event1 = Event("New Year's Eve Party", datetime(2023, 12, 31, 22, 0),datetime(2023, 12, 31, 22, 0), "Town Hall", 'Bob')
    print(event1)
