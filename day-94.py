import re
text = "My email is ahad@example.com and my number is 01712345678"

# Find email
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
email = re.search(email_pattern, text)
if email:
    print("Email found:", email.group())

# Find phone numbers
phone_pattern = r"\d{11}"
phones = re.findall(phone_pattern, text)
print("Phone numbers:", phones)
