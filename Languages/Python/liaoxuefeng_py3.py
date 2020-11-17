'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
'''
lis1=['adam', 'LISA', 'barT']
#1 recursion ????????
def std(lis):
  for i in range(len(lis)):
    lis[i]=lis[i].capitalize()
  #print(lis)
  return lis 
print(upper(lis1))  
#2 define function
def cap(x):
  x=x.capitalize()
  return x
std_lis=map(cap,lis1)
#3 anonymous function 
std_lis=map(lambda x:x.capitalize(),lis1)
print(list(std_lis1))   #注意std_lis1的type是map object，打印要先转化成list或者其他能直接打印的类型



  
