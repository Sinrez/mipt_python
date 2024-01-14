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

class Interface:

    if __name__ == '__main__':
        from datetime import datetime
        user1 = User('Bob2', '12')
        user1_id = user1.get_user_id()
        event1 = Event("New Year's Eve Party", datetime(2023, 12, 31, 22, 0),datetime(2023, 12, 31, 22, 0), "Town Hall", user1)
        event2 = Event("New Year's Eve Party", datetime(2023, 12, 31, 22, 0),datetime(2023, 12, 31, 22, 0), "Town Hall", user1)
        calendar1 = Calendar(user1_id)
        calendar1.add_event(event1)
        calendar1.add_event(event2)
        calendar1.get_events()