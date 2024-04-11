# ValueError: cannot reshape array of size X into shape Y

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape((2, 3))

# [[1 2 3]
#  [4 5 6]]
print(new_arr)