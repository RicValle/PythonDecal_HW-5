
#8x8 Array with a checkerboard pattern of zeros and ones 

import numpy as np

Checkerboard = np.zeros((8, 8))

Checkerboard[1::2, ::2] = 1 #Puts the ones in Odd rows, even columns 

Checkerboard[::2, 1::2] = 1 #Puts the ones in Even Rows, odd columms

print(Checkerboard)