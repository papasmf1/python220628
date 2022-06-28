# function3.py 
#함수 정의
from imghdr import tests


x = 2 
def func1(a):
    return a+x 

#호출
print(func1(1))

#함수 정의
def func2(a):
    x = 5
    return a+x 

#함수 호출
print(func2(1))

print("---불변형식---")
a = 1.2 
print(id(a))
a = 2.3 
print(id(a))

print("---가변형식---")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))


#불변형식을 함수 내부에서 읽기 + 쓰기 
#전역변수
g = 1 
def testScope(a):
    #global g 
    #지역변수 
    g = 2 
    return g+a 

#호출
print(testScope(1))
print("전역 변수 g:", g)




