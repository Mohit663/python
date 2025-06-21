#np.insert(array, index, value, axis=None)
#array - original array
#axis - 1 means column
#axis - 0 means row

import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr)
new_arr = np.insert(arr, 2, 100, axis=0)
print(new_arr)