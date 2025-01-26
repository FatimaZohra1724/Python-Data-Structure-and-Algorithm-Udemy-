#print("hello world")
# class Cookie:
#     def __init__(self,color):
#         self.color = color

#     def get_color(self):
#         return self.color
    
#     def set_color(self,color):
#         self.color = color

# cookie_one = Cookie('green')
# cookie_two = Cookie('blue')

# print('cookie one:',cookie_one.get_color())
# print('cookie two:',cookie_two.get_color())

class Cake:
    def __init__(self,Variety):
        self.Variety = Variety

    def get_Variety(self):
        return self.Variety
    
    def set_Variety(self,Variety):
        self.Variety = Variety
    
Cake_one = Cake('Black Forest')
Cake_two = Cake('Red Valvet')

print('Cake one Flavour is:' ,Cake_one.get_Variety())
print('Cake two Flavour is:' ,Cake_two.get_Variety())


Cake_one.set_Variety('Choclate')
Cake_two.set_Variety('DarkChoclate')

print('Cake one is now:',Cake_one.get_Variety())
print('Cake two is now:',Cake_two.get_Variety())