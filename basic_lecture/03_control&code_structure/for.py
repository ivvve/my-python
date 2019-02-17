some_list = [1, 2, 3, 4, 5]

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

##

for i in some_list:
    print(i)
else:
    print('done')

##

for c in 'abcd':
    print(c)

for word in ['My', 'Name', 'Is', 'YC']:
    if word == "Is":
        break
    print(word)
