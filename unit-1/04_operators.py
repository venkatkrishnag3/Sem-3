# Program to demonstrate arithmetic, modulo, and relational operators.

heading = 350
turn = 25
print("New heading:", (heading + turn) % 360)

distance = 18.5
battery = 45.0
is_docked = False

# Safe to move only when distance > 10, battery > 20, and not docked
safe_to_move = (distance > 10) and (battery > 20) and (not is_docked)
print("Safe to move:", safe_to_move)

# Output:
# New heading: 15
# Safe to move: True
