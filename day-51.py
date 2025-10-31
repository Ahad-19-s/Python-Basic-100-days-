with open ('myfile.txt','r') as file:
    print(type(file))
    file.seek(3)

    print(file.read(12))
    print(file.tell())


   
    file.seek(24)
     
    print(file.read(12)) 
    file.close()
with open('requirments.txt','w')as f:
    f.write('hello world')
    f.truncate(4)

with open('requirments.txt','r')as f:
    print(f.read())