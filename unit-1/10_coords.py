# Program to demonstrate sets and tuples for tracking unique visited grid coordinates.

position = (4.5, 7.8)
x, y = position
print(f"Tuple position: x = {x}, y = {y}")

visited = set()
visited.add((0, 0))
visited.add((0, 1))
visited.add((1, 1))
visited.add((2, 2))
visited.add((0, 1))  # repeat
visited.add((1, 1))  # repeat
visited.add((2, 3))
visited.add((2, 2))  # repeat

print("Visited coordinates:", sorted(visited))
print("Distinct cells visited:", len(visited))
print("Was (2, 2) visited?", (2, 2) in visited)

# Output:
# Tuple position: x = 4.5, y = 7.8
# Visited coordinates: [(0, 0), (0, 1), (1, 1), (2, 2), (2, 3)]
# Distinct cells visited: 5
# Was (2, 2) visited? True
