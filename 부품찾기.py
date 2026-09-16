import sys

N = int(sys.stdin.readline().rstrip())
part = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
want = list(map(int, sys.stdin.readline().split()))

part.sort()

def binary_search(array, target, start, end):
  while start<=end:
    mid = (start+end) // 2

    if target == array[mid]:
      return mid
    elif target < array[mid]:
      end = mid - 1
    else:
      start = mid + 1
  return None

for i in want:
  result = binary_search(part,i,0,len(part)-1)
  if result != None:
    print("yes", end=" ")
  else:
    print("no", end=" ")