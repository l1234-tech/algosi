f = open("input.txt")
n, m = map(int, f.readline().split())

number = f.readline().strip()

result = []

curr_num = 0

for num in number:
    curr_num = curr_num * 10 + int(num)
    result.append(str(curr_num % m))

print(" ".join(result))