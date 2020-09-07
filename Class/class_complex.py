class complex:
    def __init__(self,x,y):
        self._real = x
        self._imag = y
        
    def __repr__(self):
        return str(float(self._real)) + '+' + 'j*' + str(float(self._imag))
    
    def __add__(self,other):
        result = complex(0,0)
        result._real = self._real + other._real
        result._imag = self._imag + other._imag
        return result._real,result._imag
    
    def __mul__(self,other):
        result = complex(0,0)
        result._real = (self._real * other._real)-(self._imag * other._imag)
        result._imag = (self._real * other._imag)+(other._real * self._imag)
        return result._real,result._imag
    
    def __abs__(self):
        return (self._real**2 + self._imag**2)**0.5
    
a = complex(0,1)
b = complex(0,1)
print(a+b)
print(a*b)
repr(a)
