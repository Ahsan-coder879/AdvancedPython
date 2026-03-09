import numpy as np

"""
li = [1,2,3,4,5,6,7]

arr = np.array(li)
print(arr/2)

arr = np.array(range(0, 10),ndmin=9)
print(arr)
print(arr.ndim)


arr2D = np.array([[1,2,3,4],[5,6,7,8]])
print(arr2D)

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

arr2D = np.array(range(72))

arr2D.reshape(2,2,3,6)
print(arr2D)
print("===========")
print(arr2D.reshape(2,2,3,6))

arr0 = np.identity(5)
arr0 = np.zeros((2,5))
print(arr0)

arr2D = np.array(range(240))
newArr = arr2D.reshape(2,2,3,4,5)
print(newArr)
print(newArr.ndim)

li = [1,2,3,4,5,6,7]
print(li)
arr = np.array(li)
print(arr)
177
71
240
0
arr5D = np.array(range(288))
newArr = arr5D.reshape(2,3,2,6,4)

print(newArr[0,1,2,1,3])
print(newArr[1,0,2,3,2])
print(newArr[0,1,0,2,1])
print(newArr[-1,-1,-1,-1,-1])
print(newArr[0,0,0,0,0])

#1
#33
#58
#102
#143
#215
slicingMatrics = np.array(range(60))
newArr = slicingMatrics.reshape(2,5,6)
print(newArr)
print("=======")
arr_slice = newArr[0,1:4,1:6:2]
print(arr_slice)

#filter command
#Where
tbt = np.array[10,20,30,40]
ar = tbt[(tbt >10) & (tbt < 40)]

fourByFour = np.array(range(16))
n_matrix = fourByFour.reshape(4,4)
print(n_matrix)
print("==========")
print(n_matrix[0:2,2:])
"""
word = "Python lecture"
print("*" * (len(word) + 4))
print(f"* {word} *")
print("*" * (len(word) + 4))