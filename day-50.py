f= open('myfile.txt','r')
while True:
    line = f.readline()
    print(line)
    m= line.split(",")[2]
    print(m)
    if not line:
        #  print(line,type(line))
        break
    