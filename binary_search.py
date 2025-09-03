def binary_search(arr,num):
  start = 0
  last = len(arr)-1
  while start <= last:
    mid = (start+last)//2
    if arr[mid] == num :
      return mid
    elif num > arr[mid]:
      start = mid+1
    else:
      last = mid-1
  return -1

arr = [50, 60, 70, 80, 85, 90]
num = int(input("Enter num you want to search : "))
ind = binary_search(arr,num)
if ind == -1:
  print(f"{num} is not present")
else:
  print(f"{num} is present in {ind} index")