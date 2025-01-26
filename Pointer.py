# # integer are immuatable means ones we assigned a value of interger they can't be change .

# num1 = 11
# num2 = num1

# print("Before num2 value is updated")

# print("num1 =",num1)
# print("num2 =",num2)

# print("\nnum1 points to:",id(num1))
# print("\nnum2 points to:",id(num2))

# num2 = 22

# print("after updated the value of num 2")

# print("num1 =",num1)
# print("num2 =",num2)

# print("\nnum1 points to:",id(num1))
# print("\nnum2 points to:",id(num2))

head = {
            "value" :11,
            "next":{
                 "value" :3,
            "next":{
                        "value" :23,
            "next":{
                        "value" :7,
            "next": None
                        
            }
            }
            }

            }

print(head['next']['next']['value'])

# this will only un ith linked list
#print(my_linked_list.head.next.next.value)