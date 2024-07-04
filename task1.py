a = len(arr) - 1        # O(1)
out = list()            # O(1)

while a > 0:            # O(log(n))
    out.append(arr[a])
    print(out)
    a = a // 1.7

merge_sort(out)         # O(n*Log(n))


# O(1) + O(log(n)) + O(n*Log(n)) = O(n*Log(n))
