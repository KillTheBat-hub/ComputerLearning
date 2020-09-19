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
