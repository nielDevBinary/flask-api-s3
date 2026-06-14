from app.extensions import db
from app.models.user_model import User

class UserRepository:

    @staticmethod
    def get_all():
        return User.query.all()
    
    @staticmethod
    def get_by_id(user_id: id):
        return User.query.get(user_id)
    
    @staticmethod
    def create(data: dict):
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    @staticmethod
    def update(user, data:dict):
        for key, value in data.items():
            if value is not None:
                setattr(user, key, value)
        db.session.commit()
        return user
    
    @staticmethod
    def delete(user):
        db.session.delete(user)
        db.session.commit()
