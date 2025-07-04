class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str):
        return mail in self.mails

    def __is_domain_valid(self, domain: str):
        return domain in self.domains

    def validate(self, email: str):
        username, data = email.split('@')
        mail, domain = data.split('.')

        is_valid = self.__is_name_valid(username) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)
        return is_valid

