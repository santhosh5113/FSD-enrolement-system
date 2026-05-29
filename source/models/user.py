import re

class User:
    EMAIL_PATTERN = (
        r"^[a-zA-Z0-9._%+-]+"
        r"@university\.com$"
    )

    PASSWORD_PATTERN = (
        r"^[A-Z][a-zA-Z]{4,}\d{3,}$"
    )

    NAME_PATTERN = (
        r"^[a-zA-Z][a-zA-Z\s]{1,}$"
    )

    def __init__(self, email, password):
        self._email = email
        self._password = password

    def validate_name(self, name):
        return re.fullmatch(self.NAME_PATTERN, name.strip()) is not None

    def validate_email(self):
        return re.fullmatch(
            self.EMAIL_PATTERN,
            self._email
        ) is not None

    def validate_password(self):
        return re.fullmatch(
            self.PASSWORD_PATTERN,
            self._password
        ) is not None
        

