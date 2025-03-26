from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum

class UserRole(Enum):
    ADMIN = "admin"
    REGULAR = "regular"
    MODEL_OWNER = "model_owner"

class BaseUser(ABC):
    def __init__(self, user_id: str, username: str, email: str, password : str, role: UserRole):
        self._user_id = user_id
        self._username = username
        self._email = email
        self._password = password
        self._role = role
        self._created_at = datetime.now()
        self._is_active = True

    @property
    def user_id(self) -> str:
        return self._user_id

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email
    
    @property
    def password(self) -> str:
        return self._password

    @property
    def role(self) -> UserRole:
        return self._role

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def is_active(self) -> bool:
        return self._is_active

    def deactivate(self) -> None:
        self._is_active = False

    @abstractmethod
    def can_perform_action(self, action: str) -> bool:
        pass

    def __str__(self) -> str:
        return f"User {self._username} ({self._role.value})"

class RegularUser(BaseUser):
    def __init__(self, user_id: str, username: str, email: str):
        super().__init__(user_id, username, email, UserRole.REGULAR)

    def can_perform_action(self, action: str) -> bool:
        return action in ["make_prediction", "view_history"]

class ModelOwnerUser(BaseUser):
    def __init__(self, user_id: str, username: str, email: str):
        super().__init__(user_id, username, email, UserRole.MODEL_OWNER)

    def can_perform_action(self, action: str) -> bool:
        return action in ["make_prediction", "view_history", "upload_model", "manage_model"]

class AdminUser(BaseUser):
    def __init__(self, user_id: str, username: str, email: str):
        super().__init__(user_id, username, email, UserRole.ADMIN)

    def can_perform_action(self, action: str) -> bool:
        return True