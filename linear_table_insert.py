arr = list(map(int,input("Enter an array : ").split()))
num = int(input("Number : "))
insert = int(input("insert in position : "))

temp_arr = [0 for i in range(len(arr)+1)]

for i in range(len(arr)):
  if i < insert:
    temp_arr[i] = arr[i] 
  else:
    temp_arr[i+1] = arr[i]   
  
temp_arr[insert] = num

print(temp_arr)