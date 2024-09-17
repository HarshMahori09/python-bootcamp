Age = int(input("Enter the Age="))
gender = input("Enter the Gender=")
if (Age > 17 and gender=="female"):
    print("Your are eligible for Government Job")
elif (Age > 17 and gender=="male"):
    print("Your are eligible for privater Job")
else :
    print("Not Eligible")   