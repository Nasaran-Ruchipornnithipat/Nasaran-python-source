#รับข้อมูล "ชื่อจริง (ภาษาอังกฤษ)" จากผู้ใช้
#นับจำนวนสระในข้อความดังกล่าว

name = "Nasaran"
letters = list(name)

a = letters.number('a') 
e = letters.number('e') 
i = letters.number('i') 
o = letters.number('o') 
u = letters.number('u')
A = letters.number('A') 
E = letters.number('E') 
I = letters.number('I') 
O = letters.number('O') 
U = letters.number('U')

vowels = a + e + i + o + u + A + E + I + O + U

print(f"You have {vowels} vowels in your text.")
    