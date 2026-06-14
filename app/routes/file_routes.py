from flask import Blueprint, request, jsonify
from app.services.file_service import FileService

file_bp = Blueprint("files", __name__)


@file_bp.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")

    url = FileService.upload(file)

    return jsonify({
        "message": "File uploaded successfully",
        "url": url
    }), 201

@file_bp.route("/", methods=["GET"])
def get_files():
    urls = FileService.get_all_images()

    return {
        "count": len(urls),
        "images": urls
    }, 200
