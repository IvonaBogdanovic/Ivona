#Program for calculating BMI
#Author: Ivona Bogdanovic

weight = int(input ("Enter weight: "))
height1 = int(input ("Enter height: "))
height2 = ((height1 / 100))**2
BMI = (weight / height2)
print ("BMI is {}".format (BMI))