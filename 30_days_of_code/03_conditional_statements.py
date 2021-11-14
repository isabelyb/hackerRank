'''
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not n is weird.
'''


if __name__ == '__main__':
    N = int(input().strip())
    if (N > 20) and (N %2 == 0):
        print('Not Weird')
    elif (N > 5) and (N %2 == 0):
         print('Weird')
    elif (N > 1) and (N %2 == 0):
        print('Not Weird')
    else:
        print('Weird')   


