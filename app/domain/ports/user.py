from abc import ABC, abstractmethod
from app.domain.models.user import User, Permission, Role
from uuid import UUID


class UserPort(ABC):
    @abstractmethod
    def create(self, user: User) -> int:
        """Создать пользователя"""
        ...

    @abstractmethod
    def get(self, tg_id: int) -> User | None:
        """Получить пользователя по его id в телеграмме"""
        ...

    @abstractmethod
    def update(self, tg_id: int, user: User) -> bool:
        """Обновить пользователя по его id в телеграмме"""
        ...

    @abstractmethod
    def delete(self, tg_id: int) -> bool:
        """Удалить пользователя по его id в телеграмме"""
        ...


class PermissionPort(ABC):
    @abstractmethod
    def create(self, permission: Permission) -> UUID:
        """Создать разрешение"""
        ...

    @abstractmethod
    def get(self, _id: UUID) -> Permission | None:
        """Получить разрешение по id"""
        ...

    @abstractmethod
    def update(self, _id: UUID, permission: Permission) -> bool:
        """Обновить разрешение по id"""
        ...

    @abstractmethod
    def delete(self, _id: UUID) -> bool:
        """Удалить разрешение по id"""
        ...


class RolePort(ABC):
    @abstractmethod
    def create(self, role: Role) -> UUID:
        """Создать роль"""
        ...

    @abstractmethod
    def get(self, _id: UUID) -> Role | None:
        """Получить роль по id"""
        ...

    @abstractmethod
    def update(self, _id: UUID, role: Role) -> bool:
        """Обновить роль по id"""
        ...

    @abstractmethod
    def delete(self, _id: UUID) -> bool:
        """Удалить роль по id"""
        ...
