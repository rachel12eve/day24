# open the file
from Tools.demo.beer import n
#
# file = open("text.txt")
# # read the file
# content = file.read()
# # print the content
# # print(content)
#
# # close the file to save the resources
# file.close()

#use with +as no need to close file
with open("/Users/rachel/OneDrive/桌面/text.txt") as file:
    content=file.read()
    print(content)
#
# #r=read only (default)
# #w= can write
# #a=append
# with open("text.txt", mode="a") as file:
#     file.write("New line.")
#     print(content)
#
# with open("new text.txt", mode="w") as file:
#     file.write("New line.")
#     print(content)