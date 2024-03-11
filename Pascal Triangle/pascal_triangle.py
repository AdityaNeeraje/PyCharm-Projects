# # from tkinter import *
# #
# # # root = Tk()
# #
# n = 20
# combinations_matrix = [[1], [1, 1]]
# for number in range(2, n+1):
#     combinations_matrix += [[1] + [combinations_matrix[number-1][i] + combinations_matrix[number-1][i+1] for i in range(number-1)] + [1]]
#     # for i in range(len(combinations_matrix)):
#     #     combinations_matrix[i] = [" "] + combinations_matrix[i] + [" "]
#
# for i in range(len(combinations_matrix)):
#     new_list = []
#     for num in range(len(combinations_matrix[i])):
#         new_list += [combinations_matrix[i][num], " "]
#     combinations_matrix[i] = [" "]*(len(combinations_matrix) - i - 1) + new_list[:-1] + [" "]*(len(combinations_matrix) - i - 1)
#
# for n in range(len(combinations_matrix[0])):
#     max_string_len = max([len(str(combination_list[n])) for combination_list in combinations_matrix])
#     for combination_list in combinations_matrix:
#         lpadding = max_string_len - len(str(combination_list[n]))
#         combination_list[n] = " "*(lpadding//2) + str(combination_list[n]) + " "*(lpadding-lpadding//2)
#
# for combination_list in combinations_matrix:
#     print("".join(combination_list))
# even_combinations_matrix = combinations_matrix[::2]
# odd_combinations_matrix = combinations_matrix[1::2]
#
# for n in range(len(even_combinations_matrix[0])):
#     max_string_len = max([len(str(combination_list[n])) for combination_list in even_combinations_matrix])
#     for combination_list in even_combinations_matrix:
#         combination_list[n] = str(combination_list[n]) + " "*(max_string_len - len(str(combination_list[n])))
# for n in range(len(odd_combinations_matrix[0])):
#     max_string_len = max([len(str(combination_list[n])) for combination_list in odd_combinations_matrix])
#     for combination_list in odd_combinations_matrix:
#         combination_list[n] = str(combination_list[n]) + " "*(max_string_len - len(str(combination_list[n])))
# for combination in odd_combinations_matrix:
#     combination[len(combination)//2] = " " + str(combination[len(combination)//2])

# for combination in combinations_matrix:
#     if combination in odd_combinations_matrix:
#         print(" " + "  ".join(["1" if str(element).strip().isdigit() else str(element) for element in combination]))
#     else:
#         print("  ".join(["1" if str(element).strip().isdigit() else str(element) for element in combination]))

combinations_matrix = []
# for n in range(len(even_combinations_matrix)):
#     combinations_matrix += [even_combinations_matrix[n]]
#     if len(odd_combinations_matrix) >= n+1:
#         combinations_matrix += [[" "]*((len("".join(even_combinations_matrix[0])) - len("".join(odd_combinations_matrix[0])))//2) + odd_combinations_matrix[n]]
# for combination in combinations_matrix:
#     print("  ".join(combination))
