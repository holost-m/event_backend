from uuid import UUID
from app.domain.ports.event import EventPort, EventCategoryPort
from app.domain.models.event import Event, EventCategory
from app.domain.filters import EventFilter


class EventService:
    def __init__(self, adapter: EventPort):
        self.adapter = adapter

    def create(self, event: Event) -> bool:
        """Создать событие"""
        return self.adapter.create(event)

    def get(self, _id: UUID) -> Event:
        result = self.adapter.get(_id)
        if not result:
            raise ValueError(f"Событие с ID {_id} не найдено")
        return result

    def get_by_filter(self, _filter: EventFilter) -> tuple[Event]:
        """Получить события по фильтру"""
        return self.adapter.get_by_filter(_filter)

    def update(self, event: Event) -> bool:
        """Обновить событие"""
        return self.adapter.update(event)

    def delete(self, _id: UUID) -> bool:
        """Удалить событие"""
        return self.adapter.delete(_id)

    def bulk_delete(self, _filter: EventFilter) -> bool:
        """Удалить события по фильтру"""
        return self.adapter.bulk_delete(_filter)


class EventCategoryService:
    def __init__(self, adapter: EventCategoryPort):
        self.adapter = adapter

    def create(self, category: EventCategory) -> bool:
        """Создать категорию событий"""
        return self.adapter.create(category)

    def get(self, _id: UUID) -> EventCategory:
        """Получить категорию событий"""
        result = self.adapter.get(_id)
        if not result:
            raise ValueError(f"Категория {_id} не найдена")
        return result

    def get_events(self, _id: UUID) -> tuple[Event]:
        """Получить все события категории"""
        return self.adapter.get_events(_id)

    def update(self, category: EventCategory) -> bool:
        """Обновить категорию"""
        return self.adapter.update(category)

    def delete(self, _id: UUID) -> bool:
        """Удалить категорию"""
        return self.adapter.delete(_id)
