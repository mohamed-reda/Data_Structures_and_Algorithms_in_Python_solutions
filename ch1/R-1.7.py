# R-1.7 Give a single command that computes the sum from Exercise R-1.6, relying
# on Python’s comprehension syntax and the built-in sum function.
n = int(input())
theSum = sum(smaller * smaller for smaller in range(n) if smaller % 2 == 1)

print(f'The sum is: {theSum}')
