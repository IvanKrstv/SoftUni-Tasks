class PasswordTooShortError(Exception):
    """Password is less than 8 characters long"""
    pass

class PasswordTooCommonError(Exception):
    """The password consists of only letters, digits or special characters"""
    pass

class PasswordNoSpecialCharactersError(Exception):
    """No special characters in password"""
    pass

class PasswordContainsSpacesError(Exception):
    """Password contains empty spaces"""
    pass

def password_too_common(password: str, special_chars: set) -> bool:
    only_letters = password.isalpha()
    only_digits = password.isdigit()
    only_specials = all(char in special_chars for char in password)
    return only_digits or only_letters or only_specials


SPECIAL_CHARACTERS = {"@", "*", "&", "%"}
while True:
    password = input()
    if password == 'Done':
        break

    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password_too_common(password, SPECIAL_CHARACTERS):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(char in SPECIAL_CHARACTERS for char in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if ' ' in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")