# import math
# absolute = -5.999
# floor_test = 198.42

# result1 = math.fabs(absolute)
# result2 = math.floor(floor_test)

# print(result1, " is the absolute value of ", absolute)
# print(result2, "is the floor value of ", floor_test)

#File handling

# print("Here is my diary: \n")
# f1 = open("diary.txt", "r")
# print(f1.read())
# f1.close()

# print("\n Now let's create another diary ! ")

# f2 = open("diary2.txt", "w")
# f2.write ("Writing in my diary file ")
# f2.close()




#Exception Handling 


# try:
#     file = open("diaryy1.txt", "r")
# except FileNotFoundError:
#     print("File not found")


#import os       #importing os module

#Get the current working directory

#directory (cwd)

# cwd=os.getcwd()

# #print the current working directory

# print(" Cuurrent working directory ", cwd)




# import json
# variable= json.dumps(42)
# print(type(variable))

# import subprocess
# def new_user():
#     confirm = "N"
#     while confirm != "Y":
#         username = input("Enter thename of the user to add: ")
#         print("Use the username '" + username + "'? (Y/N)")
#         confirm = input().upper()
#         os.system("sudo adduser " + username)

# new_user()










