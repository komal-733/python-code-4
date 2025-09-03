arr = [90,70,50,80,60,85]
mid = (0+len(arr))//2
for i in range(mid):
  arr[i],arr[len(arr)-i-1] = arr[len(arr)-i-1],arr[i]
print(arr)