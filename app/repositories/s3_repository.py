from app.extensions import s3_client
from app.config import Config

class S3Repository:

    @staticmethod
    def upload_file(file, key):
        s3_client.upload_fileobj(
            Fileobj=file,
            Bucket=Config.AWS_S3_BUCKET,
            Key=key,
            ExtraArgs={
                "ContentType": file.content_type
            }
        )
        return f"{Config.AWS_S3_BASE_URL}/{key}"
    
    @staticmethod
    def delete_file(key):
        s3_client.delete_object(
            Bucket=Config.AWS_S3_BUCKET,
            key=key
        )
        
    @staticmethod
    def list_files(prefix="uploads/"):
        response = s3_client.list_objects_v2(
            Bucket=Config.AWS_S3_BUCKET,
            Prefix=prefix
        )

        if "Contents" not in response:
            return []

        return [
            f"{Config.AWS_S3_BASE_URL}/{obj['Key']}"
            for obj in response["Contents"]
            if not obj["Key"].endswith("/")  # evita carpetas
        ]