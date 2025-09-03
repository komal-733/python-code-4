def shell_sorting(arr):
  gap = len(arr)//2
  
  while gap:
    for i in range(gap,len(arr)):
      insert_val = arr[i]
      index = i
      while arr[index-gap] > insert_val and index-gap >= 0:
        arr[index] = arr[index-gap]
        index = index-gap
      arr[index] = insert_val
    gap = gap// 2
  return arr
arr = [9,6,5,8,0,7,4,3,1,2]
print(shell_sorting(arr))