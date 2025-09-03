arr = [60,80,95,50,70]

min_index = 0

for i in range(1,len(arr)):
  if arr[min_index] > arr[i]:
    min_index = i
    
print(arr[min_index])