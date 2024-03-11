
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)


lcm_dict = {}
def lcm(given_list):
    given_list = sorted(given_list, reverse=True)
    if lcm_dict.get(tuple(given_list)) is not None:
        return lcm_dict[tuple(given_list)]
    if len(given_list) == 2:
        a = max(given_list)
        b = min(given_list)
        if lcm_dict.get(tuple([a, b])) is not None:
            return lcm_dict[tuple([a, b])]
        else:
            result = a * b // gcd(a, b)
            lcm_dict[tuple([a, b])] = result
            return result
    else:
        result = lcm([given_list[0], lcm(given_list[1:])])
        lcm_dict[tuple(given_list)] = result
        return result


bijection_lengths = {}
def max_bijection_length(n):
    if bijection_lengths.get(n) is not None:
        return bijection_lengths[n]
    if n < 5:
        bijection_lengths[n] = n
        return n
    else:
        result = max([lcm([i, max_bijection_length(n-i)]) for i in range(1, n)])
        bijection_lengths[n] = result
        return result


for i in range(1, 21):
    print(max_bijection_length(i))
