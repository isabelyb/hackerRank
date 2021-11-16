'''
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.
'''

from sys import stdin

n = int(input().strip())

data_list = []
for i in range(n):
    friends = list(map(str, input().split()))
    data_list.append(friends)

print(data_list)

phone_book = {}
for i in range(len(data_list)):
    phone_book.update({data_list[i][0] : data_list[i][1]})

print(phone_book)



queries = []
while True:
    try:
        to_find = input()
        if len(to_find) != 0:
            queries.append(to_find)
        else:
            break

    except (EOFError,ValueError):
        break




print(queries)

for i in queries:
    if i in phone_book.keys():
        print(f'{i}={phone_book[i]}')
    else:
        print('Not found')


