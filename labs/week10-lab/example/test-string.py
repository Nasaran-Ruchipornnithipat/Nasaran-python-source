# เขียนโปรแกรม นับจำนวนอักขระที่สนใจในข้อความที่กำหนดโดยผู้ใช้
# 1. รับข้อความที่กำหนดให้จากผู้ใช้ (text)
# 2. รับอักขระที่สนใจจากผู้ใช้ (char)
# 3. แสดงผลการนับอักขระที่สนใจในข้อความออกทางหน้าจอ
 
# ตัวอย่างหน้าจอ
# Insert the text: Kasetsart Sriracha
# Charcter to find: r
# 3 letters 'r' found in 'Kasetsart Sriracha'
 
print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert the text: ")
char = input("Character to find ")
for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters '{char}' found in '{text}'")



# เขียนโปรเเกรม ตรวจสอบความเเข็งเเรงของ password
# password ที่เเข็งเเรงคือ ยาวมากกว่า 8 ตัว เเละผสมกันระหว่างตัวเลข ตัวอักษร เเละอักขระพิเศษ

# ตัวอย่างหน้าจอ

# Insert yous password: Test123
# your password is not strong;

# Insert yous password: Test1234;
# your password is strong

password = input("โปรดใส่รหัสผ่าน:")
lenght = len(password)
check = password.isalnum()

if lenght > 8 and check == False:   
    print("your password is  strong")
else:
    print("your password if not strong")
