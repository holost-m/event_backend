from app.domain.ports.user import UserPort
from app.domain.models.user import User
from app.domain.filters import UserFilter


class UserService:
    def __init__(self, adapter: UserPort):
        self.adapter = adapter

    def create(self, user: User) -> bool:
        """Добавить пользователя"""
        return self.adapter.create(user)

    def get(self, tg_id: int) -> User:
        """Получить пользователя по его ID в Telegram"""
        user = self.adapter.get(tg_id)
        if not user:
            raise ValueError(f"Пользователь с TG ID {tg_id} не найден")
        return user

    def get_by_filter(self, _filter: UserFilter) -> tuple[User]:
        """Получить пользователей по фильтру"""
        return self.adapter.get_by_filter(_filter)

    def update(self, user: User) -> bool:
        """Обновить пользователя"""
        return self.adapter.update(user)

    def delete(self, tg_id: int) -> bool:
        """Удалить пользователя"""
        return self.adapter.delete(tg_id)

    def bulk_delete(self, _filter: UserFilter) -> bool:
        """Удалить пользователей по фильтру"""
        return self.adapter.bulk_delete(_filter)
