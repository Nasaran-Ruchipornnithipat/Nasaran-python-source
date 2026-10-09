INITIAL_BALANCE = 1000


def deposit(money):
    """จำลองการฝากเงินเข้าบัญชี (ยอดเริ่มต้น 1,000 บาท)"""
    try:
        # แปลงข้อความเป็นตัวเลข ถ้าแปลงไม่ได้ (เช่น abc) จะเกิด ValueError
        try:
            amount = float(money)
        except ValueError:
            raise ValueError("กรุณากรอกจำนวนเงินเป็นตัวเลขเท่านั้น")

        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
    except ValueError as e:
        print(f"เกิดข้อผิดพลาด: {e}")
    else:
        new_balance = INITIAL_BALANCE + amount
        print("ฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {new_balance:.2f} บาท")
    finally:
        print("สิ้นสุดรายการฝากเงิน")


if __name__ == "__main__":
    print(f"ยอดเงินเริ่มต้น: {INITIAL_BALANCE} บาท")
    money = input("กรอกจำนวนเงินที่ต้องการฝาก: ")
    print()
    deposit(money)