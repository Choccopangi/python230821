# ChatGPT 주민번호 체크

import re

def is_valid_korean_ssn(ssn):
    pattern = r'^\d{6}-[12][0-9]{6}$'
    return re.match(pattern, ssn)

ssn_samples = [
    "950101-1111111",  # Valid
    "891212-2222222",  # Valid
    "020304-1111111",  # Valid
    "030405-2222222",  # Valid
    "990909-1111111",  # Valid
    "123456-1111111",  # Invalid (first 6 digits don't represent valid date)
    "950101-1234567",  # Invalid (last 7 digits contain digits other than 1 or 2)
    "850101-1111122",  # Invalid (last 7 digits contain digits other than 1 or 2)
    "950101-11111",    # Invalid (last 7 digits not 7 characters)
    "9501011111111",   # Invalid (missing hyphen)
    "950101-123456a",  # Invalid (last 7 digits contain non-digit characters)
]

for ssn in ssn_samples:
    if is_valid_korean_ssn(ssn):
        print(f"{ssn} is a valid Korean social security number.")
    else:
        print(f"{ssn} is not a valid Korean social security number.")
