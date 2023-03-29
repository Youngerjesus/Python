a = ["one", "two", "three"]
b = [1, 2, 3]
c = [4, 5, 6]

result = {}

# zip 을 통해서 여러 개의 순회 가능한 객체를 인자로 받는다.
for x, y, z in zip(a,b,c):
    result[x] = y * z

print(result)

print({x: y * z for x, y, z in zip(a, b, c)})

print(dict((x, y * z) for x, y, z in zip(a, b, c)))