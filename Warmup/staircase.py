n = int(input())
print(*[(num * '#').rjust(n, ' ') for num in range(1, n+1)], sep="\n")