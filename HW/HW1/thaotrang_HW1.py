
#Bai 01:

# Ket qua dau ra la 5 va 6
#Co the thay doi cau lenh vd x+3 va output dau ra la 8
5

x = 5
x + 1

#Bai 02:

# Output dau ra la gia tri ket qua va kieu du lieu moi ket qua bao gom int, float, str
# delimeter * height get an error because python can't multiply sequence by non-int of type 'float'
width = 17
height = 12.0
delimiter = "."

a = width/2
b = width//2
c = width/2.0
d = height/3
e = 1 + 2 * 5
f = (1 + 2) * 5
g = delimiter * 5
h = delimiter * width
#i = delimiter * height

print("width/2:", a,type(a))
print("width//2:", b,type(b))
print("width/2.0:", c,type(c))
print("height/3:", d,type(d))
print("1+2*5:", e,type(e))
print("(1+2)*5:", f,type(f))
print("delimiter*5:", g,type(g))
print("delimiter*width:", h,type(h))
print("delimeter * height get an error because python can't multiply sequence by non-int of type 'float'")

#Bai 0303

# KQ dau ra la 1.04e-33 but hbar = h/2*pi lai khong phai la cong thuc dung, cho nen ket qua output la sai.
# de ouput dung thi sua lai hbar = h/(2*pi) moi co duoc output la 1.05e-34
import math

h = 6.62606876e-34
hbar_fail = h/2 * math.pi
hbar_true = h/(2*math.pi)
print ("hbar fail = ", hbar_fail)
print ("hbar true = ", hbar_true)