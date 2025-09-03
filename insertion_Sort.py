def insertion_sort(arr):
  l = len(arr)
  
  for i in range(l):
    insert_ind = i
    insert_val = arr[i]
    for j in range(i-1,-1,-1):
      if arr[j] > insert_val:
        arr[j+1] = arr[j]
        insert_ind -= 1
    arr[insert_ind] = insert_val
    
  return arr
      
arr = [60,80,50,70,90,85]
arr = insertion_sort(arr)
print(arr)