import numpy as np

arr_2d = np.array([[10,20,30],[40,50,60]])
print(arr_2d)

new_arr_2d = np.insert(arr_2d, 1,[70,80],axis=1)
print(new_arr_2d)

new_arr_2d = np.insert(arr_2d, 1,[70,80,90],axis=0)
print(new_arr_2d)