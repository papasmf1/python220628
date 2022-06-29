#부모 클래스 정의 
class Person:
    #초기화 메서드(생성자)
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    #인스턴스 메서드 
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
    def methodA(self):
        print("methodA실행")
    def methodB(self):
        print("methodB실행")

#자식 클래스 정의 
class Student(Person):
    #상속받은 초기화 메서드를 재정의 
    def __init__(self, name, phoneNumber, subject, studentID):
        #부모클래스의 초기화 메서드를 명시적 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속받은 메서드를 재정의(덮어쓰기, override) 
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
        print("Info(Subject:{0}, StudentID: {1})".format(
            self.subject, self.studentID))

#인스턴스(복사본) 생성 
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "191122")
p.printInfo()
s.printInfo() 
s.methodA()
s.methodB() 


