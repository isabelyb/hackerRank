n = 3

def factorial(n):
    # Write your code here
    if n > 1:
        n = n * factorial(n-1)
    return  n
    
    
    

if __name__ == '__main__':
    result = factorial(n)
    print(result)