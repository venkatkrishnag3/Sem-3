# Program to demonstrate while loops using battery discharge and countdown.

battery = 100
minutes = 0
while battery > 20:
    battery -= 8
    minutes += 1
    print(f"Minute {minutes}: battery {battery}%")

print(f"Low battery alert after {minutes} minutes ({battery}% remaining)")

print("\nCountdown:")
count = 5
while count >= 1:
    print(count)
    count -= 1
print("Take off")

# Output:
# Minute 1: battery 92%
# Minute 2: battery 84%
# Minute 3: battery 76%
# Minute 4: battery 68%
# Minute 5: battery 60%
# Minute 6: battery 52%
# Minute 7: battery 44%
# Minute 8: battery 36%
# Minute 9: battery 28%
# Minute 10: battery 20%
# Low battery alert after 10 minutes (20% remaining)
# 
# Countdown:
# 5
# 4
# 3
# 2
# 1
# Take off
