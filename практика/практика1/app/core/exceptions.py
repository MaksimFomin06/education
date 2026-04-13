class AppError(Exception):
    code = "app_error"
    status_code = 400

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class NotFoundError(AppError):
    code = "not_found"
    status_code = 404


class PermissionDeniedError(AppError):
    code = "permission_denied"
    status_code = 403


class ConflictError(AppError):
    code = "conflict"
    status_code = 409


class ValidationAppError(AppError):
    code = "validation_error"
    status_code = 422
