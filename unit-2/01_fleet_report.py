# Program to demonstrate functions, default arguments, and variable-length arguments.

def battery_band(pct):
    if pct < 15:
        return "critical"
    elif pct < 30:
        return "low"
    return "OK"

fleet = {"Alpha": 8, "Beta": 22, "Gamma": 76, "Delta": 41}
for name, pct in fleet.items():
    print(f"{name:<7} {pct:>3}% {battery_band(pct)}")

def move_robot(x, y, speed=1.0):
    print(f"moving to ({x}, {y}) at {speed} m/s")

move_robot(3, 4)
move_robot(3, 4, 0.5)

def log(*values, **options):
    print("values:", values)
    print("options:", options)

log("start")
log("waypoint", 3, 4.5)
log("alert", level="high", retries=2)

# Output:
# Alpha     8% critical
# Beta     22% low
# Gamma    76% OK
# Delta    41% OK
# moving to (3, 4) at 1.0 m/s
# moving to (3, 4) at 0.5 m/s
# values: ('start',)
# options: {}
# values: ('waypoint', 3, 4.5)
# options: {}
# values: ('alert',)
# options: {'level': 'high', 'retries': 2}
