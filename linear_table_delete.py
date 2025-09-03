arr = list(map(int,input("Enter a array : ").split()))
delete_ind = int(input("Enter delete index : "))

for i in range(len(arr)-1):
  if i >= delete_ind:
    arr[i]=arr[i+1]
    
print(arr[:-1])