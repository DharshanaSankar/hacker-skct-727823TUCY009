# Dharshana - 727823TUCY009

import datetime
from tool_main import generate_payloads

print("Running XSS Payload Generator...")
print("Roll No: 727823TUCY009")
print("Timestamp:", datetime.datetime.now())

payloads = generate_payloads()

print("\nGenerated Payloads:")
for i, payload in enumerate(payloads):
    print(f"{i+1}. {payload}")

