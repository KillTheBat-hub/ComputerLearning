# try...exception..finally
'''  
？？？？？？？？
python的错误判断顺序很有意思
'''
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

#open file
#open一个不存在的file，会在当前文件夹创造这个file，但格式是TextIOWrapper而不是BufferRandom,可以write、close但是无法read
# 删除file后，依然能够查看为file命名的变量名和格式
'''
>>> newfile=open("newfile.txt","w")
>>> newfile.close()
>>> os.remove("newfile.txt")
>>> newfile
   <_io.TextIOWrapper name='newfile.txt' mode='w' encoding='cp936'>
'''
#解决方法：file.close()，再次以"w+"或"r"模式打开，依然是TextIOWrapper但是可以file.read()
#write模式下没有read权限


#file.read()
#file.read()只能用一次，因为相当于光标会停到文档最后
#file.close()后再次open，file.read()依然为空。解决方法有：file.seek(0)回到开头，试过后无效
#原因：每次以"w"模式打开，file都会清空。使用"a"append模式，此时file.write()会在文档末尾添加新内容。


#print和None的用法
n=None
n
n=None
print(n)
#????????????

#如何让dict的一个值为raise Error
dic[2]=raise ValueError("value error")
#???????????
dic[2]=ValueError("value error")
#dic[2]并不会显示为ValueError:value error。但是它的type是<class ValueError>
#????????????


#for iteration
#把lis中的每一个元素变成tuple格式
lis=[1,2,3,[4,5]]
#1
for i in lis:
  lis[i]=tuple(lis[i])
#2
for i in len(lis):
  lis[i]=tuple(lis[i])
#3
for i in range(len(lis)):
  lis[i]=tuple(lis[i])

#?????????????????

#类型转换后使用function
lis=["hello","all","you","guys"]
print(str(lis).upper())
print(str(lis)+"ohhhhhhh")
print((str(lis)+"ohhhhhhh").upper())
#list变str常见办法是",".join(lis)，变为str type，然后通过lis.split()变回
lis=",".join(lis)
print(lis.split())
print(lis.split(","))


