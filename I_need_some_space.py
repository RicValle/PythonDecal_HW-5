
#Seperating string in an array, where each letter is one space apart 

import numpy as np

myarr = np.array(['python', 'is', 'cool'])

def Spacebtw(myarr):

    return [' '.join(words) for words in myarr]

print(Spacebtw(myarr))