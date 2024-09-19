weight = int(input("Enetr your weight (kg)="));
height = float(input("Enetr your height (m)="));
x = weight/float(height*height)
print(x)
if x < 18.5:
    print('Underweight')
if x>=18.5 and x<25:
    print("Normal")
if x >= 25 and x < 30:
   print('Overweight')
if x >= 30:
   print('Obesity')