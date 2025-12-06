from uuid import UUID
from abc import ABC, abstractmethod
from app.domain.models.event import Event, EventCategory, Subscription


class EventPort(ABC):
    @abstractmethod
    def create(self, event: Event) -> UUID:
        """Создать новое событие из модели"""
        ...

    @abstractmethod
    def get(self, _id: UUID) -> Event | None:
        """Получить конкретное событие по его ID"""
        ...

    @abstractmethod
    def update(self, _id: UUID, event: Event) -> bool:
        """Обновить событие по его ID"""
        ...

    @abstractmethod
    def delete(self, _id: UUID) -> bool:
        """Удалить событие по его ID"""
        ...

    @abstractmethod
    def search(self, query: str, limit: int = 5, offset: int = 0) -> tuple[Event]:
        """Получить события по запросу"""
        ...


class EventCategoryPort(ABC):
    @abstractmethod
    def create(self, category: EventCategory) -> UUID:
        """Создать новую категорию"""
        ...

    @abstractmethod
    def get(self, _id: UUID) -> EventCategory | None:
        """Получить категорию по ID"""
        ...

    @abstractmethod
    def get_events_by_category(self, _id: UUID) -> list[Event]:
        """Получить все события этой категории"""
        ...

    @abstractmethod
    def update(self, _id: UUID, category: EventCategory) -> bool:
        """Обновить категорию (в контексте модели это, по сути, переименование)"""
        ...

    @abstractmethod
    def delete(self, _id: UUID) -> bool:
        """Удалить категорию по ID"""
        ...


class SubscriptionPort(ABC):
    @abstractmethod
    def create(self, subscription: Subscription) -> UUID:
        """Создать подписку пользователя"""
        ...

    @abstractmethod
    def get(self, _id: UUID) -> Subscription | None:
        """Получить подписку по ID"""
        ...

    @abstractmethod
    def get_by_user(self, user_id: int) -> list[Subscription]:
        """Найти подписки пользователя"""
        ...

    @abstractmethod
    def delete(self, _id: UUID) -> bool:
        """Удалить одписку по ID"""
        ...
