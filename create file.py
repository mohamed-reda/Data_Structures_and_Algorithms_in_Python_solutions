# create from 9 to 12
# for i in range(9, 13):
#     s = f"ch2/R-1.{i}.py"
#     f = open(s, "a")
#
# f.close()
import os

# for i in range(29):
#     s = f"ch2/Creativity/C-1.{i}.py"
#     f = open(s, "a")
#     f.close()

ch = 2
os.mkdir(f'ch{ch}')
os.mkdir(f'ch{ch}/Reinforcement')
os.mkdir(f'ch{ch}/Creativity')
os.mkdir(f'ch{ch}/Projects')
r = 23
c = 32
p = 39
for i in range(1, r + 1):
    s = f"ch{ch}/Reinforcement/R-1.{i}.py"
    f = open(s, "a")
    f.close()
for i in range(r + 1, c + 1):
    s = f"ch{ch}/Creativity/C-1.{i}.py"
    f = open(s, "a")
    f.close()

for i in range(c + 1, p + 1):
    s = f"ch{ch}/Projects/P-1.{i}.py"
    f = open(s, "a")
    f.close()
