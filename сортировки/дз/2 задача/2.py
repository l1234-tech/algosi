f = open("input.txt")

n = int(f.readline())

a = [int(s) for s in f.readline().split()]

def merge_and_count(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, left_inv = merge_and_count(arr[:mid])
    right, right_inv = merge_and_count(arr[mid:])
    
    merged = []
    inv_count = left_inv + right_inv
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, inv_count

_ , total = merge_and_count(a)
print(total)