
#Given a random matrix sort it

import numpy as np 

np.random.seed(12345)

a = np.random.randint(1, 50, (4, 5))

def sorting_matrix(a):

    sorted_list = np.sort(a, axis = 0)

    return sorted_list

print(sorting_matrix(a))