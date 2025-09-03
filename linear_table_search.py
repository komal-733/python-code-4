def linear_search(arr,num):
  count = 0 
  for i in range(len(arr)):
    if arr[i] == num:
      print(f"{num} is present in {i} index")
      count +=1
      break
  if count == 0:
    print(f"{num} in not present")

arr = [60,80,50,70,90,85]
num = int(input("Enter num you want to search : "))
linear_search(arr,num)