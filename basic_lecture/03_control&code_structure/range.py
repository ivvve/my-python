# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for i in num_list:
#     print(i)

for i in range(0, 10): # range(10)
    print(i)

for i in range(2, 10, 3):
    print(i)

# index를 사용하지 않음을 명시적으로 알리기위해 _로 지정
for _ in range(10):
    print('hello')