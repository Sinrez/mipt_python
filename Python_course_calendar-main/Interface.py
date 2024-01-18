"""
Позволяет зайти по логину-паролю или создать нового пользователя (а так же выйти из аккаунта)
Позволяет выбрать календарь, узнать ближайшие события, события из промежутка времени а так же
Создать событие или удалить событие
После создания события можно добавить туда пользователей
Если нас добавили в событие или удалили мы получаем уведомление.

в main можно использовать ТОЛЬКО interface
"""
from Backend import Backend
from Calendar import Calendar
from Event import Event
from User import User
from datetime import datetime

class Interface:

    if __name__ == '__main__':
        
        # user1 = User('Bob2', '12')
        # user1_id = user1.get_user_id()
        # event1 = Event("New Year's Eve Party", datetime(2023, 12, 31, 22, 0),datetime(2023, 12, 31, 22, 0), "Town Hall", user1)
        # event2 = Event("New Year's Eve Party", datetime(2023, 12, 31, 22, 0),datetime(2023, 12, 31, 22, 0), "Town Hall", user1)
        # calendar1 = Calendar(user1_id)
        # calendar1.add_event(event1)
        # calendar1.add_event(event2)
        # calendar1.get_events()

        # Пример использования с БД:
        backend_instance = Backend()
        # calendar_instance = Calendar(backend_instance, user_id=1)

        user1 = User(backend_instance, '0000008', 'bob00000008@mail.ru','12')
        user1.save_to_database()
        user1_id = user1.get_user_id()
        print(user1_id)
        user1_mail = user1.get_user_mail()
        print(user1.load_from_database(backend_instance, user1_id))
        event1 = Event("New Year's Eve Party", datetime(2023, 12, 31, 22, 0),datetime(2023, 12, 31, 22, 0), "Town Hall", user1)
        event2 = Event("New Year's Eve Party", datetime(2023, 12, 31, 22, 0),datetime(2023, 12, 31, 22, 0), "Town Hall", user1)

        # Добавление события
        # event_id = calendar_instance.add_event(event1)

        # Поиск событий в промежутке
        # events_in_range = calendar_instance.search_events("2023-01-01 00:00", "2024-01-02 00:00")
        # print("Events in range:", events_in_range)