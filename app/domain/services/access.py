from uuid import UUID
from app.domain.models.user import Permission, Role
from app.domain.ports.user import PermissionPort, RolePort


class PermissionService:
    def __init__(self, adapter: PermissionPort):
        self.adapter = adapter

    def create(self, permission) -> bool:
        """Создать новое разрешение"""
        return self.adapter.create(permission)

    def get(self, _id: UUID) -> Permission:
        """Получить существующее разрешение"""
        result = self.adapter.get(_id)
        if not result:
            raise ValueError(f"Разрешение с ID {_id} не найдено!")
        return result

    def update(self, permission) -> bool:
        """Обновить разрешение"""
        return self.adapter.update(permission)

    def delete(self, _id: UUID) -> bool:
        """Удалить разрешение"""
        return self.adapter.delete(_id)


class RoleService:
    def __init__(self, adapter: RolePort):
        self.adapter = adapter

    def create(self, role) -> bool:
        """Создать роль"""
        return self.adapter.create(role)

    def get(self, _id: UUID) -> Role:
        result = self.adapter.get(_id)
        if not result:
            raise ValueError(f"Роль с ID {_id} не найдена!")
        return result

    def update(self, role) -> bool:
        """Обновить роль"""
        return self.adapter.update(role)

    def delete(self, _id: UUID) -> bool:
        """Удалить роль"""
        return self.adapter.delete(_id)
