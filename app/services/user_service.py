from app.repositories.user_repository import UserRepository
from app.core.exceptions import NotFoundException

class UserService:

    @staticmethod
    def list_users():
        return UserRepository.get_all()
    
    @staticmethod
    def get_user(user_id: int):
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise NotFoundException("User not found")
        return user
    
    @staticmethod
    def create_user(data: dict):
        return UserRepository.create(data)
    
    @staticmethod
    def update_user(user_id:int, data:dict):
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise NotFoundException("User not found")
        updated = UserRepository.update(user, data)
        return updated

    @staticmethod
    def delete_user(user_id: int):
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise NotFoundException("User not found")
        UserRepository.delete(user)
        