word = 'python'
print(word[0])
print(word[2])
print(word[-1])
print(word[0:2]) # slice
print(word[:2])
print(word[2:])
# print(word[10]) # Error orccurred

##

# word[0] = 'J' # index로 문자 지정 불가
word = 'J' + word[1:]
print(word[:])
