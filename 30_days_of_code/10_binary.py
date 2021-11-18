from itertools import groupby


def max_ones():
    n_binary = bin(n)

    n_binary_str = list(n_binary[2:])

    n_binary_num = []
    for i in range(len(n_binary_str)):
        nums = int(n_binary_str[i])
        n_binary_num.append(nums)

    ones = [sum(ones) for i, ones in groupby(n_binary_num) if i == 1]

    result = max(ones)
    
    return result


if __name__ == '__main__':
    n = int(input().strip())
    max_ones()

