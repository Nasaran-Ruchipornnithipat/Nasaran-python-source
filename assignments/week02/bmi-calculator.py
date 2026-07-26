weight = float(input("โปรดใส่น้ำหนัก"))
height = float(input("โปรดใส่ส่วนสูง"))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif bmi < 24.9:
    print("Normal weight")
elif bmi < 29.9:
    print("Overweight") 
else:
    print("Obese")