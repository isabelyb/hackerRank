# numbers = [20,30,0,10]
# queries = [[1,3,10]]

# numbers = [5,10,10]
# queries = [[1,2,5]]

numbers = [-5,0]
queries = [[2,2,20], [1,2,10]]

def sumi(numbers, queries):
    result = []
    for q in queries:
        subarray_sums = 0
        x = q[2]
        for i in numbers[q[0]-1:q[1]]:
            if i == 0:
                i = i + x
            else:
                i = i
            subarray_sums = subarray_sums + i
        result.append(subarray_sums)
    return result

if __name__ == '__main__':
    print(sumi(numbers, queries))









### TO SUM ELEMENTS IN A LIST ###

''' Method 1: Sum()
x = [1,2,3,4]
y = [2,3]
numbers_list = []
for i in range((y[0]-1),(y[1])):    
    numbers_list.append(x[i])
    result = sum(numbers_list)
print(result) 
'''

''' Method 2: variable 0
x = [1,2,3,4]
y = [2,3]
result = 0
for i in range((y[0]-1),(y[1])):        
    result = result + x[i]
print(result) 
'''   
