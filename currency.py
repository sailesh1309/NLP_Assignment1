import re
#defining a function to check the currency validation

def validating_currency(given_currency):
    currency_validation = re.compile(r"^[$]?[0-9]+(?:,[0-9]{3})*(?:\.[0-9]{2})?|[$]?[0-9]+(?:M|B|K)?|[-][$]?[0-9]+(?:,[0-9]{3})*(?:\.[0-9]{2})?|[+][$]?[0-9]+(?:,[0-9]{3})*(?:\.[0-9]{2})?|[A-Z]{3}[0-9]+(?:M|B)$")
    return currency_validation.findall(given_currency)