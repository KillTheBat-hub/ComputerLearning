'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
'''
lis=['adam', 'LISA', 'barT']
#1 recursion ????????
def std(lis):
  lis=['adam', 'LISA', 'barT']
  for i in range(len(lis)):
    lis[i]=lis[i].capitalize()
  return lis 
#2 define function
def cap(x):
  x=x.capitalize()
  return x
std_lis=map(cap,lis)
#3 anonymous function 
std_lis=map(lambda x:x.capitalize(),lis)
print(list(std_lis))


  
