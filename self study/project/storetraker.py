# item 1_= 'phone ' 
# item1_price = 1_0
# item1_quantity = 5 
class Item :
    def calculate_total_price(self,x,y):
        return x * y




item1= Item()
item1.name = "phone "
item1.price = 20
item1.quantity = 5
print(item1.calculate_total_price(item1.price,item1.quantity))
 
# print (type(item1_)
# print (type (item1_name))
# print(type (item1_price))
# print(type(item1_quantity))

item2= Item()
item2.name = "Laptop "
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price,item2.quantity))



# class Student:
#     def __init__(self,name,roll,sub):
#         self.name = name 
#         self.roll = roll 
#         self.sub = sub 
# s1 = Student()
# print(s1.name )

        


