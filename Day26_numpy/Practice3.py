#random numbers
import numpy as np
rng = np.random.default_rng(seed=1)
print(rng.integers(1, 31, size =(2,3,2)))
print(np.random.uniform(1, 20, size=(3,2)))
cards = np.array([1,2,7,9,13,23,56])
print(rng.shuffle(cards))
print(rng.choice(cards))
