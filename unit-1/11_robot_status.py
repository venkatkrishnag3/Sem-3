# Program to demonstrate dictionary operations and character frequency counting.

robot = {"name": "Alpha", "battery": 78, "mode": "auto"}
print("Robot info:", robot)
print("Robot name:", robot["name"])

robot["battery"] -= 5
robot["speed"] = 0.5
print("Updated robot:", robot)

name = "venkat krishna"
freq = {}
for ch in name:
    if ch != " ":
        freq[ch] = freq.get(ch, 0) + 1

print(f"\nCharacter frequency for '{name}':")
for letter, count in sorted(freq.items()):
    print(f"{letter}: {count}")

most_common = max(freq, key=freq.get)
print(f"Most frequent character: '{most_common}' ({freq[most_common]} times)")

# Output:
# Robot info: {'name': 'Alpha', 'battery': 78, 'mode': 'auto'}
# Robot name: Alpha
# Updated robot: {'name': 'Alpha', 'battery': 73, 'mode': 'auto', 'speed': 0.5}
# 
# Character frequency for 'venkat krishna':
# a: 2
# e: 1
# h: 1
# i: 1
# k: 2
# n: 2
# r: 1
# s: 1
# t: 1
# v: 1
# Most frequent character: 'n' (2 times)
