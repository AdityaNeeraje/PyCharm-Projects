# # given_list = []
# max_sequence_sum = 0
# max_ending_sum = 0
# while True:
#     n = input().strip()
#     if not n.isdigit() and not (n[0] in ["-", "+"] and n[1:].isdigit()):
#         break
#     n = int(n)
#     # given_list.append(n)
#     # if n == 0:
#     #     pass
#     if n > 0:
#         max_ending_sum += n
#         max_sequence_sum = max([max_sequence_sum, max_ending_sum])
#     elif max_ending_sum + n >= 0:
#         max_ending_sum += n
#     else:
#         max_ending_sum = 0
#     # print(given_list)
#     print(max_sequence_sum)

import pandas

def check_if_poset(matrix):
    for num_rows in range(len(matrix)):
        for column_number in range(num_rows+1,len(matrix)):
            if matrix[num_rows][column_number] == matrix[column_number][num_rows] == 1:
                return False
            if matrix[num_rows][column_number] == 1:
                for element in range(column_number+1,len(matrix[column_number])):
                    if matrix[column_number][element] == 1:
                        if matrix[num_rows][element] != 1:
                            print(num_rows, column_number, element)
                            return False
    return True


posets = [[[1 if i == j else 0 for i in range(4)] for j in range(4)]]
given_dict = posets[0]
for i in range(len(given_dict)):
    pass
# df.set_index([1, 2, 3, 4])
print(check_if_poset(given_dict))
