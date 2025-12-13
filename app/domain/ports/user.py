from abc import ABC, abstractmethod
from app.domain.filters import UserFilter
from app.domain.models.user import User, Permission, Role
from uuid import UUID


class UserPort(ABC):
    @abstractmethod
    def create(self, user: User) -> bool:
        """Создать пользователя"""
        ...

    @abstractmethod
    def get(self, tg_id: int) -> User | None:
        """Получить пользователя по его id в телеграмме"""
        ...

    @abstractmethod
    def get_by_filter(self, _filter: UserFilter) -> tuple[User]:
        """Получить пользователей по фильтру"""
        ...

    @abstractmethod
    def update(self, user: User) -> bool:
        """Обновить пользователя по его id в телеграмме"""
        ...

    @abstractmethod
    def delete(self, tg_id: int) -> bool:
        """Удалить пользователя по его id в телеграмме"""
        ...

    @abstractmethod
    def bulk_delete(self, _filter: UserFilter) -> bool:
        """Удалить пользователей по фильтру"""
        ...


class PermissionPort(ABC):
    @abstractmethod
    def create(self, permission: Permission) -> bool:
        """Создать разрешение"""
        ...

    @abstractmethod
    def get(self, _id: UUID) -> Permission | None:
        """Получить разрешение по id"""
        ...

    @abstractmethod
    def update(self, permission: Permission) -> bool:
        """Обновить разрешение по id"""
        ...

    @abstractmethod
    def delete(self, _id: UUID) -> bool:
        """Удалить разрешение по id"""
        ...


class RolePort(ABC):
    @abstractmethod
    def create(self, role: Role) -> bool:
        """Создать роль"""
        ...

    @abstractmethod
    def get(self, _id: UUID) -> Role | None:
        """Получить роль по id"""
        ...

    @abstractmethod
    def update(self, role: Role) -> bool:
        """Обновить роль по id"""
        ...

    @abstractmethod
    def delete(self, _id: UUID) -> bool:
        """Удалить роль по id"""
        ...
