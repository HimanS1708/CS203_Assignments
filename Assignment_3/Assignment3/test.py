import random
import numpy as np

doors = ["car"] * 10 + ["goat"] * (35-10)
# print(doors)
random.shuffle(doors)
# print(doors)
ind = np.arange(0,35)
f = np.random.choice(ind)
print(f)
a = np.random.choice([x for x in ind if x!=f and doors[x]!="goat"])
print(a)