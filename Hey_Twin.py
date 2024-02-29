
#Given an Array, find the rows where all the values are equal

import numpy as np

arr = np.array([[1, 1, 1], [1, 2, 3], [2, 2, 2]])

def Equal_Arrays(arr):

    Equal_rows = []

    for row in arr:

        if all(element == row[0] for element in row):

            Equal_rows.append(row)

    return Equal_rows

print(Equal_Arrays(arr))
