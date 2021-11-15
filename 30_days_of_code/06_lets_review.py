T = int(input().strip())

strings = []
for t in range (T):
    S = input()
    strings.append(S)

for i in range(len(strings)):
    print(strings[i][0::2],strings[i][1::2])



