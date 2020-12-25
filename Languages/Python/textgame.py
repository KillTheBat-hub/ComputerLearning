#text-based adventure game

#定义输入交互函数，包括动作和动作对象
def get_command():
	'''
	输入信息，在verb_dict中查找对应的动作
	command:输入的信息
	verb_search:verb_dict key
	verb:verb_dict value
	'''
	command=input(": ").split()
	verb_search=command[0]
	if verb_search in verb_dict:
		verb=verb_dict[verb_search]
	else:
		print("unkown verb {}".format(verb_search))
		return
	if len(command)>=2:
		noun=command[1]
		print(verb(noun))
	else:
		print("what's the object of your action?")
	
def say(noun):
	return "you say {}".format(noun)

#定义GameObject类，并定义一个具体的子类Goblin
class GameObjects:
	class_name=""
	desc=""
	objects={}
	def __init__(self,name):
		self.name=name
		GameObjects.objects[self.class_name]=self   #子类实例交互，每次定义新的实例即传入
	def get_desc(self):
		return self.class_name+"\n"+self.desc

class Goblin(GameObjects):
	def __init__(self,name):
		self.class_name="goblin"   #为什么转成实例属性了？实例属性可以与类属性相互转换？--因为要与实例的状态交互，改成实例属性--实例属性和类属性？--不需要交互的直接改成类属性？
		self._desc="A fool and ugly creature"
		self.health=3
		super().__init__(name)   #为什么没有self了？为什么放最后？--前面class name没定义，无法传入objects --继承__init__的意义是不用再一次一次地敲，特别参数多的时候，直接命令向上寻找重复地拿来用，有需要再另添加新的即可

	@property  #将方法变成属性
	def desc(self):
		'''控制health和desc'''
		if self.health>=3:
			return self._desc
		elif self.health==2:
			return "it has a wound on his knee"
		elif self.health==1:
			return "one of its arm has been cut off"
		elif self.health<=0:
			return "it is dead"

	@desc.setter
	def desc_setter(self,value):
		self._desc=value
		return 

def hit(noun):
	'''
	攻击
	noun-子类名
	thing-实例
	'''
	if  noun in GameObjects.objects:
		thing=GameObjects.objects[noun]  
		if type(thing)==Goblin:
			thing.health=thing.health-1
			if thing.health<=0:  #注意必须加上<，否则dead一次就会一直报hit
				msg="you kill the {}".format(noun)
			else:
				msg="you hit the {}".format(noun)
	else:
		msg= "there is no {}".format(noun)
	print(msg)
	return thing.desc


#一个检验函数,如果创建了相应的子类，则返回它的描述，否则提示没有此类NPC
def examine(noun):  #noun-子类名
	if noun in GameObjects.objects:
		return GameObjects.objects[noun].get_desc()
	else:
		return "There is no {} .".format(noun)

verb_dict={
	"say":say,
	"examine":examine,
	"hit":hit
}

gob=Goblin("gob")

while True:
	get_command()
