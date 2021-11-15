
def multiple(n):
    if n >= 2 and n <= 20:
        for i in range(1,11):    
            result = n * i
            print(f'{n} x {i} = {result}')


if __name__ == '__main__':
    n = int(input().strip())
    multiple(n)