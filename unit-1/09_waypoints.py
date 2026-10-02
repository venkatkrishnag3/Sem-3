# Program to demonstrate list operations, slicing, and list comprehensions.

waypoints = ["Base", "Station_A", "Station_B"]
waypoints.append("Station_C")
waypoints.insert(1, "Check_1")
waypoints.remove("Station_A")
print("Waypoints list:", waypoints)

a = [10, 20, 30]
b = a
c = a[:]
b.append(40)
c.append(99)

print("\nReference vs Copy:")
print("a:", a)
print("b (alias of a):", b)
print("c (copy of a):", c)

readings = [12, 45, 8, 62, 33]
doubled = [r * 2 for r in readings]
above_30 = [r for r in readings if r > 30]
print("\nDoubled:", doubled)
print("Readings > 30:", above_30)

# Output:
# Waypoints list: ['Base', 'Check_1', 'Station_B', 'Station_C']
# 
# Reference vs Copy:
# a: [10, 20, 30, 40]
# b (alias of a): [10, 20, 30, 40]
# c (copy of a): [10, 20, 30, 99]
# 
# Doubled: [24, 90, 16, 124, 66]
# Readings > 30: [45, 62, 33]
