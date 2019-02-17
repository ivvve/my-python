d = {'x': 10, 'y': 20}
print(d)
print(type(d))

print(d['x'])
print(d['y'])

##

d['x'] = 'hello'
d['y'] = 'world'
d['me'] = 'devson'
print(d)

##
# 생성
d = {'x': 10, 'y': 20}
d = dict(x=10, y=20)
d = dict([('a', 10), ('b', 20)])
