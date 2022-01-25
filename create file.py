# create from 9 to 12
# for i in range(9, 13):
#     s = f"ch2/R_1.{i}.py"
#     f = open(s, "a")
#
# f.close()
import os

# for i in range(29):
#     s = f"ch2/Creativity/C_1.{i}.py"
#     f = open(s, "a")
#     f.close()

# change the next 4 lines:
ch = 2
r = 23
c = 32
p = 39

os.mkdir(f'ch{ch}')
os.mkdir(f'ch{ch}/1 Reinforcement')
os.mkdir(f'ch{ch}/2 Creativity')
os.mkdir(f'ch{ch}/3 Projects')

for i in range(1, r + 1):
    s = f"ch{ch}/1 Reinforcement/R_{ch}_{i}.py"
    f = open(s, "a")
    f.close()
for i in range(r + 1, c + 1):
    s = f"ch{ch}/2 Creativity/C_{ch}_{i}.py"
    f = open(s, "a")
    f.close()

for i in range(c + 1, p + 1):
    s = f"ch{ch}/3 Projects/P_{ch}_{i}.py"
    f = open(s, "a")
    f.close()
