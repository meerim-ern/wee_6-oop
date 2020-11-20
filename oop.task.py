# ##1
# class Student:
#     def __init__(self,name,lastname,department,ent_year):
#         self.name =name
#         self.lastname =lastname
#         self.department = department
#         self.ent_year = ent_year

#     def get_info(self):
#         print(f"{self.name}{self.lastname} поступил в {self.ent_year} на факультет {self.department}")


# ivanov =Student("Вася"," Иванов","Программирование",2017)
# ivanov.get_info()


##2 

# class BankAccount:
#     balance = 0
#     def withdraw(self,amount):
#         self.amount = amount
#         while BankAccount.balance >= amount:
#             new_balance = BankAccount.balance - amount
#             print(new_balance)
#             break
#         else:
#             print("Unavailable balance")

#     def deposit(self,amount):
#         self.amount = amount
#         BankAccount.balance += amount
#         print(BankAccount.balance)

# account = BankAccount()

# account.deposit(int(input("Enter deposit amount: ")))
# account.withdraw(int(input("Enter withdraw amount: ")))


##3
# class Flying:

#     def __init__(self,make,model,year,max_speed,odometr,is_flying):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.odometr = odometr
#         self.is_flying = False
        
#     def info(self):
#         print(f"{self.make} {self.model} designed in {self.year},maximum speed {self.max_speed} km/h, Odometr indicator is {self.odometr} km.")

#     def land(self):
#         print(f"Самолет {self.make} {self.model} на взлетной полосе.")
#         return True
    
#     def take_off(self):
#         self.is_flying = True
#         print(f"Самолет летит: {self.is_flying}, самолет на земле {Flying.land==False}")

#     def fly(self,distance):
#         self.odometr += distance
#         print(f"Cамолет пролетел {distance} км. Показатель одометра {self.odometr} км")
        
        
    

# plane = Flying("Boing","A380",2008,1050,9000,False)
# plane.info()
# plane.land()
# plane.take_off()
# plane.fly(500)

