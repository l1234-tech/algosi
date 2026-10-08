f = open("input.txt")
n = int(f.readline())
a = [int(s) for s in f.readline().split()]
s = int(f.readline())

def solution(a , s):
    all_index = {}
    for i , x in enumerate(a , start = 1):
        need = s - x
        if need in all_index:
            print(all_index[need] , i)
            return 

        if need not in all_index:
            all_index[x] = i

    print(-1)

solution(a,s)