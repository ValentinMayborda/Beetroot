"""
Створіть метод класу (мається на увазі окремий метод класу) з назвою validate,
 який повинен викликатися з методу __init__ для перевірки параметра email, переданого в конструктор.

Логіка всередині методу validate може полягати в перевірці того,
 чи є переданий параметр email коректною адресою електронної пошти.
"""
import string


class Email:
    def __init__(self, email):
        if self.validate(email):
            self.email = email
        else:
            raise ValueError(' Не валідний емейл!')


    @staticmethod
    def validate(email):
        email = email.lower()
        parts = email.split('@')

        if len(parts) != 2:
            return False

        local = parts[0]
        domain = parts[1]

        if local == "" or domain == "":
            return  False

        if '.' not in domain:
            return False

        if '..' in local or domain:
            return False

        if local.startswith('.') or local.endswith('.'):
            return False

        if domain.startswith('.') or domain.endswith('.'):
            return False

        allowed = set(string.ascii_letters + string.digits + '.-_')
        for part in parts:
            if not set(part) <= allowed:
                return False
        return True


# t = Email('val@gmail.com')
#t1 = Email('val@gm.ai.l.com')
#t2 = Email('@gm.ai.l.com')
#t3 = Email('val@')
#t4 = Email('@')
#t5 = Email('val.ccdc.c@gmail.com')
#t6 = Email('.val.ccdc.c@gmail.com')
#t7 = Email('.val.ccdc.c@gmail.com.')
#t8 = Email('val..ccdcc@gmail.com')
#t9 = Email('val.ccdcc@gmail..com')