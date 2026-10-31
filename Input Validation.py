import re

email = input("Enter email: ")
if re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email):
    print("Valid Email")
else:
    print("Invalid Email")

phone = input("Enter phone number: ")
if re.fullmatch(r"[6-9][0-9]{9}", phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

log = "Payment successful TXN12345 and TXN67890"

ids = re.findall(r"TXN[0-9]+", log)

print("Transaction IDs:", ids)
