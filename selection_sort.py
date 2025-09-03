def selection_sort(arr):
  l = len(arr)
  
  for i in range(l-1):
    min_index = i
    for j in range(i+1,l):
      if arr[min_index] > arr[j]:
        min_index = j
    arr[i],arr[min_index] = arr[min_index],arr[i]
    
  return arr

arr = [60,80,95,50,70]
print(selection_sort(arr))