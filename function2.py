# function2.py 
#튜플로 리턴 
def swap(x,y):
    return y,x 

#호출
result = swap(5,6)
print(result)

#교집합 문자를 리턴
def intersect(prelist, postlist):
    #교집합 문자를 모아들 지역변수(함수 내부 변수)
    result = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        #특정 글자가 postlist에도 있고 result에 없으면 
        if x in postlist and x not in result:
            result.append(x)
    return result 

#호출
#중단점(Break Point)
print(intersect("HAM","SPAM"))