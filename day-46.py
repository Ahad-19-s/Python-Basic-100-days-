import os

if not os.path.exists("data"):
    os.mkdir("data")
    

# for i in range(1, 101):
#     os.rename(f"data/tuorial{i}",f"data/Tuorial_day{i}") 
    # new_name = f"data/tuorial{i}_renamed"
    # if os.path.exists(old_name):
    #     os.rename(old_name, new_name)
    # else:
    #     print(f"File {old_name} does not exist")



# file=os.open("ahad.txt",os.tuorial14_renamed)
# os.exit()
folders= os.listdir("data")
     # print(folders)

# for i in folders:
#     print(i)
#     print(os.listdir(f"data/{i}"))

print(os.getcwd())