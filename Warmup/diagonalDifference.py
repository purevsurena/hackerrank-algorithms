import os

def diagonalDifference(arr):
  left_diagonal = right_diagonal = 0
  length = len(arr) - 1
  for i in range(len(arr)):
      left_diagonal += arr[i][i]
      right_diagonal += arr[i][length - i]
  return abs(left_diagonal - right_diagonal)

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  n = int(input().strip())

  arr = []

  for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

  result = diagonalDifference(arr)

  fptr.write(str(result) + '\n')

  fptr.close()
