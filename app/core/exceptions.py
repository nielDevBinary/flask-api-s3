class AppException(Exception):
    status_code = 400
    message = "Application error"

class NotFoundException(AppException):
    status_code = 404
    message = "Resource not found"
