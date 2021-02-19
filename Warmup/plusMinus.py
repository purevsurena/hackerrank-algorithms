import os

def plusMinus(arr):
  positive = negative = zero = 0
  total = len(arr)
  for num in arr:
      if num > 0:
        positive += 1
      elif num == 0:
        zero += 1
      else:
        negative += 1
  print(F"{positive/total:.6f}\n{negative/total:.6f}\n{zero/total:.6f}")

if __name__ == '__main__':
  n = int(input())

  arr = list(map(int, input().rstrip().split()))

  plusMinus(arr)
