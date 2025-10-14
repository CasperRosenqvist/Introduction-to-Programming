Children = 0
Hometown = "Turku"
#Lista
TownsInFinland = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

RandomInformation = ["Casper", 22, True, Children, Hometown]

print(TownsInFinland[0])
TownsInFinland.append("Rovaniemi")
print(TownsInFinland)

NumOfTowns = len(TownsInFinland)

print(TownsInFinland[NumOfTowns-1])

Municipality = ["Asikkala", "Hollola", "Karvia", "Kempele"]
Towns = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

MunicipilatyAndTowns = [Municipality, Towns]

print(MunicipilatyAndTowns[1][-2])

Towns.sort()
print(Towns)

Teacher = {
    'name': 'Juha',
    'age': '50',
    'city': 'Lahti'
}

print(Teacher["name"])

Teacher['email']= 'juha.hyytainen@lab.fi'

print(Teacher)

for key in Teacher:
    print(key, end='')
    print(Teacher[key])




for town in Towns: 
    print(f"The town of {town}")
print(f"All of the towns {Towns}")

for i in range(1,10):
    print(i)

for i in range(1,10):
    print(i, end=' ')

for i in range(1,10,3):
    print(i)

Total = 0
for i in range(1,101):
    Total+=i
    print(Total)

print(Total)

for i in range(9):
    if i == 3:
        continue
    print(i)

#while 1<10:
 #   print("Do not try at home")

continueLoop = True
while continueLoop == True:
    if input("Do you want to continue? ") !="yes":
        continueLoop = False