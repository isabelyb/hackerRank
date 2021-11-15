
numbers = [5,10,10]
queries = [[1,2,5]]


def findSum(numbers, queries):
    for i in range(len(queries)):
        result = 0
        for i in range(queries[i][0]-1,queries[i][1]):
            result = result + numbers[i]
        print(result)

    

if __name__ == '__main__':
    findSum(numbers, queries)



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