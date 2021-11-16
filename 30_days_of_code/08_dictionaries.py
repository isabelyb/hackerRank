phone_book = {}

friends = [['ana', '12345678'], ['rosa', '58974463'], ['jenn', '89562417']]

#To save data from list in a dictionary

for i in range(len(friends)):
    phone_book.update({friends[i][0] : friends[i][1]})

print(phone_book)

# to find a value from a key in list
to_find = ['rosa', 'pepa', 'ana']

for i in to_find:
    if i in phone_book.keys():
        print(f'{i}={phone_book[i]}')
    else:
        print('Not found')


   
