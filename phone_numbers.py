import re

def validating_phone(given_phone):
    pattern = re.compile(r"^(?:\+1|001)?[\s-]?[\(]?[0-9]{3}[\)]?[\s-]?[0-9]{3}[\s-]?[0-9]{4}$")
    return pattern.search(given_phone)