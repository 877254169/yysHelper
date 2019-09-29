from collections import Iterable
from functools import reduce
from types import MethodType
from enum import Enum, unique
from io import StringIO, BytesIO
import os
import pickle
import json
import time, threading

print("hello")
print(2+3)
print(2**10)
# name = input('输入名字：')
# print(name)
print('''aaa
bbb
b''')
print(4>5)
if 3>4 and 5<6:
    print('a')
else:
    print('b')
print(10/3)
print(10//3) #地板除
print(ord('哈')) #获取字符的整数表示
print(chr(123)) #获取编码对应的字符
print('啊哈哈'.encode('utf-8'))
print(b'\xe5\x95\x8a\xe5\x93\x88\xe5\x93\x88'.decode('utf-8'))
print("%s 你好呀，我是%d号" % ('Jam', 8))
print("%d, %02d, %f, %.2f, %%" % (1, 1, 1, 1))
print("%.1f%%" % ((83-73)/73))
ss = 'adsf'
print(len(ss))
arr = ['11', 'sadf', 123]
print(arr)
print(arr[0])
print(arr[-1])
print(len(arr))
arr.append('aaa')
print(arr)
arr.insert(4, 'test')
print(arr)
arr.pop(1)
print(arr)
arr = list(range(5))
print(arr)
for x in arr:
    print(x)
print('END')
i=0
while i<len(arr):
    print(arr[i])
    i = i+1
d = {'key':'key', 'a':1}
print(d)
print('key' in d)
print(d.get("s", -1))
s = set(['a', 'b', 'b', 'c', 2, 4])
print(s)
print(abs(1))
print(abs(-1))
print(max(1, 5, 2, 6, 9, 12, 2, 0, -2, 4))
print(int('123'))
print(int(123.12))
print(float('12.34'))
print(bool(1))
print(hex(123))
a = abs
print(a(-1))
def my_abs(x):
    if not isinstance(x, (int, float)):
       raise TypeError('error type')
    elif x>10:
        return True
    else:
        return False
print(my_abs(9))
def nop():
    print("调用空函数")
    pass
nop()
print(isinstance('a', (int, float)))
# print(my_abs('a'))
#函数返回多个结果，实际上返回的tuple，语法上tuple可以省略括号
def twoRes(x, y):
    return y, x
print(twoRes(1, 2))
#定义默认参数，默认参数必须指向不可变对象
def add_end(l=None):
    if l is None:
        l = []
    l.append('END')
    return l
print(add_end())
print(add_end())
#传入可变参数，在前面加*
def getSum(*numbers):
    sum = 0;
    for i in numbers:
        sum += i
    return sum
print(getSum(1, 2, 3, 4, 5))
a = [1, 2, 3, 4, 5]
print(getSum(*a))
#关键字参数，在内部组成一个dict
def funKey(**kw):
    print(kw)
funKey(name='Sam')
#命名关键字参数，用“*, ”，*后的参数视为命名关键字 -或- 如果已经有一个可变参数，后面跟的命名关键字就不需要特殊分隔符“*”了
#命名关键字参数可以作为默认参数
def funKey2(*, name):
    print(name)
def funKey3(*numbers, name):
    print(numbers, name)
# funKey2(city='changsha') #报错，参数名不符合
funKey2(name='Tom')
funKey3(1, 2, name='Tomi')
#递归函数
def fibonacci(x):
    if x <= 2:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
print(fibonacci(5))
#切片
l = list(range(100))
print(l[0:20]) #取前20个数
print(l[-20:]) #取后20个数
print(l[0:20:2]) #前20个数中以步长2取数
print(l[::17]) #取list中17的倍数
#迭代
d = {'a':1, 'b':2, 'c':3}
for k in d:
    print(k)
for v in d.values():
    print(v)
for k, v in d.items():
    print(k, v)
for ch in 'abc':
    print(ch)
print(isinstance('abc', Iterable)) #判断是否可以迭代
print(isinstance(123, Iterable)) #判断是否可以迭代
for i, v in enumerate(['a', 'b', 'c']):
    print(i, v)
for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)
#列表生成式
l = [x*x for x in range(0, 10)]
print(l)
l = [x for x in range(0, 10) if x % 2 == 0]
print(l)
l = [x+y for x in 'abc' for y in '123']
print(l)
l = [k + str(v) for k, v in d.items()]
print(l)
l = [s.lower() for s in ['HeLlo', 'WorLD']]
print(l)
#生成器
g = (x for x in range(0, 10) if x % 2 == 0)
print(g)
for n in g:
    print(n)
def fib(n):
    i, a, b = 0, 0, 1
    while i < n:
        yield b
        a, b = b, a+b
        i += 1
l = fib(5)
for x in l:
    print(x)
#杨辉三角
def triangles(n):
    i, l = 1, [1]
    while i <= n:
        if i == 1:
            yield l
        elif i == 2:
            l.append(1)
            yield l
        else:
            t = [l[j-1]+l[j] for j in range(1, len(l))]
            t.insert(0, 1)
            t.insert(len(t), 1)
            l = t
            yield l
        i += 1
print('---杨辉三角---')
for i in triangles(5):
    print(i)
print('--------------')
#map
def f(x):
    return x*x
l = map(f, [1, 2, 3, 4, 5])
print(list(l))
l = map(str, [1, 2, 3, 4, 5])
print(list(l))
#reduce
def add(x, y):
    return x*10+y
l = reduce(add, [1, 2, 3, 4, 5])
print(l)
#filter
def is_odd(n):
    return n%2 == 0
l = list(filter(is_odd, range(10)))
print('filter过滤出偶数: ', l)
#----求素数.start
def _odd_iter(): #获取从2开始的自然数，这是一个生成器！
    n=1
    while True:
        n += 1
        yield n
def _is_available(n): #筛选器，选出所有不是n的倍数的数
    return lambda x : x%n != 0
def getPrimes(): #获取素数，这是一个生成器！
    it = _odd_iter()
    while True:
        n = next(it) #返回序列第一个数
        yield n
        it = filter(_is_available(n), it)
for i in getPrimes():
    if i < 20:
        print('素数: ', i)
    else:
        break
#----求素数.end
#sorted
l = [1 , -9, 8, 77,  0, 1.9, -7]
print('数字排序: ', sorted(l))
print('数字排序-按绝对值: ', sorted(l, key=abs))
l = ['df', 'ySy', 'Zafd', 'asdf', 'ard']
print('字符串排序: ', sorted(l))
print('字符串排序-按全小写: ', sorted(l, key=str.lower))
print('字符串排序-按全小写-逆序: ', sorted(l, key=str.lower, reverse=True))
#返回函数
def lazy_sum(*args):
    def sum(): #一个求和函数
        res = 0
        for i in args:
            res += i
        return res
    return sum #注意：返回的函数不要加“()”，不然就返回函数执行后的返回值了
f = lazy_sum(1, 2, 3, 4, 5)
print('未调用函数f: ', f) #返回的函数并不是求和结果，只是单纯的函数
print('调用函数f: ', f()) #调用函数才有结果
#匿名函数 lambda
l = list(map(lambda x : x*x, [1, 2, 3]))
print('利用lambda计算平方: ', l) #lambda也可以作为函数对象返回
#装饰器
#简单装饰器
def call_1(func):
    # @functools.wraps(func) #如果不加这个，hello()会因为被装饰，其‘__name__’属性变为‘wrapple’
    def wrapper(*args, **kw):
        print('function \'%s()\' be called !' % (func.__name__))
        return func(*args, **kw)
    return wrapper
#带参数装饰器
def call_2(msg = ''): #个人觉得默认参数更好，可以省略
    def decorator(func):
        # @functools.wraps(func) #如果不加这个，hello()会因为被装饰，其‘__name__’属性变为‘wrapple’
        def wrapper(*args, **kw):
            print('message: \'%s\', function \'%s()\' be called !' % (msg, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# @call_1
@call_2()
def hello():
    print('hello')
hello()
#类
class User(object):
    #类属性，相当于Java中静态属性
    className = 'User'
    #相当于构造器
    #属性不要单独定义，直接写在__init__()内
    #以两个“__”开头的是私有属性，外部不能直接访问
    #私有属性（比如“__username”）实际上会变成“_User__username”
    def __init__(self, username, passwd):
        self.__username = username
        self.__passwd = passwd
    def showInfo(self):
        print('user info [ username : ', self.__username, ', password : ', self.__passwd, ' ]')
    def get_username(self):
        return self.__username
    def set_username(self, username):
        self.__username = username
    def get_passwd(self):
        return self.__passwd
    def set_passwd(self, passwd):
        self.__passwd = passwd
user = User('root', '123')
user.showInfo()
print('强行访问私有属性(实际上不可取): username: ', user._User__username)
user.set_username('root2')
print('修改值后再次强行访问私有属性(实际上不可取): username: ', user._User__username)
print('user的所有属性和方法: ', dir(user)) #私有属性显示的时候会有所改变
#判断对象是否有某一属性
print('判断user是否有username属性: ', hasattr(user, 'username'))
print('判断user是否有_User__username属性: ', hasattr(user, '_User__username'))
#给对象设置一个属性
setattr(user, 'age', 20)
print('判断user是否有age属性: ', hasattr(user, 'age'))
print('获取user新增的age属性: ', getattr(user, 'age'))
#获取对象的方法
print('获取user的shouInfo方法: ', getattr(user, 'showInfo'))
fn = getattr(user, 'showInfo')
fn()
#获取类属性
print('直接获取User的类属性 User.className: ', User.className)
print('通过对象获取User的类属性 user.className: ', user.className)

class Student(object):
    # __slots__ = ('name', 'set_age', 'age') #限制可以绑定的属性和方法
    pass
s = Student()
s.name = 'Jam'#动态绑定属性
print('动态绑定的属性：name =', s.name)
#给实例绑定一个方法
def set_age(self, age):
    self.age = age
s.set_age = MethodType(set_age, s)
s.set_age(23)
print('动态绑定的方法set age:', s.age)
#给类绑定方法，相当于静态方法
def set_grade(self, grade):
    self.grade = grade
Student.set_grade = MethodType(set_grade, Student)
s1 = Student()
s2 = Student()
s1.set_grade('M')
s2.set_grade('F')
print('给类绑定方法，相当于静态方法，set grade:', s1.grade, s2.grade) #s2覆盖了s1
#给类绑定方法，相当于实例方法
def set_weight(self, weight):
    self.weight = weight
Student.set_weight = set_weight
s3 = Student()
s4 = Student()
s3.set_weight(50)
s4.set_weight(60)
print('给类绑定方法，相当于实例方法，set weight:', s3.weight, s4.weight) #实例方法，s4没有覆盖s3

class Cat(object):
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError('age must be a integer!')
        if age<0 or age>30:
            raise ValueError('range of age is error! must be 0 ~ 30')
        self.__age = age
c = Cat()
c.age = 5 #实际上被转化为 c.set_age(5)
print('用@property标注get、set方法后，获取age:', c.age) #实际上被转换为 c.get_age()
#枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
day1 = Weekday.Mon
print(day1, Weekday['Tue'], Weekday(3))
#文件
with open(r'C:\Users\csj\Desktop\代办.txt', 'r') as f:
    print(f.readline(5))
with open(r'C:\Users\csj\Desktop\代办.txt', 'a') as f:
    f.write('')
#StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print('StirngIO:', f.getvalue())
f = StringIO('hello\nhi\nhah')
while True:
    s = f.readline()
    if s == '':
        break
    print('read StringIO:', s.strip())
#操作文件和目录
print('操作系统类型:', os.name) #如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# print('详细系统信息:', os.uname()) #windows系统不支持这个函数
print('所有环境变量:', os.environ)
print('PATH环境变量:', os.environ.get('PATH'))
print('当前目前绝对路径:', os.path.abspath('.'))
print('创建目录前，先表示该目录:', os.path.join(r'C:\Users\csj\Desktop', 'py_test'))
# os.mkdir(r'C:\Users\csj\Desktop\py_test') #创建目录
# os.rmdir(r'C:\Users\csj\Desktop\py_test') #删除目录
# os.mknod(r'C:\Users\csj\Desktop\py_test.txt') #创建空文件
print('拆分目录，自动把最后一个提出来:', os.path.split(r'C:\Users\csj\Desktop\py_test.txt'))
print('得到文件扩展名:', os.path.splitext(r'C:\Users\csj\Desktop\py_test.txt'))
print('当前目录下所有文件:', [x for x in os.listdir('.') if not os.path.isdir(x)])
print('当前目录下所有py文件:', [x for x in os.listdir('.') if os.path.splitext(x)[1] == '.py'])
#序列化
d = {'name':'Jam', 'age':'23', 'grade':'M'}
print('序列化后:', pickle.dumps(d))
with open(r'C:\Users\csj\Desktop\pytest.txt', 'wb') as f:
    pickle.dump(d, f)
    print('直接序列化后写进文件')
with open(r'C:\Users\csj\Desktop\pytest.txt', 'rb') as f:
    d = pickle.load(f)
    print('从文件读序列化后的对象:', d)
#json
d = {'name':'Jam', 'age':'23', 'grade':'M'}
print('python转json:', json.dumps(d))
with open(r'C:\Users\csj\Desktop\pytest.txt', 'w') as f: #转成json会变成string形式，所以直接用“w”
    json.dump(d, f)
    print('把对象序列化为json写进文件')
with open(r'C:\Users\csj\Desktop\pytest.txt', 'r') as f:
    d = json.load(f)
    print('从文件读取转为json的对象:', d)
u = User('root', 'root')
print('把class转为json:', json.dumps(u, default=lambda obj:obj.__dict__))
#线程
def MyThread():
    print('线程 %s 正在运行' % (threading.current_thread().name))
    print('线程 %s 结束' % (threading.current_thread().name))
print('线程 %s 正在运行' % (threading.current_thread().name))
t = threading.Thread(target=MyThread, name='MyThread')
t.start()
print('线程 %s 结束' % (threading.current_thread().name))


