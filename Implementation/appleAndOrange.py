import os

def countApplesAndOranges(s, t, a, b, apples, oranges):
  apples_count = oranges_count = 0
  for apple in apples:
    cur_apple_distance = a + apple
    if cur_apple_distance >= s and cur_apple_distance <= t:
      apples_count += 1
  for orange in oranges:
    cur_orange_distance = b + orange
    if cur_orange_distance >= s and cur_orange_distance <= t:
      oranges_count += 1
  print(F"{apples_count}\n{oranges_count}") 

if __name__ == '__main__':
  st = input().split()
  s = int(st[0])
  t = int(st[1])
  ab = input().split()
  a = int(ab[0])
  b = int(ab[1])
  mn = input().split()
  m = int(mn[0])
  n = int(mn[1])

  apples = list(map(int, input().rstrip().split()))
  oranges = list(map(int, input().rstrip().split()))
  countApplesAndOranges(s, t, a, b, apples, oranges)
