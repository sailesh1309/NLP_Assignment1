# -*- coding: utf-8 -*-
"""date.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XezbWks3kR7O7cIQH3K1Iea1awPEDtOO
"""

import re
#definign function
def validating_date(given_date):
    date_validation = re.compile(r'^(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2},\s+\d{4}$|^\d{1,4}[/-]\d{1,2}[/-]\d{2,4}$|^\d{1,2}[- ](?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|Jul(?:y)?|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?),\s+\d{4}$')
    return date_validation.match(given_date)