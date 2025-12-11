
#import pandas as pd
#import matplotlib.pyplot as plt

#data = {
#    'Temperature': [23, 22, 12, 32, 14, 20, 22, 22, 22, 21],
#    'Movement': [1, 0, 1, 1, 1, 1, 0, 0, 0, 1]
#}

#df = pd.DataFrame(data)
#print(df)

#plt.figure(figsize=(10,5))
#plt.plot(df['Temperature'], label = "Temperature")
#plt.plot(df['Movement'], label = "Movement")
#plt.xlabel('Time')
#plt.ylabel('Value')
#plt.legend()
#plt.show()
##################################

#import turtle


#from turtle import Screen
#turtle_screen = Screen()

#from turtle import *
#turtle_screen = Screen()

#sipi = turtle.Turtle() #Luo uusi kilpikonna olio eli Turtle instanssi
#sipi.shape("turtle") # Metodi
#sipi.color("green") # Metodi
#sipi.forward(100) # Metodi

#turtle_screen = turtle.Screen() # Luo uusi ikkuna olio eli instanssi
#turtle_screen.exitonclick() # Metodi

####################################################

#class LABStudent:
#    name: str # attribute
#    age: int #attribute
#    major: str #attribute

#    def introduce(self): #Method
#        return f"Hi, I'm {self.name}, {self.age} years old, majoring in {self.major}."
#    
#    def study(self): # Method
#        return f"{self.name} is studying {self.major}"

#John = LABStudent()
#John.name = "John"
#John.age = 32
#John.major = "computer science"


#Jane = LABStudent()
#Jane.name = "Jane"
#Jane.age = 25
#Jane.major = "physics"

#print(John.introduce())
#print(Jane.study())

###########################


from lab_student import LABStudent

John = LABStudent("John", 32, "Computer Science")
Jane = LABStudent("Jane", 25, "Physics")

print(John.introduce())
print(Jane.study())
