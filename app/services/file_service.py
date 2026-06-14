import uuid
from werkzeug.utils import secure_filename
from app.repositories.s3_repository import S3Repository


class FileService:
    @staticmethod
    def upload(file):
        if not file:
            raise ValueError("No file provided")

        filename = secure_filename(file.filename)
        unique_name = f"uploads/{uuid.uuid4()}_{filename}"

        return S3Repository.upload_file(
            file=file,
            key=unique_name
        )
    
    @staticmethod
    def get_all_images():
        return S3Repository.list_files()