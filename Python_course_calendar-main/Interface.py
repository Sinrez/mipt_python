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
    pass
    def create_calendar(self):
        # Реализация создания календаря для пользователя
        pass

    def create_event(self, calendar_id, event_data):
        # Реализация создания события пользователем
        pass

    def delete_event(self, event_id):
        # Реализация удаления события пользователем
        pass