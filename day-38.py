a = int(input("Enter any value between 5 and 9"))

if(a<5  or a>9):
  raise  ValueError("Value should be between 5 and 9")
 
print(a)

class CustomError(Exception):

  pass

try:
  # code ...
  x=int(input("enter the number:"))
  if x<0:
    raise CustomError("negative number are not aloow")
  print("you  entered ", x)

except CustomError as e:
  print("Custom error occured ",e)
  # code...