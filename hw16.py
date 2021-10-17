b = int(input("Athletes first day result: "))
r = int(input("Wanted distance: "))

d = 1
while b < r:
    b *= 1.1
    d += 1
print(f"Athlete complete  distance for {r} by {d} days")
