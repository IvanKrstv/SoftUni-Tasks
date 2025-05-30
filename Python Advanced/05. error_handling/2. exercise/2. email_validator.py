class NameTooShortError(Exception):
    """The name in the email is less than or equal to 4"""
    pass

class MustContainAtSymbolError(Exception):
    """No '@' in the email name"""
    pass

class InvalidDomainError(Exception):
    """The domain of the email is invalid"""
    pass

VALID_DOMAINS =('.com', '.bg', '.org', '.net')
current_email = input()
while current_email != 'End':
    if '@' not in current_email:
        raise MustContainAtSymbolError("Email must contain @")
    else:
        name = current_email.split('@')[0]
        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")

        domain = current_email.split('.')[-1]
        if f'.{domain}' not in VALID_DOMAINS:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    current_email = input()