# 사칙연산 클래스

'''
a = FourCal()

a.setdata(4,2)

a.add() >>> 6
a.mul() >>> 8
a.sub() >>> 2
a.div() >>> 2


'''

class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
        
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
    
        
    

a = FourCal()
# print(type(a))

a.setdata(4,2)

print(a.first)
print(a.second)

b = FourCal()
b.setdata(3,5)
print(b.first)
print(b.second)

print("a.add() :" , a.add)
print("a.mul() :" , a.mul)
print("a.sub() :" , a.sub)
print("a.div() :" , a.div)

# d = FourCal(4,2)
# print(d.add())
# print(d.div())

print("------클래스 상속 ------")
print()

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
        
    # div 메서드 오버라이딩
    def div(self):
        if self.second == 0:
            return 0

print(a.add())
print(a.div())

a = MoreFourCal(4,0)

print(b.div())

print(MoreFourCal.third)
print(a.third)
print(b.third)





