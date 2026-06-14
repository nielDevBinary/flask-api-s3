from flask import jsonify
from .exceptions import AppException

def register_error_handlers(app):

    @app.errorhandler(AppException)
    def handle_app_exception(e):
        return jsonify({
            "error": e.message
        }), e.status_code

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Route not found"}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"error": "Internal server error"}), 500
