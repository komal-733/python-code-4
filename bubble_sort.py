def bubble_sort(arr):
  l = len(arr)
  
  for i in range(l-1):
    for j in range(l-1-i):
      if arr[j] > arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
        
  return arr


arr = [60,50,95,80,70]
print(bubble_sort(arr))