# Question 1 - Counting DNA Nucleotides
# string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
# print(list(string).count('A'), list(string).count("C"), list(string).count('G'), list(string).count('T'))

# Question 2 - Transcribing DNA into RNA
# string = "CGGCAAAGTGCATAAACCAGCATATTAGCTTTACCTCGGCACACCTTGCACGGCATTCGGCAATTCTTATTTGTTCGCGCCCGTGGTATATTGTAGTTAGTGCTGTGCCTAAGTATCGGGATGCGGCGCGTTGCCTATCGCCCTGGGAGATTTAAGCTGAGGTGTGCCGCTAAAGTAGCGTAACGTCTATCCTGACTAGGGTCATGGCTAAAGGTTCCTGGCGGATGATTTAACATTGTAATTGATTGATCTGGGGCACGTGGTAGGAGGCGTATGTGTCGAAACCGATTTCACAGGTAAGTCTCCTTACGTGGTCGCCCCGTGTGAACATAAATAGCCCATATAACACGTGGTCCGATGCTTTTCCTTGAGTGTCGTAGGGTGAGTCGCCCCCGGAATCCATGTTGCACGGGAAGTTACGAGTGCCTCATGAGTACTCTCTCCGTAGCCGAGGTCCTGCCCGCTTAATAATCGTCAACACAACGCCGTATGTCGACCATGTCGAGGTCCGCCACAGTATTAACGTAATTTCACAGGACCCGAGATACTTACGCGTACTTCATAAGGTCGATTGTGTCAAGCAGGTGCGTACCTGAATTATCCCACCTTTATTGCAATCGCATTGGCGATACGAATTCCTTCAAGAAGTCAGTGTTTAATAGGACGTCGCACTAGGTACGCGGGAAGACGCGTCCCAAACCTCATCATACATTAATTCAGGGGATCAACGATGACGGGTGTCGTGCCGGCCCCTGTCCCTCTAAACTATTCGACCATCGCTTCAACTCAGCAATCTTGGACCCATGGAGTCACCGCTGTGGGCAGCAGAAGTCGGGTAGTGAAGTGAAGTCGAGCACTACGTCTCGCCGGGCAGCAAGCTGATACATAAACCCGATGTAGTCATCTGCGCCAAGCCGCGATCGGTCTCAGCCTAGTTAGATTCCGT"
# print(string.replace("T", "U"))

# # Question 3 - Complementing a Strand of DNA
# string = "CAACGAGTGCTTTTACTCTCGACACAAGCTGACCGTTACCAACAGCACCTGGCAATTCCTGAGGAAGTCTCGGATTGACCCCACAGACTCATATTGGTTGCTCGGCTCAGATATCCTGCGCACTTCAGAGGCAAACCACAAAGTAATTTTATTGCGGGTATTAGAGCCTCAACGGATTATCACTTAAATTTGCTTCTCAGCGGACTTTGCTGTACACTTTGAGGGGCAGTCACTTCTCTCAATTCAGTCGGACGAGGTACGGATGGGAGAGAGCGCCACATCTCTACCTTATTAGGAATTTTTATATGATCGATATCTTCGCCAAAAATGCCAATTACCCTAAGTTCACACCGGCCAGTGATGATTATGGGAAAACTGCGTGGTAACGCGGAATCCCCAACGTGTGCTATGTTATGTGAACTGGTCTCCCGCTTTCCGCTTAGCAACCCGTCTTAACAAAGTCTATGTATACTCGACGCGCGTTTCTTCGTCACGCCCGTTGTCTCTGAGCGGGATGTCGTGTTCGCTCTCTAAACGCGACTACACCCGCAACGCACGCAGCGATATTCCGAGTAGCGTTATGGACTGATGCATATCACTGATGGCGATAGTGTAGAGCAAACCAACACCCTCCAGTAGGATCATGCTTCTCAAAAATAGTTGTCGAACGAGATCCTCCGAGACGTGTATGTGTACCAAGTTCGCCGATGGGCATCTAGGATGATACGAGTTGATAGTCCTGGGGCTTACTGCCGTCCCAATATTCAGGACCCGCCTGTAAGTTTTCAACTCGTACGATGCGCTCAGCACGGAGATACGCATACAAGCCGCCACGACCACGTAGGGATTTGCG"
# print(string.replace("A", "t").replace("G", "c").replace("T", "a").replace("C", "g").upper()[::-1])

# # Question 4 - Recurrence Relations and Fibonacci Rabbits
# k = 5
# n = 32
# f0 = 0
# f1 = 1
# for number in range(2, n+1):
#     f1 += k*f0
#     f0 = f1 - k*f0
# print(f1)

# # Question 5 - Computing GC Content
# # https://rosalind.info/problems/gc/
# with open("data_strings", "r") as file:
#     string = "".join([line.strip() for line in file.readlines()])
# dictionary_of_strands = {strand: strand.split("_")[1][4:] for strand in string.split(">")[1:]}
# list_of_strands = [(strand.count("G") + strand.count("C"))/len(strand) for data, strand in dictionary_of_strands.items()]
# index = list_of_strands.index(max(list_of_strands))
# print(list(dictionary_of_strands.keys())[index][:13])
# print(100*max(list_of_strands))

# # Question 6 - Counting Point Mutations
# # https://rosalind.info/problems/hamm/
# with open("data_strings", "r") as file:
#     data = file.readlines()
#     string_s = data[0].strip()
#     string_t = data[1].strip()
# hamming_distance = len([n for n in range(len(string_s)) if string_s[n] != string_t[n]])
# print(hamming_distance)

# # Question 7 - Mendel's First Law
# # https://rosalind.info/problems/iprb/
# with open("data_strings", "r") as file:
#     data = file.read().split()
#     k, m, n = int(data[0]), int(data[1]), int(data[2])
# probability_dominant = (k*(m+n) + 0.5*m*n + 0.5*k*(k-1) + 0.75/2*m*(m-1))/((k+n+m)*(k+n+m-1)/2)
# print(probability_dominant)
# probability_recessive = (0.5*m*n + 0.5*n*(n-1) + 0.125*m*(m-1))/((k+n+m)*(k+n+m-1)/2)

# # Question 8 - Translating RNA into Protein
# # https://rosalind.info/problems/prot/
# from important_data import dictionary_of_amino_acids
#
# with open("data_strings", "r") as file:
#     string = file.read().strip()
#
# result = ""
# for substring in [string[n: n+3] for n in range(0, len(string), 3)]:
#     if dictionary_of_amino_acids[substring] == "Stop":
#         break
#     elif substring:
#         result += dictionary_of_amino_acids[substring]
# print(result)

# # Question 9 - Finding a Motif in DNA
# # https://rosalind.info/problems/subs/
# with open("data_strings", "r") as file:
#     data = file.readlines()
#     string_s = data[0].strip()
#     string_t = data[1].strip()
#
# substrings_list = [string_s[n: n+len(string_t)] for n in range(0, len(string_s) - len(string_t) + 1)]
# print(" ".join([str(i+1) for i in range(len(substrings_list)) if substrings_list[i] == string_t]))

# # Question 10 - Consensus Strings and Profiling
# # https://rosalind.info/problems/cons/
# import pandas as pd
#
# with open("data_strings", "r") as file:
#     string = "".join(line.strip() for line in file.readlines())
#
# string_list = string.split(">")[1:]
# strand_length = len(string_list[0]) - 10
# df = pd.DataFrame([list(strand[-strand_length:]) for strand in string_list])
# new_df = pd.DataFrame({base: [df[column].to_list().count(base) for column in df.columns] for base in ["A", "C", "G", "T"]})
# new_df = new_df.transpose()
# print("".join([new_df[column].idxmax() for column in new_df.columns][3:]))
# for row in list(new_df.index):
#     print(f"{row}: " + " ".join([str(df[column].to_list().count(row)) for column in df.columns[3:]]))

# # Question 11 - Mortal Fibonacci Rabbits
# # https://rosalind.info/problems/fibd/
# with open("data_strings", "r") as file:
#     data = file.read().strip()
#     n = int(data.split()[0])
#     m = int(data.split()[1])
# rabbits_after_n_months = [0]*m + [1]
# number_born = [0]*m + [1]
# # new_list = [0]*m + [1]
# # num = 1
# for number in range(1, n):
#         # num += 1
#         try:
#             number_born += [sum(number_born[-m:-1])]
#         except TypeError:
#             number_born += number_born[-m:-1]
#         # number_born = number_born[1:]
#         # new_list += [sum(number_born[-1:-num:-1]) - sum(number_born[-m - 1: - m - num:-1]) + 1]
#         rabbits_after_n_months += [number_born[-1] + rabbits_after_n_months[-1] - number_born[-m-1]]
#         # rabbits_after_n_months = rabbits_after_n_months[1:]
# print(rabbits_after_n_months[-1])
# print(rabbits_after_n_months[m:])
# # print(new_list[m:])

# Question 12 - Overlap Graphs
# https://rosalind.info/problems/grph/
# with open("data_strings", "r") as file:
#     data = [line.strip() for line in file.readlines()]
#     string_dict = {string[:13]: string[13:] for string in "".join(data).split(">")[1:]}
#
# for key_s, string_s in string_dict.items():
#     for key_t, string_t in string_dict.items():
#         if string_s != string_t and string_s[-3:] == string_t[:3]:
#             print(f"{key_s} {key_t}")

# # Question 13 - Calculating Expected Offspring
# # https://rosalind.info/problems/iev/
# with open("data_strings", "r") as file:
#     data = file.read().strip()
#     AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa = [int(element) for element in data.split()]
#
# number_of_dominant_offspring = 2 * (AA_AA + AA_aa + AA_Aa) + 1 * Aa_aa + 1.5 * Aa_Aa
# print(number_of_dominant_offspring)

# # Question 14 - Finding a Shared Motif
# # https://rosalind.info/problems/lcsm/
# # Note - Please do not repeat this program without significant reason. Due to the lengths of the strings involved and
# # the brute force nature of this algorithm, this problem has a high time complexity.
# with open("data_strings", "r") as file:
#     data = [line.strip() for line in file.readlines()]
#     string_list = [string[4:] for string in "".join(data).split(">Rosalind_")][1:]
#     lengths = [len(string) for string in string_list]
#     min_length = min(lengths)
#
# for n in range(min_length, 0, -1):
#     for substring in [string_list[lengths.index(min_length)][i: i+n] for i in range(min_length-n + 1)]:
#         if all([substring in string for string in string_list]):
#             print(substring)
#             break
#     else:
#         continue
#     break

# # Question 15 - Independent Alleles
# # https://rosalind.info/problems/lia/
# from math import factorial
#
# with open("data_strings", "r") as file:
#     data = file.read().split()
#     k = int(data[0].strip())
#     n = int(data[1].strip())
#
# # Upon careful consideration, P(Aa, Bb) = P(Aa)^2. P(Aa) = 1 - P(AA) - P(aa). Number_of_homozygous_dominant = number_of_homozygous_recessive
# # N(AA) = 2^(k-1) + 0.5(N-1)(AA)
# # Pk(AA) = (1+P(k-1)(AA))/4
# # probability = 1
# # for number in range(k):
# #     probability = (1+probability)/4
# # probability = 1/3 + (2/3)/(4**k)
# #
# # probability = probability**2
# probability = 0.25
# if 0 < n < 2**(k-1):
#     combination = factorial(2 ** k) / (factorial(2 ** k - n + 1) * factorial(n - 1))
#     final_probability = 1
#     for number in range(n)[::-1]:
#         final_probability -= combination*(probability**number)*((1-probability)**(2**k - number))
#         combination *= number/(2**k - number + 1)
# else:
#     combination = factorial(2**k)/(factorial(2**k - n)*factorial(n))
#     final_probability = 0
#     for number in range(n, 2**k + 1):
#         final_probability += combination*(probability**number)*((1-probability)**(2**k - number))
#         combination *= (2**k - number)/(number+1)
# print(round(final_probability, 3))

# # Question 16 - Finding a Protein Motif
# # https://rosalind.info/problems/mprt/
# from bs4 import BeautifulSoup
# from requests import get
#
# with open("data_strings", "r") as file:
#     data = file.readlines()
#     access_ids = [line.strip() for line in data]
#
# dictionary_of_ids = {}
# for access_id in access_ids:
#     response = get(f"http://www.uniprot.org/uniprot/{access_id.split('_')[0]}.fasta")
#     soup = BeautifulSoup(response.content, "html.parser")
#     string = "".join(soup.text.split("\n")[1:])
#
#     for i in [i for i in range(len(string) - 3) if string[i] == "N"]:
#         if "P" not in [string[i+1], string[i+3]] and string[i+2] in ["S", "T"]:
#             if dictionary_of_ids.get(access_id) is None:
#                 dictionary_of_ids[access_id] = f"{i + 1}"
#             else:
#                 dictionary_of_ids[access_id] += f" {i + 1}"
#
# for key, value in dictionary_of_ids.items():
#     print(key)
#     print(value)

# # Question 17 - Inferring MRNA from Protein
# # https://rosalind.info/problems/mrna/
# from important_data import reverse_translation_dictionary
#
# with open("data_strings", "r") as file:
#     string = file.read().strip()
#
# product = 1
# for amino_acid in list(string):
#     product *= len(reverse_translation_dictionary[amino_acid])
#     product = product % 1000000
#
# product *= len(reverse_translation_dictionary["Stop"])
# product = product % 1000000
#
# print(product)

# # Question 18 - Open Reading Frames
# # https://rosalind.info/problems/orf/
# from important_data import reverse_translation_dictionary, dictionary_of_amino_acids
#
# with open("data_strings", "r") as file:
#     data = [line.strip() for line in file.readlines()[1:]]
#     string = "".join(data)
#
# string_s = string.replace("T", "U")
# string_t = string_s.replace("A", "u").replace("U", "a").replace("C", "g").replace("G", "c").upper()[::-1]
# substring_list = []
#
# for string in [string_s, string_s[1:], string_s[2:], string_t, string_t[1:], string_t[2:]]:
#     codons = [string[n:n+3] for n in range(0, len(string) - 2, 3)]
#     start_indices = [3*i for i in range(len(codons)) if codons[i] == "AUG"]
#     for start_index in start_indices:
#         stop_list = [3*i for i in range(len(codons[int(start_index/3):])) if dictionary_of_amino_acids[codons[i + int(start_index/3)]] == "Stop"]
#         if stop_list:
#             stop_index = start_index + min(stop_list)
#             substring = "".join([dictionary_of_amino_acids[codon] for codon in codons[int(start_index/3): int(stop_index/3)]])
#             if substring not in substring_list:
#                 substring_list.append(substring)
#
# for substring in substring_list:
#     print(substring)

# # Question 19 - Enumerating Gene Orders
# # https://rosalind.info/problems/perm/
#
#
# def permutation(given_list):
#     if len(given_list) == 2:
#         return [given_list, given_list[::-1]]
#     elif len(given_list) == 1:
#         return given_list
#     else:
#         permutation_list = []
#         for n in range(len(given_list)):
#             for element in permutation(given_list[:n] + given_list[n+1:]):
#                 permutation_list += [[given_list[n]] + element]
#         return permutation_list
#
#
# with open("data_strings", "r") as file:
#     n = int(file.read().strip())
#
# permutation_list = permutation(list(range(1, n+1)))
# print(len(permutation_list))
# for ordering in permutation_list:
#     print(" ".join([str(element) for element in ordering]))

# # Question 20 - Calculating Protein Mass
# # https://rosalind.info/problems/prtm/
# from important_data import monoisotopic_mass_table
#
# with open("data_strings", "r") as file:
#     string = file.read().strip()
#
# print(sum([monoisotopic_mass_table[character] for character in list(string)]))

# # Question 21 - Locating Restriction Sites
# # https://rosalind.info/problems/revp/
# with open("data_strings", "r") as file:
#     data = file.readlines()[1:]
#     string_s = "".join([line.strip() for line in data])
#
# string_t = string_s.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c").upper()
#
# for number in range(4, min(len(string_s)+1, 13)):
#     for i in range(len(string_s) - number + 1):
#         if string_s[i: i+number] == string_t[i: i+number][::-1]:
#             print(i+1, number)

# # Question 22 - RNA Splicing
# # https://rosalind.info/problems/splc/
# from important_data import reverse_translation_dictionary, dictionary_of_amino_acids
#
#
# def check_for_exons(given_string):
#     global substrings
#     for substring in substrings:
#         if substring in given_string:
#             start_index = given_string.find(substring)
#             given_string = given_string[:start_index] + given_string[start_index + len(substring):]
#             return check_for_exons(given_string)
#     return given_string
#
#
# with open("data_strings", "r") as file:
#     data = [line.strip() for line in file.readlines()]
#     strings = "".join(data).split(">Rosalind_")[1:]
#     string_s = strings[0][4:]
#     substrings = [string[4:] for string in strings[1:]]
#
# string_s = check_for_exons(string_s)
# transcripted_string = string_s.replace("T", "U")
# codons = [transcripted_string[n:n+3] for n in range(0, len(transcripted_string) - 2, 3)]
#
# if "AUG" in codons and any([stop_codon in codons for stop_codon in reverse_translation_dictionary["Stop"]]):
#     start_index = codons.index("AUG")
#     stop_index = min([i for i in range(len(codons)) if dictionary_of_amino_acids[codons[i]] == "Stop"])
#     print("".join([dictionary_of_amino_acids[codons[i]] for i in range(start_index, stop_index)]))

# # Question 23 - Enumerating k-mers Lexicographically
# # https://rosalind.info/problems/lexf/
#
#
# def permutation_of_length(given_list, n):
#     if n == 1:
#         return [[element] for element in given_list]
#     else:
#         result_list = []
#         for i in range(len(given_list)):
#             for permutation in permutation_of_length(given_list, n-1):
#                 result_list += [[given_list[i]] + permutation]
#         return result_list
#
#
# with open("data_strings", "r") as file:
#     data = file.readlines()
#     alphabet = [char.strip() for char in data[0].split()]
#     number = int(data[1].strip())
#
# alphabet.sort()
#
# for ordering in permutation_of_length(alphabet, number):
#     print("".join(ordering))

# # Question 24 - Longest Increasing Subsequence
# # https://rosalind.info/problems/lgis/
# from random import shuffle
#
#
# def longest_subsequence2(given_list, increasing=True):
#     sequences_list = []
#     for index in list(range(len(given_list)))[::-1]:
#         if increasing:
#             list_of_sequences = [subsequence for subsequence in sequences_list if subsequence[-1] > given_list[index]]
#             if list_of_sequences:
#                 max_sequence = max(
#                     [[integer for integer in subsequence if integer > sequence[index]] for subsequence in list_of_sequences],
#                     key=len)
#                 sequences_list.append([sequence[index]] + max_sequence)
#                 if max_sequence in sequences_list:
#                     sequences_list.remove(max_sequence)
#             else:
#                 sequences_list.append([sequence[index]])
#         elif not increasing:
#             list_of_sequences = [subsequence for subsequence in sequences_list if subsequence[-1] < given_list[index]]
#             if list_of_sequences:
#                 max_sequence = max(
#                     [[integer for integer in subsequence if integer < sequence[index]] for subsequence in list_of_sequences],
#                     key=len)
#                 sequences_list.append([sequence[index]] + max_sequence)
#                 if max_sequence in sequences_list:
#                     sequences_list.remove(max_sequence)
#             else:
#                 sequences_list.append([sequence[index]])
#     return max(sequences_list, key=len)
#
#
# def longest_subsequence(given_list, increasing=True):
#     global number
#     if len(given_list) < 2:
#         return given_list
#     else:
#         max_length = 0
#         result_list = []
#         if not increasing:
#             for i in range(len(given_list)):
#                 if len(given_list) - i > max_length and given_list[i] > max_length:
#                     list_of_values = [given_list[n] for n in range(len(given_list)) if
#                                       n > i and given_list[n] < given_list[i]]
#                     if len(list_of_values) >= max_length:
#                         result_list.append([given_list[i]] + longest_subsequence(list_of_values, increasing=False))
#                         if len(result_list[-1]) - 1 > max_length:
#                             max_length = len(result_list[-1]) - 1
#             return max(result_list, key=len)
#         if increasing:
#             for i in range(len(given_list)):
#                 if len(given_list) - i > max_length and (number - given_list[i]) >= max_length:
#                     list_of_values = [given_list[n] for n in range(len(given_list)) if
#                                       n > i and given_list[n] > given_list[i]]
#                     if len(list_of_values) >= max_length:
#                         result_list.append([given_list[i]] + longest_subsequence(list_of_values, increasing=True))
#                         if len(result_list[-1]) - 1 > max_length:
#                             max_length = len(result_list[-1]) - 1
#             return max(result_list, key=len)
#
#
# with open("data_strings", "r") as file:
#     data = file.readlines()
#     number = int(data[0].strip())
#     sequence = [int(element.strip()) for element in data[1].strip().split()]
#
# # print(" ".join([str(element) for element in longest_subsequence(sequence, increasing=True)]))
# # print(" ".join([str(element) for element in longest_subsequence(sequence, increasing=False)]))
#
# print(" ".join([str(element) for element in longest_subsequence2(sequence)]))
# print(" ".join([str(element) for element in longest_subsequence2(sequence, increasing=False)]))

# # Question 25 - Genome Assembly as a Shortest Superstring
# # https://rosalind.info/problems/long/
# with open("data_strings", "r") as file:
#     data = "".join([line.strip() for line in file]).split(">Rosalind_")[1:]
#     data = [element[4:] for element in data]
#
#
# # def find_overlap(string_s, given_list):
# #     original_string = string_s
# #     start_append_index = -1
# #     end_append_index = -1
# #     if string_s in given_list:
# #         new_list = [sequence for sequence in given_list if sequence != string_s]
# #     else:
# #         new_list = given_list
# #     for n in range(len(string_s)//2, len(string_s) + 1)[::-1]:
# #         for sequence in new_list:
# #             if string_s[-n:] == sequence[:n] and start_append_index < 0:
# #                 string_s += sequence[n:]
# #                 start_append_index = new_list.index(sequence)
# #                 new_list[start_append_index] = string_s
# #                 break
# #         for sequence in new_list:
# #             if string_s[:n] == sequence[-n:] and end_append_index < 0:
# #                 string_s = sequence + string_s[n:]
# #                 end_append_index = new_list.index(sequence)
# #                 new_list[end_append_index] = string_s
# #                 break
# #         if start_append_index >= 0 and end_append_index >= 0:
# #             break
# #     if end_append_index >= 0 and start_append_index >= 0:
# #         new_list[end_append_index] += new_list[start_append_index][len(original_string):]
# #         new_list.remove(new_list[start_append_index])
# #     return new_list
#
#
# def concatenate(string_s, dictionary_of_strings):
#     start_length = len(data[dictionary_of_strings[string_s][0]])
#     end_length = len(data[dictionary_of_strings[string_s][-1]])
#     for n in range(start_length//2, start_length + 1)[::-1]:
#         for sequence in [key for key in list(dictionary_of_strings.keys()) if key != string_s]:
#             if string_s[:n] == sequence[-n:]:
#                 dictionary_of_strings[sequence + string_s[n:]] = dictionary_of_strings[sequence] + dictionary_of_strings[string_s]
#                 dictionary_of_strings.pop(sequence)
#                 dictionary_of_strings.pop(string_s)
#                 string_s = sequence + string_s[n:]
#             else:
#                 continue
#             break
#     for n in range(end_length//2, end_length + 1)[::-1]:
#         for sequence in [key for key in list(dictionary_of_strings.keys()) if key != string_s]:
#             if string_s[-n:] == sequence[:n]:
#                 dictionary_of_strings[string_s + sequence[n:]] = dictionary_of_strings[string_s] + dictionary_of_strings[sequence]
#                 dictionary_of_strings.pop(sequence)
#                 dictionary_of_strings.pop(string_s)
#             else:
#                 continue
#             break
#     return dictionary_of_strings
#
#
# strings_dict = {data[i]: [i] for i in range(len(data))}
# while len(strings_dict.keys()) > 1:
#     strings_dict = concatenate(list(strings_dict.keys())[0], strings_dict)
#
# for key, value in strings_dict.items():
#     print([data[value[i]] in key for i in range(len(value))])
# print(list(strings_dict.keys())[0])

# # Question 26 - Perfect Matchings and RNA Secondary Structures
# # https://rosalind.info/problems/pmch/
# from math import factorial
#
# with open("data_strings", "r") as file:
#     data = list("".join([line.strip() for line in file.readlines()[1:]]))
#
# print(factorial(data.count("A"))*factorial(data.count("C")))

# # Question 27 - Partial Permutations
# # https://rosalind.info/problems/pper/
# with open("data_strings", "r") as file:
#     data = file.read().split()
#     n = int(data[0].strip())
#     k = int(data[1].strip())
#
# permutations = 1
# for i in range(n - k + 1, n + 1):
#     permutations *= i
#     permutations = permutations % 1000000
# print(permutations)

# # Question 28 - Modeling Random Genomes
# # https://rosalind.info/problems/prob/
# from math import log10
# with open("data_strings", "r") as file:
#     data = file.readlines()
#     s = list(data[0].strip())
#     A = [float(probability) for probability in data[1].strip().split()]
#
# B = [(s.count("G") + s.count("C"))*log10(probability/2) + (s.count("A") + s.count("T"))*log10((1-probability)/2) for probability in A]
# print(" ".join([str(round(probability, 3)) for probability in B]))

# # Question 29 - Enumerating Oriented Gene Orderings
# # https://rosalind.info/problems/sign/
# with open("data_strings", "r") as file:
#     n = int(file.read().strip())
#
#
# def signed_permutation(given_list):
#     if len(given_list) == 1:
#         return [[-given_list[0]], [given_list[0]]]
#     else:
#         permutation_list = []
#         for n in range(len(given_list)):
#             for element in signed_permutation(given_list[:n] + given_list[n+1:]):
#                 permutation_list += [[given_list[n]] + element, [-given_list[n]] + element]
#         return permutation_list
#
#
# permutation_list = signed_permutation(list(range(1, n+1)))
# print(len(permutation_list))
# for ordering in permutation_list:
#     print(" ".join([str(n) for n in ordering]))

# # Question 30 - Finding a spliced motif
# # https://rosalind.info/problems/sseq/
# with open("data_strings", "r") as file:
#     data = "".join([line.strip() for line in file.readlines()]).split(">Rosalind_")[1:]
#     if data[0][3].isdigit():
#         string_s = list(data[0][4:])
#         string_t = list(data[1][4:])
#     else:
#         string_s = list(data[0][2:])
#         string_t = list(data[1][2:])
#
# indices = [0]
# for character in string_t:
#     indices.append(max(indices) + string_s[max(indices):].index(character) + 1)
#
# print(" ".join([str(index) for index in indices[1:]]))

# # Question 31 - Transitions and Transversions
# # https://rosalind.info/problems/tran/
# with open("data_strings", "r") as file:
#     data = "".join([line.strip() for line in file.readlines()]).split(">Rosalind_")[1:]
#     if data[0][3].isdigit():
#         string_s = data[0][4:]
#         string_t = data[1][4:]
#     else:
#         string_s = data[0][2:]
#         string_t = data[1][2:]
#
# number_of_transitions = 0
# number_of_transversions = 0
# for i in range(len(string_s)):
#     if string_s[i] != string_t[i]:
#         if {string_s[i], string_t[i]} in [{"A", "G"}, {"C", "T"}]:
#             number_of_transitions += 1
#         else:
#             number_of_transversions += 1
#
# print(number_of_transitions/number_of_transversions)

# # Question 32 - Completing a Tree
# with open("data_strings", "r") as file:
#     data = [line.strip() for line in file.readlines()]
#     n = int(data[0])
#     edges = [line.split() for line in data[1:]]
#
# print(n - 1 - len(edges))

# # Question 33 - Catalan Numbers and Secondary Structures
# # https://rosalind.info/problems/cat/
# def is_symmetric(given_list):
#     if given_list.count("C") == given_list.count("G") and given_list.count("A") == given_list.count("U"):
#         return True
#     return False
#
#
# def calculate_catalan_numbers(list1, list2):
#     global dictionary_of_catalan_numbers, dict_of_base_pairs
#     result = 1
#     for basepair_list in [list1, list2]:
#         product = 0
#         if basepair_list:
#             for n in [n for n in range(len(basepair_list))[1::2] if basepair_list[n] == dict_of_base_pairs[basepair_list[0]]]:
#                 if is_symmetric(basepair_list[1: n]) and is_symmetric(basepair_list[n+1:]):
#                     keys_list = list(dictionary_of_catalan_numbers.keys())
#                     if tuple(basepair_list[1:n]) in keys_list:
#                         value1 = dictionary_of_catalan_numbers[tuple(basepair_list[1:n])]
#                     else:
#                         value1 = calculate_catalan_numbers(basepair_list[1:n], [])
#                         dictionary_of_catalan_numbers[tuple(basepair_list[1:n])] = value1
#                     if tuple(basepair_list[n+1:]) in keys_list:
#                         value2 = dictionary_of_catalan_numbers[tuple(basepair_list[n+1:])]
#                     else:
#                         value2 = calculate_catalan_numbers(basepair_list[n+1:], [])
#                         dictionary_of_catalan_numbers[tuple(basepair_list[n+1:])] = value2
#                     product += (value1*value2) % 1000000
#         elif not basepair_list:
#             product = 1
#         result *= product % 1000000
#     return result % 1000000
#
#
# with open("data_strings", "r") as file:
#     data = [line.strip() for line in file.readlines()[1:]]
#     dna_list = list("".join(data))
#
# dictionary_of_catalan_numbers = {}
# dict_of_base_pairs = {"A": "U", "C": "G", "U": "A", "G": "C"}
# print(calculate_catalan_numbers(dna_list, []))

# # Question 34 - Error Correction in Reads
# def reverse_complement(string):
#     return string.replace("T", "a").replace("A", "t").replace("G", "c").replace("C", "g").upper()[::-1]
#
#
# def hamming_distance(string1, string2):
#     if len([n for n in range(len(string2)) if string2[n] != string1[n]]) == 1:
#         return True
#     return False
#
#
# with open("data_strings", "r") as file:
#     reads = [line.strip() for line in file.readlines()][1::2]
#
# reverse_reads = [reverse_complement(read) for read in reads]
# correct_reads = list(set([read for read in reads if reverse_reads.count(read) + reads.count(read) >= 2]))
# correct_reads.extend([reverse_complement(read) for read in correct_reads])
# incorrect_reads = [string for string in reads if string not in correct_reads]
# incorrect_reads = {incorrect_string: [correct_string for correct_string in correct_reads if hamming_distance(incorrect_string, correct_string)][0] for incorrect_string in incorrect_reads}
# for key, value in incorrect_reads.items():
#     print(f"{key}->{value}")

# # Question 35 - Counting Phylogenetic Ancestors
# # https://rosalind.info/problems/inod/
# with open("data_strings", "r") as file:
#     n = int(file.read().strip())
# phylogenetic_ancestors_number = {3: 1, 2: 0}
#
#
# def count_phylogenetic_ancestors(number):
#     global phylogenetic_ancestors_number
#     if number in list(phylogenetic_ancestors_number.keys()):
#         return phylogenetic_ancestors_number[number]
#     elif number % 2 == 0:
#         result = int(number/2) + count_phylogenetic_ancestors(int(number/2))
#         phylogenetic_ancestors_number[number] = result
#         return result
#     elif number % 2 == 1:
#         result = int((number-1)/2) + count_phylogenetic_ancestors((number+1)/2)
#         phylogenetic_ancestors_number[number] = result
#         return result
#
#
# print(n - 2)
# # Trivial solution: The answer is simply n - 2 for a given n

# # Question 36 - k-Mer composition
# # https://rosalind.info/problems/kmer/
# k = 4
# permutation_dict = {1: ["A", "C", "G", "T"]}
# with open("data_strings", "r") as file:
#     data = [line.strip() for line in file.readlines()[1:]]
#     string = "".join(data)
#
#
# def permutation(k):
#     global permutation_dict
#     if permutation_dict.get(k) is not None:
#         return permutation_dict.get(k)
#     elif k > 1:
#         result = []
#         for element in ["A", "C", "G", "T"]:
#             for ordering in permutation(k-1):
#                 result += [element + "".join(ordering)]
#         permutation_dict[k] = result
#         return result
#
# kmers_list = ["".join(ordering) for ordering in permutation(4)]
# string_list = [string[i:i + k] for i in range(len(string) - k + 1)]
# print(" ".join([str(string_list.count(kmer)) for kmer in kmers_list]))

# # TODO Question 37
# # Question 37 - Finding a Shared Spliced Motif
# # https://rosalind.info/problems/lcsq/
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
# def dictionary_of_indices(string1, string2):
#     result_dictionary = {}
#     for n in range(len(string1)):
#         try:
#             result_dictionary[n] = min([number for number in range(len(string2)) if
#                                         string2[number] == string1[n] and number not in list(
#                                             result_dictionary.values())])
#         except ValueError:
#             pass
#     return result_dictionary
#
#
# def longest_subsequence(string1, string2):
#     if tuple([string1, string2]) in list(dictionary_of_longest_subsequences.keys()):
#         return dictionary_of_longest_subsequences[tuple([string1, string2])]
#     dict_of_indices = dictionary_of_indices(string1, string2)
#     if list(dict_of_indices.keys()):
#         s_index = min(list(dict_of_indices.keys()))
#         t_index = dict_of_indices[s_index]
#         if s_index == len(string1) - 1 or t_index == len(string2) - 1:
#             return string1[s_index]
#         else:
#             result_subsequence = longest_subsequence(string1[s_index + 1:], string2[t_index + 1:])
#             dictionary_of_longest_subsequences[tuple([string1, string2])] = string1[s_index] + result_subsequence
#             return string1[s_index] + result_subsequence
#     else:
#         return ""
#
#
# # result_dict = {}
# # def longest_subsequence_by_method2(string1, string2):
# #     if tuple([string1, string2]) in list(result_dict.keys()):
# #         print("Accessing Dictionary")
# #         return result_dict[tuple([string1, string2])]
# #     if len(string1) > 0 and len(string2) > 0:
# #         if string1[-1] == string2[-1]:
# #             result = string1[-1] + longest_subsequence_by_method2(string1[-1], string2[-1])
# #             result_dict[tuple([string1, string2])] = result
# #             return result
# #         else:
# #             result = max([longest_subsequence_by_method2(string1[-1], string2), longest_subsequence_by_method2(string1, string2[-1])], key=len)
# #             result_dict[tuple([string1, string2])] = result
# #             return result
# #     else:
# #         return ""
#
# dictionary_of_longest_subsequences = {}
# list_of_longest_subsequences = []
# for n in range(len(string_s)):
#     if not list_of_longest_subsequences or len(string_s) - n > max([len(string) for string in list_of_longest_subsequences]):
#         list_of_longest_subsequences.append(longest_subsequence(string_s[n:], string_t))
#
# print(max(list_of_longest_subsequences, key=len))
# # print(longest_subsequence_by_method2("AU", "AU"))

# # Question 36 - Speeding Up Motif Finding
# # https://rosalind.info/problems/kmp/
# with open("data_strings", "r") as file:
#     string_s = "".join([line.strip() for line in file.readlines()[1:]])
#
# failure_array = [0]
# for k in range(len(string_s))[1:]:
#     length_list = [number for number in list(range(1, failure_array[-1]+2)[::-1]) if string_s[k + 1 - number] == string_s[0] and string_s[k] == string_s[number - 1]]
#     for length in length_list:
#         if string_s[k + 1 - length: k+1] == string_s[:length]:
#             failure_array.append(length)
#             break
#     if len(failure_array) != k+1:
#         failure_array.append(0)
# print(" ".join([str(number) for number in failure_array]))

# # Question 38 - Ordering Strings of Varying Length Lexicographically
# # https://rosalind.info/problems/lexv/
# with open("data_strings", "r") as file:
#     data = [line.strip() for line in file.readlines()]
#     characters = data[0].split()
#     number = int(data[1])
#
#
# def varying_length_permutations(given_list, n):
#     if n == 1:
#         return [[item] for item in given_list]
#     else:
#         result_list = []
#         for i in given_list:
#             for ordering in [[None]] + varying_length_permutations(given_list, n-1):
#                 result_list += [[i] + ordering]
#         return result_list
#
#
# result_list = ["".join([element for element in ordering if element is not None]) for ordering in varying_length_permutations(characters, number)]
# print("\n".join(result_list))

# # Question 39 - Maximum Matchings and RNA Secondary Structures
# # https://rosalind.info/problems/mmch/
# # Important Note - Rosalind always marks this problem as wrong, even if the code is correct. This is because Python 3.5
# # has much greater accuracy in calculation than the programming language Rosalind has used, hence the terms get rounded
# # off in the Rosalind answer.
# from math import factorial
# with open("data_strings", "r") as file:
#     string = list("".join([line.strip() for line in file.readlines()[1:]]))
#
# a, u, g, c = string.count("A"), string.count("U"), string.count("G"), string.count("C")
# print(int((factorial(max(a, u))*factorial(max(g, c)))/(factorial(max(a, u) - min(a, u))*factorial(max(g, c) - min(g, c)))))

# # Question 40 - Creating a Distance Matrix
# # https://rosalind.info/problems/pdst/
# with open("data_strings", "r") as file:
#     data = "".join([line.strip() for line in file.readlines()]).split(">Rosalind_")[1:]
#     if data[0][3].isdigit():
#         strings = [string[4:] for string in data]
#     else:
#         strings = [string[2:] for string in data]
#
# for string_s in strings:
#     result_list = ['{0:.5f}'.format(len([i for i in range(len(string_s)) if string_s[i] != string_t[i]])/len(string_s)) for string_t in strings]
#     print(" ".join(result_list))

# # Question 41 - Reversal Distance
# # https://rosalind.info/problems/rear/
# with open("data_strings", "r") as file:
#     data = [line.strip() for line in file.readlines() if line.strip() != ""]
#     list_of_strings = []
#     for i in range(len(data))[::2]:
#         list_of_strings.append([data[i].split().index(number) + 1 for number in data[i + 1].split()])
#
# dictionary_of_reversals = {}
# def reversal_length(given_list):
#     if dictionary_of_reversals.get(tuple(given_list)) is not None:
#         return dictionary_of_reversals.get(tuple(given_list))
#     if len(given_list) == 1:
#         return 0
#     if max(given_list) == given_list[-1]:
#         result = reversal_length(given_list[:-1])
#         dictionary_of_reversals[tuple(given_list)] = result
#         return result
#     if min(given_list) == given_list[0]:
#         result = reversal_length(given_list[1:])
#         dictionary_of_reversals[tuple(given_list)] = result
#         return result
#     n_max = given_list.index(max(given_list))
#     n_min = given_list.index(min(given_list))
#     result = 1 + min(reversal_length(given_list[:n_max] + given_list[n_max+1:][::-1]), reversal_length(given_list[:n_min][::-1] + given_list[n_min+1:]))
#     dictionary_of_reversals[tuple(given_list)] = result
#     return result
#
#
# print(" ".join([str(reversal_length(string_list)) for string_list in list_of_strings]))

# # Question 42 - Matching Random Motifs
# # https://rosalind.info/problems/rstr/
# with open("data_strings", "r") as file:
#     data = [line.strip() for line in file.readlines()]
#     n = int(data[0].split()[0])
#     p = float(data[0].split()[1])
#     string = data[1]
#
# probability = (p/2)**(string.count("G") + string.count("C"))*((1-p)/2)**(string.count("A")+string.count("T"))
# print(round(1 - (1-probability)**n, 3))

# # Question 43 - Counting Subsets
# # https://rosalind.info/problems/sset/
# with open("data_strings", "r") as file:
#     n = int(file.read().strip())
#
# result = 1
# for i in range(n):
#     result *= 2
#     if result > 1000000:
#         result = result % 1000000
# print(result)

# # Question 44 - Alternative Splicing
# # https://rosalind.info/problems/aspc/
# with open("data_strings", "r") as file:
#     data = file.read().strip().split()
#     n = int(data[0])
#     m = int(data[1])
#
#
# def power(exponent, base=2):
#     if powers_of_primes_dict[base].get(exponent) is not None:
#         return powers_of_primes_dict[base].get(exponent)
#     result = 1
#     for i in range(exponent):
#         result *= base
#         result = result % 1000000
#     powers_of_primes_dict[base][exponent] = result
#     return result
#
#
# dictionary_of_inverses = {}
# def modInverse(A, M):
#     if dictionary_of_inverses.get(A) is not None:
#         return dictionary_of_inverses[A]
#     for X in range(1, M):
#         if (A * X) % M == 1:
#             dictionary_of_inverses[A] = X
#             return X
#     return -1
#
#
# def primes_less_than_n():
#     n = int(data[0])
#     primes_list = [2]
#     for number in range(3, n+1):
#         is_prime = True
#         for prime in primes_list:
#             if number % prime == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes_list.append(number)
#     return primes_list
#
#
# def generate_legendre_dict(number):
#     global primes_list
#     primes_dict = {prime: 0 for prime in primes_list}
#     for prime in list(primes_dict.keys()):
#         prime_power = prime
#         while prime_power <= number:
#             primes_dict[prime] += number//prime_power
#             prime_power *= prime
#     return primes_dict
#
#
# combinations_dict = {0: 1, n: 1, 1: n, n-1: n}
# def combination(k):
#     global n, primes_list
#     k = min([k, n-k])
#     if combinations_dict.get(k) is not None:
#         return combinations_dict[k]
#     if k % 2 != 0 and k % 5 != 0 and combinations_dict.get(k-1) is not None:
#         combinations_dict[k] = combinations_dict[k-1] * (n - k + 1) * modInverse(k, 1000000)
#         combinations_dict[n-k] = combinations_dict[k]
#         return combinations_dict[k]
#     if (n-k) %2 != 0 and (n-k) % 5 != 0 and combinations_dict.get(k + 1) is not None:
#         combinations_dict[k] = combinations_dict[k+1] * (k+1) * modInverse(n-k, 1000000)
#         combinations_dict[n - k] = combinations_dict[k]
#         return combinations_dict[k]
#     k_legendre_dict = generate_legendre_dict(k)
#     n_k_legendre_dict = generate_legendre_dict(n-k)
#     combination_legendre_dict = {prime: legendre_dict[prime] - k_legendre_dict[prime] - n_k_legendre_dict[prime] for prime in primes_list}
#     result_combination = 1
#     for prime, value in combination_legendre_dict.items():
#         result_combination *= power(combination_legendre_dict[prime], prime)
#         result_combination = result_combination % 1000000
#     combinations_dict[k] = result_combination
#     combinations_dict[n-k] = result_combination
#     return result_combination
#
#
# primes_list = primes_less_than_n()
# powers_of_primes_dict = {prime: {0: 1, 1: prime} for prime in primes_list}
# legendre_dict = generate_legendre_dict(n)
#
# if m <= n/4:
#     combination_sum = power(n)
#     for number in range(m):
#         combination_sum -= combination(number)
#         combination_sum = int(combination_sum) % 1000000
# elif m <= n/2:
#     if n % 2 == 1:
#         combination_sum = power(n - 1)
#         for number in range(m, int((n + 1) / 2)):
#             combination_sum += combination(number)
#             combination_sum = int(combination_sum) % 1000000
#     else:
#         combination_sum = power(n - 1) - combination(n//2) / 2
#         for number in range(m, int(n / 2 + 1)):
#             combination_sum += combination(number)
#             combination_sum = int(combination_sum) % 1000000
# elif m <= 3 * n / 4:
#     if n % 2 == 1:
#         combination_sum = power(n - 1)
#         for number in range(int((n + 1) / 2), m):
#             combination_sum -= combination(number)
#             combination_sum = int(combination_sum) % 1000000
#     elif n % 2 == 0:
#         combination_sum = power(n - 1) + combination(n//2) / 2
#         for number in range(int(n / 2), m):
#             combination_sum -= combination(number)
#             combination_sum = int(combination_sum) % 1000000
# else:
#     combination_sum = 0
#     for number in range(m, n + 1):
#         combination_sum += combination(number)
#         combination_sum = int(combination_sum) % 1000000
#
# print(combination_sum)

# # Question 45 - Distances in Trees
# # https://rosalind.info/problems/nwck/
# with open("data_strings", "r") as file:
#     data = [line.strip() for line in file.readlines()]
# indices = [-1] + [i for i in range(len(data)) if data[i] == ""]
# indices += [len(data)]
# trees = [data[indices[i] + 1:indices[i+1]] for i in range(0, len(indices) - 1)]
#
#
# for tree in trees:
#     if tree:
#         xk, yk = tuple(tree[-1].split())
#         if xk == yk:
#             print(0)
#             continue
#         tree_data = "(" + tree[0][:-1] + ")"
#         x_index = tree_data.find(xk)
#         y_index = tree_data.find(yk)
#         x_path = []
#         y_path = []
#         for index in [index for index in range(max(x_index, y_index)) if tree_data[index] == "("]:
#             closing_index = min([i for i in range(index + 1, len(tree_data)) if tree_data[i] == ")" and tree_data[index:i+1].count("(") == tree_data[index:i+1].count(")")])
#             if index < x_index < closing_index:
#                 x_path.append([index, closing_index])
#             if index < y_index < closing_index:
#                 y_path.append([index, closing_index])
#         if x_path == y_path:
#             print(2)
#             continue
#         else:
#             common_path = [index for index in x_path if index in y_path]
#             if (common_path == x_path and x_index == y_path[len(common_path)][1] + 1) or (common_path == y_path and y_index == x_path[len(common_path)][1] + 1):
#                 print(len(x_path) + len(y_path) - 2*len([index for index in x_path if index in y_path]))
#                 continue
#             else:
#                 print(len(x_path) + len(y_path) - 2 * len([index for index in x_path if index in y_path]) + 2)
#                 continue

# # Question 46 - Set Operations
# # https://rosalind.info/problems/seto/
# with open("data_strings", "r") as file:
#     data = [line.strip() for line in file.readlines()]
#     n = int(data[0])
#     a = [int(number) for number in data[1][1:-1].split(",")]
#     b = [int(number) for number in data[2][1:-1].split(",")]
#
# union = []
# intersection = []
# a_minus_b = []
# b_minus_a = []
# a_complement = []
# b_complement = []
# for i in range(1, n+1):
#     in_b = True
#     if i not in a:
#         in_a = False
#         a_complement.append(i)
#     else:
#         in_a = True
#         union.append(i)
#     if i not in b:
#         in_b = False
#         b_complement.append(i)
#         if in_a:
#             a_minus_b.append(i)
#     else:
#         if in_a:
#             intersection.append(i)
#         else:
#             b_minus_a.append(i)
#             union.append(i)
#
# for result_list in [union, intersection, a_minus_b, b_minus_a, a_complement, b_complement]:
#     print("{" + ", ".join([str(element) for element in result_list]) + "}")

# # Question 47 - Reconstructing Evolutionary Histories
# # https://rosalind.info/problems/sort/
# with open("data_strings", "r") as file:
#     data = [line.strip() for line in file.readlines() if line.strip() != ""]
#     array_a = [int(element) for element in data[1].split()]
#     array_b = [array_a.index(int(element)) + 1 for element in data[0].split()]
#
#
# def reversal_length(given_list):
#     list_of_reversals = []
#     if len(given_list) == 1 or given_list == sorted(given_list):
#         return []
#     if max(given_list) == given_list[-1]:
#         list_of_reversals += reversal_length(given_list[:-1])
#         return list_of_reversals
#     if min(given_list) == given_list[0]:
#         list_of_reversals += [[reversal[0] + 1, reversal[1] + 1] for reversal in reversal_length(given_list[1:])]
#         return list_of_reversals
#     n_max = given_list.index(max(given_list))
#     n_min = given_list.index(min(given_list))
#     reversing_from_right = reversal_length(given_list[:n_max] + given_list[n_max+1:][::-1])
#     reversing_from_left = reversal_length(given_list[:n_min][::-1] + given_list[n_min+1:])
#     if len(reversing_from_right) > len(reversing_from_left):
#         list_of_reversals += [[1, n_min+1]] + [[reversal[0] + 1, reversal[1] + 1] for reversal in reversing_from_left]
#         return list_of_reversals
#     else:
#         list_of_reversals += [[n_max+1, len(given_list)]] + reversing_from_right
#         return list_of_reversals
#
# result = reversal_length(array_b)
# print(len(result))
# for reversal in result:
#     print(" ".join([str(element) for element in reversal]))

# # Question 48 - Inferring Protein from Spectrum
# # https://rosalind.info/problems/spec/
# with open("data_strings", "r") as file:
#     data = [float(element.strip()) for element in file.readlines()]
#
# from important_data import monoisotopic_mass_table
# new_mass_table = {}
# for key, value in monoisotopic_mass_table.items():
#     new_mass_table[round(value, 4)] = key
#
# result = []
# for i in range(len(data) - 1):
#     mass = data[i+1] - data[i]
#     min_dist = 10
#     result.append("X")
#     for key in new_mass_table.keys():
#         if abs(key - mass) < min_dist:
#             min_dist = abs(key - mass)
#             result[-1] = new_mass_table[key]
#
#
# print("".join(result))

# # Question 49 - Introduction to Pattern Matching
# # https://rosalind.info/problems/trie/
# with open("data_strings", "r") as file:
#     data = [line.strip() for line in file.readlines()]
#
# paths = {1: {}}
# max_node_number = 1
# for string in data:
#     node_number = 1
#     i = 0
#     for character in string:
#         if character in paths[node_number].keys():
#             node_number = paths[node_number][character]
#             continue
#         max_node_number += 1
#         paths[max_node_number] = {}
#         paths[node_number][character] = max_node_number
#         node_number = max_node_number
#
# for beginning_node, value in paths.items():
#     if value:
#         for character, ending_node in value.items():
#             print(f"{beginning_node} {ending_node} {character}")
