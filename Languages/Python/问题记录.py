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
#python吸取了部分函数式编程的思想，保留了单变量lambda函数
type((lambda x:x+1)(2)) #<class 'int'>
type(lambda x:x+1)  #<class 'function'>
type(lambda x:x+1, 2)  #<class 'tuple'>
#问题：lambda函数在python中是如何认定的？
#解决：？？？？？？？？？？？？？？？？？？？？？
