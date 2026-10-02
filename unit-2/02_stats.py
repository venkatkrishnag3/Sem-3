# Program to demonstrate multiple return values, None return, and distance calculation.

def stats(values):
    return sum(values) / len(values), min(values), max(values)

readings = [22.5, 23.1, 21.8, 24.0, 22.9]
mean, low, high = stats(readings)
print(f"mean = {mean:.2f}, min = {low:.2f}, max = {high:.2f}")

def safe_divide(a, b):
    if b == 0:
        return None
    return a / b

print("safe_divide(10, 2):", safe_divide(10, 2))
print("safe_divide(10, 0):", safe_divide(10, 0))

def total_distance(points):
    total = 0.0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        total += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return total

d = total_distance([(0, 0), (3, 4)])
print("distance:", d)

# Output:
# mean = 22.86, min = 21.80, max = 24.00
# safe_divide(10, 2): 5.0
# safe_divide(10, 0): None
# distance: 5.0
