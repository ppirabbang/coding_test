import sys

def binary_search(array,target,start,end):
  while start <= end:
    mid = (start+end) // 2
    if (array[mid] == target):
      return mid
    elif (array[mid] > target):
      end = mid - 1
    else:
      start = mid + 1
  return None

N = int(sys.stdin.readline().rstrip())
array = list(map(int,sys.stdin.readline().split()))
array.sort()
M = list(map(int,sys.stdin.readline().rstrip()))
find = list(map(int,sys.stdin.readline().split()))

for i in M:
  a = binary_search(array,i,0,len(array)-1)
  if a != None:
    print("yes", end=" ")
  else:
    print("no", end=" ")