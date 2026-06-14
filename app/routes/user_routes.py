from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreateSchema, UserResponseSchema, UserUpdateSchema

user_bp = Blueprint("users", __name__)

@user_bp.get("/")
def all_users():
    users = UserService.list_users()
    data = [UserResponseSchema.model_validate(u).model_dump() for u in users]
    return jsonify(data), 200

@user_bp.get("/<int:user_id>")
def get_user(user_id):
    user = UserService.get_user(user_id)
    return UserResponseSchema.model_validate(user).model_dump(), 200

@user_bp.post("/")
def create_user():
    body = UserCreateSchema.model_validate(request.json)
    new_user = UserService.create_user(body.model_dump())
    return UserResponseSchema.model_validate(new_user).model_dump(), 201

@user_bp.put("/<int:user_id>")
def update_user(user_id):
    body = UserUpdateSchema.model_validate(request.json)

    # solo valores enviados (fullname o email o ambos)
    clean_data = body.model_dump(exclude_none=True)

    updated_user = UserService.update_user(user_id, clean_data)
    return UserResponseSchema.model_validate(updated_user).model_dump(), 200

@user_bp.delete("/<int:user_id>")
def delete_user(user_id):
    UserService.delete_user(user_id)
    return {"message": "User deleted"}, 200