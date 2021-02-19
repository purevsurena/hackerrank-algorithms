arr = sorted(list(map(int, input().rstrip().split())))
max = sum(arr[1:5])
min = sum(arr[0:4])
print(F"{min} {max}")