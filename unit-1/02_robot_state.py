# Program to describe robot state variables, data types, and check battery status.

robot_name = "Scout"
battery = 78.5
is_docked = True
waypoints = 12

print("Name:", robot_name, "| Type:", type(robot_name).__name__)
print("Battery:", battery, "| Type:", type(battery).__name__)
print("Docked:", is_docked, "| Type:", type(is_docked).__name__)
print("Waypoints:", waypoints, "| Type:", type(waypoints).__name__)

battery -= 35
print("\nUpdated battery after travel:", battery)

if battery < 50:
    print("WARNING: Battery is low!")

# Output:
# Name: Scout | Type: str
# Battery: 78.5 | Type: float
# Docked: True | Type: bool
# Waypoints: 12 | Type: int
# 
# Updated battery after travel: 43.5
# WARNING: Battery is low!
