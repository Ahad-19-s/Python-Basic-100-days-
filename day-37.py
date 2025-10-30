def func1():
    try: 
        l=[1,2,3,4]
        i=int(input("Enter the input : "))
        print (l[i])
        return 100;

    except:
        print("somr error occurred")
        return 111;

    finally:
        print ("i am always excuted")
    # print ("i am always excuted")

x=func1()
print(x)