# R-1.4 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.
n = int(input())
sum = 0
if n < 1:
    print('you entered a number less than 0, we need a positive number')


else:
    for smaller in range(1, n):
        sum += smaller * smaller
        # print(f'Results of the {smaller} * {smaller} is {smaller * smaller}')

print(f'The sum is: {sum}')
