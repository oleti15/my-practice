# n=int(input())
# name_list=[]
# print(name_list)
# for i in range(n):
#     name=input()
#     name_list.append(name)



user_list=[]
n=int(input())
for i in range(n):
    user_dict={}
    user_dict['name']=input("enter name:")
    user_dict['id']=int(input("enter id"))
    user_list.append(user_dict)
print(user_list)


keyword=input()
filterd_List=[]
for user_dict in user_list:
    if keyword in user_dict['name']:
        filterd_List.append(user_dict)
print(filterd_List)       
