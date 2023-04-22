# 1 (15 балів). Розробіть клас Fraq, що представляє звичайний дріб виду a/b, a - чисельник, b - знаменник.
# - клас повинен мати три конструктори: Fraq(), який створює дріб виду 0/1, Fraq(n,d), який створює дріб виду n/d, Fraq(f), який створює копію дробу f (змінна, що має тип Fraq);
# - додайте у клас приватний метод reduct(), який повинен скорочувати дріб. Наприклад, якщо є дріб 2/6, то метод повинен його привести до виду 1/3. Метод скорочує дріб "на місці", тобто, міняє поля поточного об'єкта, а не створює новий об'єкт;
# - якщо пишете на Python: додайте у клас методи для виконання операцій "+" (__add__), "-" (__sub__), "*", "/": додавання, віднімання, множення, ділення дробів. У результаті роботи методів повинен створюватись новий об'єкт типу Fraq, у якому записано результат відповідної операції. Наприклад, виклик f3 = f1 + f2 повинен створювати новий об'єкт, що є результатом суми дробів f1 та f2. Передбачте скорочення дробу перед поверненням результату. Приклад: f1 = 3/8, f2 = 1/8, f1 + f2 = 4/8, але після скорочення отримається 1/2, що й буде повернуто у вигляді результату виклику так, що отримається f3 = 1/2;
# - у основній програмі реалізуйте демонстрацію усіх конструкторів та методів.

# 2 (5 балів). Додайте у клас, розроблений вище, операції порівняння (типу __lt__, __gt__ та інші) та перетворення об'єкта у рядок (__repr__, __str__) для мови Python, або ж методи equals() та toString() для мови Java. Продемонструйте роботу методів.

import math,numbers,operator
class Fraq:

    def __init__(self, numerator=0, denominator=None):
        
        self.numerator = numerator
        self.denominator = denominator

        if(numerator == None):
            self.numerator = 0
            self.denominator = 1
        if(isinstance(numerator, numbers.Rational) and denominator==None):
            self.numerator = numerator.numerator
            self.denominator = numerator.denominator

        if(denominator!=None and self.denominator>0):
            self.__reduct(self.numerator,self.denominator)
    def __reduct(self,a, b):
        divisor = self.gcd(a, b)
        self.numerator =  int(self.numerator/divisor)
        self.denominator =  int(self.denominator/divisor)

    def __add__(self, val2):
        na, da = self.numerator, self.denominator
        nb, db = val2.numerator, val2.denominator
        g = math.gcd(da, db)
        if g == 1:
            return Fraq(na * db + da * nb, da * db)
        s = da // g
        t = na * (db // g) + nb * s
        g2 = math.gcd(t, g)
        if g2 == 1:
            return Fraq(t, s * db)
        return Fraq(t, s * db)

    def __sub__(self, val2):
        na, da = self.numerator, self.denominator
        nb, db = val2.numerator, val2.denominator
        g = math.gcd(da, db)
        if g == 1:
            return Fraq(na * db - da * nb, da * db)
        s = da // g
        t = na * (db // g) - nb * s
        g2 = math.gcd(t, g)
        if g2 == 1:
            return Fraq(t, s * db, _normalize=False)
        return Fraq(t // g2, s * (db // g2))

    def __mul__(self, val2):
        na, da = self.numerator, self.denominator
        nb, db = val2.numerator, val2.denominator
        g1 = math.gcd(na, db)
        if g1 > 1:
            na //= g1
            db //= g1
        g2 = math.gcd(nb, da)
        if g2 > 1:
            nb //= g2
            da //= g2
        return Fraq(na * nb, db * da)

    def __truediv__(self, val2):
        na, da = self.numerator, self.denominator
        nb, db = val2.numerator, val2.denominator
        g1 = math.gcd(na, nb)
        if g1 > 1:
            na //= g1
            nb //= g1
        g2 = math.gcd(db, da)
        if g2 > 1:
            da //= g2
            db //= g2
        n, d = na * db, nb * da
        if d < 0:
            n, d = -n, -d
        return Fraq(n, d)

    def __str__(self):
        """str(self)"""
        if (self.denominator == 1 or self.denominator == None):
            return str(self.numerator)
        else:
            return '%s/%s' % (self.numerator, self.denominator)

    def __repr__(self):
        """repr(self)"""
        return '%s(%s, %s)' % (self.__class__.__name__,
                               self.numerator, self.denominator)
    def helper(self, other, op):
        # convert other to a Rational instance where reasonable.
        if isinstance(other, numbers.Rational):
            return op(self._numerator * other.denominator,
                      self._denominator * other.numerator)
        if isinstance(other, float):
            if math.isnan(other) or math.isinf(other):
                return op(0.0, other)
            else:
                return op(self, self.from_float(other))
        else:
            return NotImplemented

    def __lt__(a, b):
        """a < b"""
        return a.helper(b, operator.lt)

    def __gt__(a, b):
        """a > b"""
        return a.helper(b, operator.gt)

    def __le__(a, b):
        """a <= b"""
        return a.helper(b, operator.le)

    def __ge__(a, b):
        """a >= b"""
        return a.helper(b, operator.ge)

    def gcd(self,a,b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a == b:
            return a
        if a > b:
            return self.gcd(a-b, b)
        return self.gcd(a, b-a)

f1 =  Fraq(3,8)
f2 =  Fraq(1,8)
sumOf = f1 + f2
print("3/8 + 1/8 =" , sumOf)
print(type(sumOf),'check typeof , should be Fraq')

mult = sumOf * sumOf
print(mult,"mult")

sub = f1 - f2
print(sub,"sub1")

f4 =  Fraq(1,4)
f5 =  Fraq(1,2)
divy = f4/f5
print(divy,"div")

f3 =  Fraq(2,8)
print(f3)

f4 =  Fraq(f3)
print(f4)
print(repr(f4))
