manu = input("ต้องการแปลงจากUSDเป็นTHBกด1,ต้องการแ/ปลงจากTHBเป็นUSDกด2")
Currency = float(input("กรุณากรอกจำนวนเงินที่ต้องการเเปลง: "))
if manu == "1":
    result = Currency * 34.5
    print(f"จำนวนเงินที่เเปลงจาก USD เป็น THB คือ: {result} บาท")
elif manu == "2":
    result = Currency / 34.5
    print(f"จำนวนเงินที่เเปลงจาก THB เป็น USD คือ: {result} USD")
else:
    print("คุณใส่ตัวเลือกไม่ถูกต้อง")