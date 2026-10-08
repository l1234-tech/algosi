f = open("input.txt")
n, m = map(int, f.readline().split())
matrix = [list(map(str, s.split())) for s in f]

snake = []

while matrix:

    snake += matrix.pop(0)

    matrix = list(map(list, zip(*matrix)))[::-1]

result = " ".join(snake)
print(result)