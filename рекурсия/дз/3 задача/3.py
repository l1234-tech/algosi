f = open("input.txt")

n = int(f.readline())

a = [int(s) for s in f.readline().split()]

s = int(f.readline())
res = None 
def search(current_sum, position,curr_arr):
    global res
    if res is not None:
        return 

    if position == len(a):
        if current_sum  == s and len(curr_arr) > 0:
            res = curr_arr
        return 

    search(current_sum + a[position] , position + 1, curr_arr + [a[position]])

    search(current_sum , position + 1,curr_arr)

search(0, 0 , [])

if res is not None:
    print('Yes')
    print(len(res))
    print(' '.join(map(str, res)))

else:
    print('No')
