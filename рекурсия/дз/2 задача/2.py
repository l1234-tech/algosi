f = open("input.txt")

A = int(f.readline())
array = [int(s) for s in f.readline().split()]
S = int(f.readline())

def find_S(array, S):
    if S in array:
        return "Yes"
    all_sum = [array[0]]
    for i in range(len(array)):
        if i > 0:
            new_sum = []
            new_sum.append(array[i])
            for num in all_sum:
                new_sum.append(num + array[i])
            all_sum.extend(new_sum)
            if S in new_sum:
                return "Yes"
    if S in all_sum:
        return "Yes"
    else:
        return "No"

print(find_S(array, S))