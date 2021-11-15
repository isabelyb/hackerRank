'''
Given an array,A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.
'''

def inverse():
    inv_arr = arr[::-1]

    for i in inv_arr:
        print(i, end=' ')


if __name__ == '__main__':
    n = int(input().strip())
    # to convert in list
    arr = list(map(int, input().rstrip().split()))
    
    inverse()
