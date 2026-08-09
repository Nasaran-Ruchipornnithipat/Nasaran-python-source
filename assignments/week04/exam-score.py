score_student = [60, 40, 74, 68, 81]

for i, score in enumerate(score_student):
    if score >= 50:
        result = "ผ่าน"
    else:
        result = "ไม่ผ่าน"
    print(f"Student {i + 1}: {score} -> {result}")