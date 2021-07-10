# R-1.8 Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index
# −n≤k<0, what is the equivalent index j ≥0 such that s[j] references
# the same element?

s = '123456'
# −6≤k<0
n = len(s)
# -6:0
j = 0
for k in range(-n, 0):
    # print(f'k = {k}')
    print(f'k = {k}, it\'s: {s[k]}')
    print(f'j = {j}, it\'s: {s[j]}\n')
    print()
    j += 1
