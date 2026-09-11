import math

class Triangle:
    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_a(self):
        return self.__a
    def get_b(self):
            return self.__b
    def get_c(self):
            return self.__c

    def set_a(self, newA):
        self.__a = newA
    def set_b(self, newB):
        self.__b = newB
    def set_c(self, newC):
        self.__c = newC
        
    def is_triangle(self):
        return (self.__a>0 and self.__b>0 and self.__c>0
                and self.__a + self.__b > self.__c
                and self.__a + self.__c > self.__b
                and self.__b + self.__c > self.__a)
        
    def perimeter(self):
        if not self.is_triangle():
            print('Ba so da cho khong la 3 canh cua tan giac!')
            return None
        return self.__a + self.__b + self.__c
    
    def area(self):
        if not self.is_triangle():
            print('Ba so da cho khong la 3 canh cua tan giac!')
            return None
        p = self.perimeter()/2
        return math.sqrt(p*(p - self.__a)*(p - self.__b)*(p - self.__c))
    
    def display(self):
        print('Thong tin ve tam giac: ')
        print('Ba canh cuar no la: ')
        print(f'a = {self.__a:.2f}, b = {self.__b:.2f}, c = {self.__c:.2f}')
        if(self.is_triangle()):
            print(f'{self.__a:.2f}, {self.__b:.2f}, {self.__c:.2f} la 3 canh cua tam giac')
            print(f'Chu vi la: {self.perimeter():.2f}')
            print(f'Dien tich la: {self.area():.2f}')
        else:
            print(f'{self.__a:.2f}. {self.__b:.2f}, {self.__c:.2f} KHONG la 3 canh cua tam giac')
            
#Tao tam giac
a = float(input('cho biet a: '))
b = float(input('cho biet b: '))
c = float(input('cho biet c: '))

t = Triangle(a,b,c)
print('KET QUA LA')
t.display()