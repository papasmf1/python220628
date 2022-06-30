# DemoFile2.py 

#파일에 쓰기
f = open("c:\\work\\demo.txt", "wt")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일을 읽기
f = open("c:\\work\\demo.txt", "rt")
print(f.read())
#처음으로 돌아가기(리셋)
print(f.tell())
f.seek(0)
result = f.readlines()
for item in result:
    print(item, end="")

#다시 처음으로 돌아가기
f.seek(0)
print(f.readline())
print(f.readline())
f.close() 

#기존에 파일이 있으면 첨부하기(a+)
f = open("c:\\work\\demo.txt", "wt")
f.write("새로운 데이터추가\n")
f.close() 


