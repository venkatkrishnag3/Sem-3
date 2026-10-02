# Program to demonstrate string methods and parsing key-value telemetry packets.

raw = "  Rover Alpha  \n"
print("Cleaned string:", raw.strip())
print("Uppercase:", raw.strip().upper())

packet = "voltage:24.5;current:3.2;temp:38.0"
fields = packet.split(";")
print("\nParsed packet:")
for item in fields:
    key, val = item.split(":")
    print(f"{key} -> {float(val):.1f}")

# Output:
# Cleaned string: Rover Alpha
# Uppercase: ROVER ALPHA
# 
# Parsed packet:
# voltage -> 24.5
# current -> 3.2
# temp -> 38.0
