# demoDict2.py 

phone = {"kim":"1111", "lee":"2222", "park":"3333"}
for key in phone.keys():
    print(key)

for value in phone.values():
    print(value)

print("park" in phone)

print("kang" not in phone)

#참조를 복사 
p = phone 
p["kang"] = "1234"
print(phone)
print(p)
print(id(phone))
print(id(p))


print("---얕은복사---")
a = [1,2,3]
b = a 
a[0] = 38 
print(a)
print(b)
print(id(a), id(b))

print("---깊은복사---")
a = [1,2,3]
b = a[:] 
a[0] = 38 
print(a)
print(b)
print(id(a), id(b))

