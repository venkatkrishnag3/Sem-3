# Program to determine operating mode using if-elif-else conditional statements.

temp = float(input("Enter temperature: "))

if temp < 40:
    mode = "heater on"
elif temp <= 60:
    mode = "normal"
elif temp <= 80:
    mode = "cooling"
else:
    mode = "shut down"

print("Operating mode:", mode)

score = 85
if score >= 90:
    grade = "DISTINCTION"
elif score >= 60:
    grade = "FIRST CLASS"
elif score >= 40:
    grade = "PASS"
else:
    grade = "FAIL"

print("Grade:", grade)

# Output:
# Enter temperature: 55
# Operating mode: normal
# Grade: FIRST CLASS
