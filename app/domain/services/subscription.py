from uuid import UUID
from app.domain.models.event import Subscription, EventCategory
from app.domain.models.user import User
from app.domain.ports.event import SubscriptionPort


class SubscriptionService:
    def __init__(self, adapter: SubscriptionPort):
        self.adapter = adapter

    def create(self, subscription) -> bool:
        """Создать объект подписки"""
        return self.adapter.create(subscription)

    def get(self, _id: UUID) -> Subscription:
        """Получить объект подписки"""
        result = self.adapter.get(_id)
        if not result:
            raise ValueError(f"Подписка с ID {_id} не найдена!")
        return result

    def get_by_user(self, user_id: int) -> tuple[EventCategory]:
        """Получить все категории, на которые подписан пользователь"""
        return self.adapter.get_by_user(user_id)

    def get_by_category(self, category_id: int) -> tuple[User]:
        """Найти всех пользователей, подписанных на категорию"""
        return self.adapter.get_by_category(category_id)

    def delete(self, _id: UUID) -> bool:
        """Удалить объект подписки"""
        return self.adapter.delete(_id)
