# R-1.5 Give a single command that computes the sum from Exercise R-1.4, relying
# on Python’s comprehension syntax and the built-in sum function.
n = int(input())
sum = sum(x * x for x in range(1, n))

print(f'The sum is: {sum}')
