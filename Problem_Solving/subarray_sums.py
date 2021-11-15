
# numbers = [5,10,10]
# queries = [[1,2,5]]

numbers = [-5,0]
queries = [[2,2,20], [1,2,10]]


def findSum(numbers, queries):
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
    print(findSum(numbers, queries))




# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     numbers_count = int(input().strip())

#     numbers = []

#     for _ in range(numbers_count):
#         numbers_item = int(input().strip())
#         numbers.append(numbers_item)

#     queries_rows = int(input().strip())
#     queries_columns = int(input().strip())

#     queries = []

#     for _ in range(queries_rows):
#         queries.append(list(map(int, input().rstrip().split())))

#     result = findSum(numbers, queries)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()