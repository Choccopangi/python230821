# ChatGPT 이메일 주소 체크

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.search(pattern, email)

email_samples = [
    "user@example.com",
    "john.doe123@gmail.com",
    "contact@website.co.uk",
    "invalid_email",
    "missing@domain",
    "user123",
    "email@example",
    "name.lastname@company",
    "12345@example.com",
    "user@sub.domain.com"
]

for email in email_samples:
    if is_valid_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")
