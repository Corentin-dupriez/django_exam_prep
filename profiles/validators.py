import string

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class UserNameValidator:
    def __init__(self, value, message: str=None) -> None:
        self.value = value
        self.message = message

    def __call__(self, value: str) -> None:
        allowed_chars = string.ascii_letters + string.digits + '_'
        for char in value:
            if char not in allowed_chars:
                raise ValidationError(self.message)

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value: str) -> None:
        if value is None:
            self.__message = 'Ensure this value contains only letters, numbers, and underscore.'
        else:
            self.__message = value
