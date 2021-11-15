numbers = [-5,0]
queries = [[1,2,10], [2,2,20]]

# for i in range(len(queries)):
#     print(i)
#     for i in range(queries[i][0]-1,queries[i][1]):
#         pass
#     print(i, 'x')
for i in range(len(queries)):
    for i in range(queries[i][0]-1,queries[i][1]):
       print('range: ', range(queries[i][0]-1,queries[i][1]))

for i in range(len(queries)):
    result = 0
    x = queries[i][2]
    for i in range(queries[i][0]-1,queries[i][1]):
        if numbers[i] == 0:
            numbers[i] = numbers[i] + x
        else:
            numbers[i] = numbers[i]
    
        result = result + numbers[i]
        print(result)







# for i in range(len(queries)):
#     result = 0
#     for i in range(queries[i][0]-1,queries[i][1]):
#         result = result + numbers[i]
#     print(result)



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
