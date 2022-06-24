import re


def isValidEmail(email):
    regex = re.compile(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    )
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def isValidPhone(phone):
    regex = re.compile(r"^\+?[0-9]{10,}$")
    if re.fullmatch(regex, phone):
        return True
    else:
        return False
