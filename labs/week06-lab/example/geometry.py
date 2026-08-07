def calculate_rectangle_area(length, width): #สูตร4เหลี่ยม
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

def calculate_sarmlium_area(length, width): #สูตรคำนวน3เหลี่ยม
    """Calculates and displays sarmlium area"""
    area = 0.5 * length * width
    print(f"sarmlium with length {length} and width {width}")
    print(f"Area = {0.5 } × {length} × {width} = {area}")
    print()

print("Calculating sarmlium areas:")
calculate_sarmlium_area(5, 3)
calculate_sarmlium_area(10, 7)

# จากตัวอย่าง ให้สร้าง function สำหรับคำนวนพท.วงกลม

def calculate_circle_area(Radius): #คำนวนพท.วงกลม
    """Calculates and circle sarmlium area"""
    area = 3.14 * (Radius * Radius)
    print(f"circle with length {Radius} ")
    print(f"Area = {3.14} × {Radius} = {area}")
    print()

print("Calculating circle areas:")
calculate_circle_area(244)
calculate_circle_area(1222)

