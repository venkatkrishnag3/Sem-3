# Program to demonstrate for loops with grid mapping and sensor readings.

readings = [22.5, 23.1, 21.8, 24.0, 22.9]
total = sum(readings)
print(f"Total: {total:.2f} | Count: {len(readings)} | Mean: {total/len(readings):.2f}\n")

obstacles = [(2, 3), (1, 6), (5, 4)]
print("8x8 Grid Map (S=Start, G=Goal, X=Obstacle):")
for i in range(8):
    for j in range(8):
        if (i, j) == (0, 0):
            print("S", end=" ")
        elif (i, j) == (7, 7):
            print("G", end=" ")
        elif (i, j) in obstacles:
            print("X", end=" ")
        else:
            print(".", end=" ")
    print()

# Output:
# Total: 114.30 | Count: 5 | Mean: 22.86
# 
# 8x8 Grid Map (S=Start, G=Goal, X=Obstacle):
# S . . . . . . . 
# . . . . . . X . 
# . . . X . . . . 
# . . . . . . . . 
# . . . . . . . . 
# . . . . X . . . 
# . . . . . . . . 
# . . . . . . . G 
