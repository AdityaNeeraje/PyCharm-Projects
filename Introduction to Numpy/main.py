import numpy as np

# matrix_3d = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
#              [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]
# matrix_3d = np.array(matrix_3d)
# print(matrix_3d)


# def partition(input_list, n):
#     for division in range(n - 1):
#         if len(input_list) // n:
#             input_list = [list(input_list[i:i + n]) for i in range(len(input_list))[::n]]
#             partition(input_list, n)
#     return input_list
#
#
# n = input("Choose a number:\n").strip()
# while True:
#     try:
#         n = int(n)
#         break
#     except TypeError:
#         n = input("Please choose a valid real number:\n").strip()
# print(np.array(partition(input_list=range(1, n ** n + 1), n=n)))

# arr = np.array([[[0, 1, 2, 3],
#                            [4, 5, 6, 7]],
#
#                           [[7, 86, 6, 98],
#                            [5, 1, 0, 4]],
#
#                           [[5, 36, 32, 48],
#                            [97, 0, 27, 18]]])
# print(arr[2, 1])

data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
print(data)
grades = np.array(data)
print (type(data),'x 2:', data * 2)
print('---')
print (type(grades),'x 2:', grades * 2)