class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        if not 5 <= len(username) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password:str):
        is_length_correct = len(password) >= 8
        is_upper_case = any([el for el in password if el.isupper()])
        is_digit = any([el for el in password if el.isdigit()])

        is_valid = is_length_correct and is_upper_case and is_digit
        if not is_valid:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = password

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*"*len(self.password)}'