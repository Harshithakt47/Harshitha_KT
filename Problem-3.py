a = int(input("Enter a number: "))

# If input is even, reduce by 1
if a % 2 == 0:
    a = a - 1

result = []

for i in range(a):
    result.append(2 * i + 1)

print(", ".join(map(str, result)))
