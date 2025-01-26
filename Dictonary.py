#Dict. is mutuable ones you chnge the value it always change 

dict1 = {
'value' : 11
}
dict2 = dict1

print("Before dict2 value is updated")

print("dict1 =",dict1)
print("dict2 =",dict2)

print("\ndict1 points to:",id(dict1))
print("dict2  points to:",id(dict2 ))

dict2['value'] = 22

print("after updated the value of dict2")

print("dict1 =",dict1)
print("dict2 =",dict2 )

print("\ndict1 points to:",id(dict1))
print("dict2 points to:",id(dict2 ))
