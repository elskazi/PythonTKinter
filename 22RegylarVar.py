import re
def validate_email(email):
    return bool(re.match(r"^.+@(\w+\.){0,2}[a-z]{2,6}$", email, re.IGNORECASE))

print(validate_email("elskazi@gmail.com"))
print(validate_email("elskazi@gmail"))
print(validate_email("elskazi@gmail.com.com"))
print(validate_email("elskazi@gmail.com.info"))
print(validate_email("elskazi@"))