# # Question 37 - Finding a Shared Spliced Motif
# # https://rosalind.info/problems/lcsq/
# import pandas
# import numpy
#
# with open("data_strings", "r") as file:
#     data = "".join([line.strip() for line in file.readlines()]).split(">Rosalind_")[1:]
#     if data[0][3].isdigit():
#         string_s = data[0][4:]
#         string_t = data[1][4:]
#     else:
#         string_s = data[0][2:]
#         string_t = data[1][2:]
#
#
# given_list = [["_" for i in range(len(string_t) + 1)]] + [["_"]]
# result = ""
# for i in range(1, len(string_s)+1):
#     for j in range(1, len(string_t)+1):
#         if string_s[i-1] == string_t[j-1]:
#             given_list[1] += [given_list[0][j-1] + string_s[i-1]]
#         else:
#             given_list[1] += [max([given_list[0][j], given_list[1][j-1]], key=len)]
#     given_list += [["_"]]
#     given_list = given_list[1:]
# print(given_list[0][-1][1:])

# # Question 53 - Edit Distance
# # https://rosalind.info/problems/edit/
# with open("data_strings", "r") as file:
#     data = "".join([line.strip() for line in file.readlines()]).split(">Rosalind_")[1:]
#     if data[0][3].isdigit():
#         string_s = data[0][4:]
#         string_t = data[1][4:]
#     else:
#         string_s = data[0][2:]
#         string_t = data[1][2:]
#
# given_list = [["" for i in range(len(string_t) + 1)]] + [[""]]
# result = ""
# for i in range(1, len(string_s)+1):
#     for j in range(1, len(string_t)+1):
#         if string_s[i-1] == string_t[j-1]:
#             given_list[1] += [given_list[0][j-1] + f"{i},{j},"]
#         else:
#             if given_list[0][j].count(",") >= given_list[1][j-1].count(","):
#                 given_list[1] += [given_list[0][j]]
#             else:
#                 given_list[1] += [given_list[1][j-1]]
#     given_list += [[""]]
#     given_list = given_list[1:]
# max_indices = [int(element) for element in given_list[0][-1].split(",")[:-1]]
# result = 0
# if max_indices:
#     result += max(max_indices[0] - 1, max_indices[1]-1)
#     result += max(len(string_s) - max_indices[-2], len(string_t) - max_indices[-1])
# for i in range(0,len(max_indices)-2,2):
#     result += max(max_indices[i+2] - max_indices[i] - 1, max_indices[i+3] - max_indices[i+1] - 1)
#
# print(result)
#
# # print(given_list[0][-1])

# #Question 50 - Expected number of restriction sites
# # https://rosalind.info/problems/eval/
# with open("data_strings", "r") as file:
#     data = [line.strip() for line in file.readlines()]
#     n = int(data[0])
#     s = data[1]
#     array = [float(probability) for probability in data[2].split()]
#
# for probability in array:
#     result_probability = (n-len(s)+1)*((1-probability)**(s.count("A") + s.count("T")))*(probability**(s.count("G") + s.count("C")))
#     print(result_probability)
#

# Question 57 - Inferring Peptide from Full Spectrum
# https://rosalind.info/problems/full/
with open("data_strings", "r") as file:
    data = [float(line.strip()) for line in file.readlines()]

total_mass = data[0]
mass_list = []
for string_mass in data[1:]:
    mass = round(min(string_mass, total_mass - string_mass), 7)
    if mass not in mass_list:
        mass_list.append(mass)

sorted(mass_list)
difference_list = [round(mass_list[i+1] - mass_list[i], 5) for i in range(len(mass_list)-1)]
print(difference_list)