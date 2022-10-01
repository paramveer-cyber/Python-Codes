print("Hey! This is a simple BMI calulator!")
print("Please enter the following values in kg/cm")

def bmi(weight, height):
    bmi = "{:.2f}".format(weight/((height/100)**2))
    return bmi

weight = float(input("Please enter you weight(kg): "))
height = float(input("Please enter you height(cm): "))
print(bmi(weight, height))
