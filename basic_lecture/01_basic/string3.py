s = 'Hey. Hi thEre. Hey'
is_start = s.startswith('Hey')
print(is_start)
is_start = s.startswith('Hi')
print(is_start)

##

print(s.find('Hey'))
print(s.rfind('Hey')) # 뒤쪽에 있는 단어 부터 찾음
print(s.count('Hey'))
print(s.capitalize()) # 맨 앞 글자만 대문자화
print(s.upper()) # 전부 대문자
print(s.title()) # 단어 앞글자는 대문자로
print(s.replace("thEre", 'devson'))