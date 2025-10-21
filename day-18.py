i = int(input("Enter the number: "))
print(i)
while(i<=38):
  i = int(input("Enter the number: "))
  print(i)

print("Done with the loop")

count = 5
while (count > 0):
  print(count)
  count = count - 1
else:
  print("I am inside else")

# do {
#   loop body;
# }while(condition);

for i in range (12):
  if(i==10):
    break
  if(i==5):
    print("skip the iteration")
    continue
  
    
  print ("5 X ",i+1," = ", 5*(i+1))