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
#？？？解决方法？
# 删除file后，依然能够查看为file命名的变量名和格式
'''
>>> newfile=open("newfile.txt","w")
>>> newfile.close()
>>> os.remove("newfile.txt")
>>> newfile
   <_io.TextIOWrapper name='newfile.txt' mode='w' encoding='cp936'>
'''
#解决方法：file.close()，再次以"r"模式打开，依然是TextIOWrapper但是可以file.read()
# ?????????
