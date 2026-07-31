import string


def is_valid_email_address(email):
    email = email.lower()
    parts = email.split('@')

    if len(parts) != 2:
        return False

    allowed = set(string.ascii_letters + string.digits + '.-_')
    for part in parts:
        if not set(part) <= allowed:
            return False
    return True

def test_regular_email_validations():
    assert is_valid_email_address('test@example.com')
    assert is_valid_email_address('user123@subdomain.example.com')
    assert is_valid_email_address('john.doe@subdomain.example.com')

def test_valid_email_has_one_at_sign():
    assert not is_valid_email_address('john.doe')

def test_valid_has_only_allowed_characters():
    assert not is_valid_email_address('john,doe@example.com')
    assert not is_valid_email_address('john doe@example.com')