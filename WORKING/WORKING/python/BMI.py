weight = int(input())
height = float(input())

bmi = weight/height**2
#print(bmi)


Underweight = bmi < float(18.5)
Normal = bmi >= 18.5 and bmi < 25
Overweight = bmi >= 25 and bmi < 30
Obesity = bmi >= 30 


if bmi == Underweight:
    print('Underweight')
if bmi == Normal:
    print('Normal')
if bmi == Normal:
    print('overweight')
if bmi >= 30:
    print('Obesity')



# # sampel input
# # 85
# # 1.9 float height in meter

# # answer output should be  = Normal


# weight = int(input())
# height = float(input())

# if weight/height**2 < 18.5:
#     print("Underweight")

# if weight/height**2 >= 18.5 and weight/height**2 < 25:
#     print("Normal")

# if weight/height**2 >= 25 and weight/height**2 < 30:
#     print("Overweight")

# if weight/height**2 >= 30:
#     print("Obesity")