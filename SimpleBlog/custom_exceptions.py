from enum import Enum
from rest_framework.exceptions import APIException

class ExceptionType(Enum):
    UNKNOWN_ERROR = "unknown_error"
    INVALID_INPUT = "invalid_input"


class CustomAPIException(APIException):
    def __init__(self, exception_type, detail=None):
        self.exception_type = exception_type
        super().__init__(detail)

    def to_representation(self):
        return {
            "type": self.exception_type,
            "detail": self.detail
        }