result = 1

for count in range(365):
    result += result * (1 / 100)

print(result)

result2 = 1
for count in range(365):
    result2 -= result2 * (1 / 100)

print(result2)
