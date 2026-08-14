"""
เบียน function ชื่อ convart_currency(value, currency)
ทีทำหน้าที่ในการเเปลงสกุลเงิน
THB<->USD กำหนดให้ 1 usd = 33 THB
ทั้งนี้ให้ function ดังกล่าว รับข้อมูล จำนวนเงินที่ต้องการเเปลง เเละสกุลเงินปลายทาง

ตัวอย่างเรียกใช้
convert_currency(100, "USD")
convert_currency(100, "THB")
ตัวอย่างหน้าจอ
100THB = 3.33 USD
100USD = 3333 THB
"""
def convert_currency(value, currency):
    if currency  == "USD":
        print(f"{value} THB = {value / 33.0} USD")
    elif currency  == "THB":
        print(f"{value} USD = {value * 33.0} THB")
    else:
        print("ไม่เข้าเงื่อนใช่")

convert_currency(100, "USD")
convert_currency(100, "THB")

def convert_currency(value, currency):
    result = 0
    if currency  == "USD":
        result = value / 33.0
        print(f"{value} THB = {result} USD")
    elif currency  == "THB":
        result = value / 33.0
        print(f"{value} THB = {result} USD")

convert_currency(100, "USD")
convert_currency(100, "THB")