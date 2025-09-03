arr = [60,50,95,80,70]

for i in range(len(arr)-1):
  if arr[i] > arr[i+1]:
    arr[i],arr[i+1] = arr[i+1],arr[i]
  
print(arr[-1])