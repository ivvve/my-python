a = {1, 2, 3, 4, 4, 4, 5, 6}
print('a : ', a) # 중복되는 값이 제거됨
print(type(a))

b = {2, 3, 3, 6, 7}
print('b : ', b)

## 차집합
print(a - b)
print(b - a)

## 교칩합
print(a & b)

## 합집합
print(a | b)

## 대칭 차집합
print(a ^ b)