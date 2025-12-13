from uuid import UUID
from abc import ABC, abstractmethod
from app.domain.filters import EventFilter
from app.domain.models.event import Event, EventCategory, Subscription
from app.domain.models.user import User


class EventPort(ABC):
    @abstractmethod
    def create(self, event: Event) -> bool:
        """Создать новое событие из модели"""
        ...

    @abstractmethod
    def get(self, _id: UUID) -> Event | None:
        """Получить конкретное событие по его ID"""
        ...

    @abstractmethod
    def get_by_filter(self, _filter: EventFilter) -> tuple[Event]:
        """Получить события по фильтру"""
        ...

    @abstractmethod
    def update(self, event: Event) -> bool:
        """Обновить событие по его ID"""
        ...

    @abstractmethod
    def delete(self, _id: UUID) -> bool:
        """Удалить событие по его ID"""
        ...

    @abstractmethod
    def bulk_delete(self, _filter: EventFilter) -> bool:
        """Удалить события по фильтру"""
        ...


class EventCategoryPort(ABC):
    @abstractmethod
    def create(self, category: EventCategory) -> bool:
        """Создать новую категорию"""
        ...

    @abstractmethod
    def get(self, _id: UUID) -> EventCategory | None:
        """Получить категорию по ID"""
        ...

    @abstractmethod
    def get_events(self, _id: UUID) -> tuple[Event]:
        """Получить все события этой категории"""
        ...

    @abstractmethod
    def update(self, category: EventCategory) -> bool:
        """Обновить категорию"""
        ...

    @abstractmethod
    def delete(self, _id: UUID) -> bool:
        """Удалить категорию по ID"""
        ...


class SubscriptionPort(ABC):
    @abstractmethod
    def create(self, subscription: Subscription) -> bool:
        """Создать подписку пользователя"""
        ...

    @abstractmethod
    def get(self, _id: UUID) -> Subscription | None:
        """Получить подписку по ID"""
        ...

    @abstractmethod
    def get_by_user(self, user_id: int) -> tuple[EventCategory]:
        """Найти все категории, на которые подписан пользователь"""
        ...

    @abstractmethod
    def get_by_category(self, category_id: int) -> tuple[User]:
        """Найти пользователей, подписанных на данную категорию"""
        ...

    @abstractmethod
    def delete(self, _id: UUID) -> bool:
        """Удалить подписку по ID"""
        ...
