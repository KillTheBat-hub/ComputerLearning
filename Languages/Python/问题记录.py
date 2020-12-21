#compiler编译器
#问题：编译器的中间语言会存储到某处以便以后直接调用吗？？？？？？？？？



#for循环 for i in xxx: 如何正确定义
lis=[1,2,3,4]
#正确示例
for i in range(len(lis)):
#错误示例1
for i in lis[i]: #
#错误示例2
for i in len(lis): #
#问题：解释上述错误的问题；for循环应该如何正确定义
#解决：1.UnboundLocalError: local variable 'i' referenced before assignment，想要直接声明i的位置为lis[i]
#问题在于下一语句lis[i]=lis[i].....已经指明了具体在哪里操作，这样写不但不合规而且无意义。
#2.TypeError: 'int' object is not iterable，int类型是不能直接迭代的。
#for i in xxx: 首先xxx必须是个可迭代对象，查询是否是可迭代对象from collections import Iterable, isinstance(str,Interable)
#https://blog.csdn.net/loner_fang/article/details/80636805



# try...exception..finally，与python的错误判断顺序
try:
    num1="1"
    print(num1/0)
except:
    print(num2)
finally:
    print(num3)  
#注意报错顺序：TypeError, num2 not defined, num3 not defined
try:
    num1="1"
    print(num1/0)
except:
    print(num2)
finally:
    print("what ever print finally")  
#先print finally，然后报错：TypeError, num2 not defined


#open()不存在的文件，并read()
'''
open一个不存在的file，会在当前文件夹创造这个file，删除file后，依然能够查看为file命名的变量名和格式
'''
newfile=open("newfile.txt","w")
newfile.close()
os.remove("newfile.txt")
newfile   #<_io.TextIOWrapper name='newfile.txt' mode='w' encoding='cp936'>
#问题：新创建TXT，对象格式是TextIOWrapper而不是BufferRandom,可以write、close但是无法read
#解决：write模式下没有read权限。file.close()，再次以"w+"或"r"模式打开，依然是TextIOWrapper但是可以file.read()


#file.read()
'''
file.read()只能用一次，因为相当于光标会停到文档最后
'''
#问题：file.close()后再次open，file.read()依然为空。解决方法有：file.seek(0)回到开头，试过后无效
#解决：每次以"w"模式打开，file都会清空。使用"a"append模式，此时file.write()会在文档末尾添加新内容。


#print和None的用法
n=None
n
n=None
print(n)
#问题：print的何种设计使它能打印“无值”的None
#解决：????????????


#如何让dict的一个值为raise Error
dic[2]=raise ValueError("value error")
#???????????
dic[2]=ValueError("value error")
#dic[2]并不会显示为ValueError:value error。但是它的type是<class ValueError>
#????????????


#for循环把lis中的每一个元素变成tuple格式
'''
for循环中的前后两个参数的指定规则：for x in ...,就是把...中的所有元素一一代入x
'''
lis=[1,2,3,[4,5]]
#1
for i in lis:
  lis[i]=tuple(lis[i])
#2
for i in lis:
  i=str(i)
#3
for i in len(lis):
  lis[i]=tuple(lis[i])
#4
for i in range(len(lis)):
  lis[i]=tuple(lis[i])
#问题：以上几段分别为什么错了？
### 解决：已实现变为str格式：
list=[1,2,3,[4,5]]
for i in range(len(list)):
  list[i]=tuple(list[i])

'''
首先，int是不能直接转变成tuple的？？？？？？？？？？？？？why?
但是int可以变为str，str可以变为tuple。
其他错误：
1-i既指代lis中的元素，又指代元素的位数，混淆了
2-??????????????   https://www.cnblogs.com/chenhuabin/p/11288797.html  for循环迭代器可以迭代list但不能迭代int
'''

#tuple与list索引
tu=[1,2,3][3,2,1]
'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not tuple'''
#问题：？？？？？？？？


#类型转换后使用function
lis=["hello","all","you","guys"]
print(str(lis).upper())
print(str(lis)+"ohhhhhhh")
print((str(lis)+"ohhhhhhh").upper())
#list变str常见办法是",".join(lis)，变为str type，然后通过lis.split()变回
lis=",".join(lis)
print(lis.split())
print(lis.split(","))


#文件打开与内容操作
def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

filename = input("Enter a filename: ")
with open(filename) as f:
  text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))
#问题：重复的字母重复执行
#解决：？？？？？？？？？？？？？？？


#anoymous functions:lambda
#python吸取了部分函数式编程的思想，保留了lambda函数作为内置函数，它可像函数式编程一样作为argument进入迭代
type((lambda x:x+1)(2)) #<class 'int'>
type(lambda x:x+1)  #<class 'function'>
type(lambda x:x+1, 2)  #<class 'tuple'>
#问题：lambda函数在python中是如何认定的？
#解决：？？？？？？？？？？？？？？？？？？？？？


#decorator
'''
装饰器func的作用就是定义一个func并return，被嵌套的func是另一个已定义的func的皮套，目的是不改变原定义的前提下增强其功能
标准格式：
def deco(func):
  def addpower():
    ..........
    func()
    ..........
  return addpower()
'''
def phello():
	print("hello world")
def addpower(func):  #简单问题的简单格式
	print("=============")
	func()
	print("=============")
dcrt_phello(phello)

def decr(func):  #标准格式
	def addpower():
		print("=============")
		func()
		print("=============")
	return addpower


#问题：func的argument和return问题
#1.return的时候到底发生了什么？什么时候必须return，什么时候可以不return？
#2.为什么外层函数的argument是func不是func()？--函数argument允许种类问题
#解答：?????????????????????

#isinstance,OOP与python内置数据类型
#在OOP,objection-oriented programming, 出现instance实例的概念，它是根据“模板”Class创造出来的具体对象
class Cat():
	legs=4
	def __init__(self,color,name):
		self.name=name
		self.color=color
	def voice(self):
		print("meow~ from "+ self.name)

lily=Cat("pink","Lily")
print(lily.color)
print(lily.voice())
print(lily.legs)
print(Cat.legs)  #class attributes
#lily就是instance, 根据class Cat创造出来
isinstance(str,Interable)
#问题：python内置函数也都是instance，即OOP方式创造和保存的吗？？？？？？？？？？？
#https://www.runoob.com/python/python-func-isinstance.html


#class MagicMethod，self和other
#magic method
class Vector2D():
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __add__(self,other):
		return Vector2D(self.x+other.x,self.y+other.y)


vector1=Vector2D(1,2)
vector2=Vector2D(2,0)
result=vector1+vector2
result
'''
问题：1.magicmethod干什么用，python的基础函数？ 2.class中的magicmethod干什么用，修改python已经写好的基础函数吗？
3.self和other为什么要这么定义，用self传入初始值，然后用other区分与self做迭代？本质是next()?
解决：1.magic method即规则，定义了+-*/和print()等基础函数。它的标志为前后双下划线。
2.class中的magic method有很多。1)数据传输，__init__和__new__。__init__的作用是instantiation创建实例，将具体的value传入class模板；__new__。
  2)重新定义规则，使得class中具有独特的运算规则，比如__add__定义加法,__getitem__定义根据index索引,__gt__定义大于等于,__repr__指定print的内容和格式
3.self
  '''



#private method
class Queue:
	def __init__(self,cont):
		self._hiddenlist=list(cont)  #self与cont的关系也可通过函数建立；那么x=y实际上是不是也是一种函数？
	def push(self,value):
		return self._hiddenlist.insert(0,value)
	def pop(self):
		return self._hiddenlist.pop(-2)
	def __repr__(self):   #指定print()的内容和格式，必须有return否则函数没有完成，不用return用print是不行的
		return "Queue({})".format(self._hiddenlist)  #这里甚至不用传入cont，为什么呢？直接指向了ID吗？
queue1=Queue(([0,0,0],[1,1,1]))  #这里的错误：1.Queue([],[])  2.Queue([][])，似乎看到括号首先按tuple处理 3.2的基础上再加一层括号，Queue(([][]))
print(queue1)
queue1.pop()
print(queue1)	
#每个method里的self指的应该是class里这同一个self值吧？


#class methods: instance method, class method, static method
class Example:
	def __init__(self):
		pass 
	def instance_met(self):
		'''实例方法，至少有一个self参数'''
		print("intance method")
	def class_met(cls):
		'''类方法，至少有一个cls参数'''
		print("class method")
	def static_met():
		'''无默认参数'''
		print("static method")   



#输入长宽高，返回体积; 使用class method改写
class Volume:
	def __init__(self,length,width,height):
		self.length=length
		self.width=width
		self.height=height
	def volume_caculate(self):
		return self.length * self.width * self.height
	@classmethod #decorator
	def vlm(cls,side_length):
		return cls(side_length,side_length,side_length)
		#class method也像decorator
	@classmethod
	def sayhi(cls):
		return "Hi!"

v=Volume.vlm(5)
print(v.volume_caculate())
print(Volume.sayhi())


#使用static method判断pizza馅料
class Pizza:
	def __init__(self,topping):
		self.topping=topping
	@staticmethod
	def validate_toppings(topping):
		if topping=="pineapple":
			raise ValueError("there is no pineapples!")
		else:
			return True

piz=["cheese","onions","spam"]
if all(Pizza.validate_toppings(i) for i in ingredients):   #all(),如果函数中的项全部为True则返回True，否则返回False
	piz=Pizza(piz)
'''
#以另一种方式改写
def test(lis):
	empty=[]
	for i in lis:
		empty.append(Pizza.is_toppings(i))
	if False not in empty:
		lis=Pizza(lis)
		return lis
'''
	@property  #用property实现对于instance read-only
	def is_pineapple_allowed(self):
		return False
pizza=Pizza(["apple","onions"])	
pizza.is_pineapple_allowed = True
Pizza.is_pineapple_allowed = True


#前后下划线https://www.runoob.com/w3cnote/python-5-underline.html  还是不太明白，具体怎么用
#


