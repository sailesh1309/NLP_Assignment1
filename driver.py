
import re
from currency import validating_currency
from date import validating_date
from phone_numbers import validating_phone
from tags import validating_tags

with open('input.txt', 'r') as file:
    lines_data = file.readlines()
    for line in lines_data:
        print('Input:', line)
        print('Currency:', validating_currency(line))
        print('Date:', validating_date(line))
        print('Phone:', validating_phone(line))
#        print('Tags:', validating_tags(line))
        print()